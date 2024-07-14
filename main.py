from input import  StandardLogger, change_to_output_directory, map_json_to_objects
from steel_connection_mdb import * 
from steel_connection_odb import *
from sys import __stdout__


# Example usage
# Set the input file path
file_path = "input - main model.json" # for the main script
input_params = map_json_to_objects(file_path)
dir = input_params.DirectoryName
change_to_output_directory(dir)
logging = StandardLogger()
# The next two lines will basically inform the 'run-script' to do nothing after creating the jobs and after the jobs are completed   
on_jobs_completed_func = lambda model_name,jobs: None
on_job_creation_func = lambda job: None

run_script(logging, input_params,on_job_creation_func,on_jobs_completed_func)



#Example usage [Load Displacement]
# Set the input file path
# file_path = "input_load_disp.json"
# input_params = map_json_to_objects(file_path)
# # Set the output directory
# dir = input_params.DirectoryName
# change_to_output_directory(dir)
# logging = StandardLogger()
# step_name = input_params.LoadingStep.Name
# # Define the functions to be called when jobs are created and completed
# on_jobs_completed_func = lambda model_name,jobs: load_disp(model_name,jobs,step_name,logging)
# on_job_creation_func = lambda job: submit_job(job,logging)
# # Run the script
# run_script(logging, input_params,on_job_creation_func,on_jobs_completed_func)


#Example usage [Sensitive Analysis]
# Set the input file path
# file_path = "input_sensitivity.json"
# input_params = map_json_to_objects(file_path)
# # Set the output directory
# dir = input_params.DirectoryName
# change_to_output_directory(dir)
# logging = StandardLogger()
# step_name = input_params.LoadingStep.Name
# # Define the functions to be called when jobs are created and completed
# on_jobs_completed_func = lambda model_name,jobs: mesh_sensitivity(model_name,jobs,step_name,logging)
# on_job_creation_func = lambda job: submit_job(job,logging)
# # Run the script
# run_script(logging, input_params,on_job_creation_func,on_jobs_completed_func)