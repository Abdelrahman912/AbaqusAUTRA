from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *


class CSVAppender:
    def __init__(self, file_path):
        self.file_path = file_path
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as csvfile:
                csv_writer = csv.writer(csvfile)
                

    def append_row(self, args):
        with open(self.file_path, 'a') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(args)

def submit_job(job, logging):
    logging.info("Running job: " + job.name)
    job.submit()
    job.waitForCompletion()

def mesh_sensitivity(model_name,jobs, step_name,logging):
    csw_writer = CSVAppender("sensitivity_results-" + str(model_name) + ".csv")
    for job in jobs:
        # open results file
        odb_name = job.name + ".odb"
        odb = session.openOdb(name=str(odb_name))
        # get the step where the results are
        step = odb.steps[str(step_name)]

        # get the vectors that store the results
        stress_field = step.frames[-1].fieldOutputs["S"]
        all_stresses = stress_field
        all_mises = []
        for i in range(len(all_stresses.values)):
            # get the s11 of the integration point and store it in s11_vector
            all_mises.append(all_stresses.values[i].mises)
        # print the highest value in s11_vector
        max_mises = max(all_mises)
        logging.info("Max Mises Stress = " + str(max_mises))
        num_elements = 0
        for instance in odb.rootAssembly.instances.values():
            num_elements += len(instance.elements)
        logging.info("Number of elements = " + str(num_elements))
        csw_writer.append_row([num_elements, max_mises,job.name])
    



def load_disp(model_name,jobs, step_name,logging):
    csw_writer = CSVAppender("load disp-" + str(model_name) + ".csv")
    # Define the path to the ODB file
    for job in jobs:
        # Open the ODB file
        odb_name = job.name + ".odb"
        odb = session.openOdb(name=str(odb_name))
        # Define the node set you are interested in
        disp_node_set_name = 'beam_loading_ref_point-Output Set'
        rf2_node_set_name = 'fixed_support_ref_point-Output Set'

        # Get the node set
        disp_node_set = odb.rootAssembly.nodeSets[disp_node_set_name]
        rf2_node_set = odb.rootAssembly.nodeSets[rf2_node_set_name]

        # Initialize lists to hold the RF2 and U2 values
        rf2_values = []
        u2_values = []

        # Access the history region for each node in the node set
        for node in disp_node_set.nodes[0]:
            node_label = node.label
            u2_history_region = odb.steps[step_name].historyRegions['Node ASSEMBLY.%s' % node_label]

            # # Extract U2 data
            logging.infor("Extracting U2 data")
            u2_data = u2_history_region.historyOutputs['U2'].data
            u2_values.append([u2 for time, u2 in u2_data])
            print(u2_values)


        for node in rf2_node_set.nodes[0]:
            node_label = node.label
            rf2_history_region = odb.steps[step_name].historyRegions['Node ASSEMBLY.%s' % node_label]
            # Extract RF2 data
            logging.info("Extracting RF2 data")
            rf2_data = rf2_history_region.historyOutputs['RF2'].data
            rf2_values.append([rf2 for time, rf2 in rf2_data])

        zipped = zip(u2_values,rf2_values)
        logging.info("Writing to CSV")
        for u2,rf2 in zipped:
            csw_writer.append_row([u2,rf2,job.name])
