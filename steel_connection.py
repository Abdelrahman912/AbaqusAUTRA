# Author: Abdelrahman Fathy Abdelrahman
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
from sys import __stdout__



def create_model(model_name):
    """
    Creates a new Abaqus model with the given name.

    Parameters:
    - model_name (str): The name of the model.

    Returns:
    - The newly created Abaqus model.
    """
    return mdb.Model(name=str(model_name))

def create_csection_part(abaqus_model,section,length,part_name):
    h = section.h
    b = section.b
    t = section.t
    c = section.c
    # Create sketch
    abaqus_model.ConstrainedSketch(name='__profile__', sheetSize=h)
    p1 = (-b/2, h/2)
    p2 = (-b/2, -h/2)
    p3 = (b/2, -h/2)
    p4 = (b/2, -h/2 + c)
    p5 = (b/2 - t, -h/2 + c)
    p6 = (b/2 -t, -h/2 + t)
    p7 = (-b/2 + t , -h/2 + t)
    p8 = (-b/2 + t, h/2 - t)
    p9 = (-b/2 + t, h/2 - t)
    p10 = (b/2 - t,h/2  - c)
    p11 = (b/2, h/2 - c)
    p12 = (b/2, h/2)
    abaqus_model.sketches['__profile__'].Line(point1=p1, point2=p2)
    abaqus_model.sketches['__profile__'].Line(point1=p2, point2=p3)
    abaqus_model.sketches['__profile__'].Line(point1=p3, point2=p4)
    abaqus_model.sketches['__profile__'].Line(point1=p4, point2=p5)
    abaqus_model.sketches['__profile__'].Line(point1=p5, point2=p6)
    abaqus_model.sketches['__profile__'].Line(point1=p6, point2=p7)
    abaqus_model.sketches['__profile__'].Line(point1=p7, point2=p8)
    abaqus_model.sketches['__profile__'].Line(point1=p8, point2=p9)
    abaqus_model.sketches['__profile__'].Line(point1=p9, point2=p10)
    abaqus_model.sketches['__profile__'].Line(point1=p10, point2=p11)
    abaqus_model.sketches['__profile__'].Line(point1=p11, point2=p12)
    abaqus_model.sketches['__profile__'].Line(point1=p12, point2=p1)
    abaqus_model.Part(dimensionality=THREE_D, name=str(part_name), type=DEFORMABLE_BODY)
    abaqus_model.parts[str(part_name)].BaseSolidExtrude(depth=length, 
        sketch=abaqus_model.sketches['__profile__'])
    del abaqus_model.sketches['__profile__']





def run_script(logging,input_params):
    logging.info(" Starting script... ")
    models = input_params.Models
    for mi, model in enumerate(models):
        model_name = model.Name
        logging.info(" Starting model [" + model_name + "]...")
        abaqus_model = create_model(model_name)

        ## Part ---------------------------------------------------------------------

        beam = model.Geometry.Beam
        column = model.Geometry.Column

        # Create part
        logging.info("Creating parts...")
        # Create beam part
        create_csection_part(abaqus_model,beam.Section,beam.Length,"beam")
        # Create column part
        create_csection_part(abaqus_model,column.Section,column.ClearHeight,"column")




        logging.info("Saving model...")
        mdb.saveAs(pathName=str(input_params.CaeName + ".cae"))
        logging.info(" Script finished... ")
       
    
    
    
    