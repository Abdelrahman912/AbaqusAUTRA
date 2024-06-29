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

def create_csection_part(abaqus_model,section,length,part_name,conn_config):
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
    p9 = (b/2 - t, h/2 - t)
    p10 = (b/2 - t,h/2  - c)
    p11 = (b/2, h/2 - c)
    p12 = (b/2, h/2)
    # create solid part
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
    # create holes
    # choose face to sketch on
    abaqus_model.ConstrainedSketch(gridSpacing=60.84, name=
    '__profile__', sheetSize=2 * length, transform=
    abaqus_model.parts[str(part_name)].MakeSketchTransform(
    sketchPlane=abaqus_model.parts[str(part_name)].faces[10], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=abaqus_model.parts[str(part_name)].edges[33], 
    sketchOrientation=RIGHT, origin=(-b/2, 0.0, length/2)))
    abaqus_model.parts[str(part_name)].projectReferencesOntoSketch(
        filter=COPLANAR_EDGES, sketch=
        abaqus_model.sketches['__profile__'])
    # abaqus_model.sketches['__profile__'].sketchOptions.setValues(
    # gridOrigin=(-length/2, h/2))

    nl = conn_config.NoL
    nt = conn_config.NoT
    pl = conn_config.PL
    pt = conn_config.PT
    el = conn_config.EL
    et = conn_config.ET
    r = conn_config.HoleDia/2

    # create holes
    center = (-length/2 +  el, h/2 - et)
    abaqus_model.sketches['__profile__'].CircleByCenterPerimeter(
    center=center, point1=(-length/2 + el + r, h/2 -  et))

    # create linear pattern
    abaqus_model.sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    270.0, geomList=(abaqus_model.sketches['__profile__'].geometry[6], 
    ), number1=nl, number2=nt, spacing1=pl, spacing2=pt, vertexList=())

    # define extrusion
    abaqus_model.parts[str(part_name)].CutExtrude(flipExtrudeDirection=
    OFF, sketch=abaqus_model.sketches['__profile__'], 
    sketchOrientation=RIGHT, sketchPlane=
    abaqus_model.parts[str(part_name)].faces[10], sketchPlaneSide=
    SIDE1, sketchUpEdge=abaqus_model.parts[str(part_name)].edges[33], upToFace=
        abaqus_model.parts[str(part_name)].faces[4])
    del abaqus_model.sketches['__profile__']


def create_head_extrusion(abaqus_model,bolt_part,head_r,head_length,origin,face_index,edge_index):
    abaqus_model.ConstrainedSketch(gridSpacing=1.06, name='__profile__', 
    sheetSize=head_r * 2, transform=
        bolt_part.MakeSketchTransform(sketchPlane=bolt_part.faces[face_index], sketchPlaneSide=SIDE1, sketchUpEdge=bolt_part.edges[edge_index], 
        sketchOrientation=RIGHT, origin=origin))

    bolt_part.projectReferencesOntoSketch(filter= COPLANAR_EDGES, sketch=abaqus_model.sketches['__profile__'])
    abaqus_model.sketches['__profile__'].CircleByCenterPerimeter(center=(0,0), point1=(head_r, 0))
    bolt_part.SolidExtrude(depth=head_length, flipExtrudeDirection=OFF, sketch=abaqus_model.sketches['__profile__'], sketchOrientation=RIGHT, 
        sketchPlane=bolt_part.faces[face_index], sketchPlaneSide= SIDE1, sketchUpEdge=bolt_part.edges[edge_index])
    del abaqus_model.sketches['__profile__']

def create_bolt_part(abaqus_model,bolt,tp,tc):
    bolt_name = bolt.Name
    shank_r = bolt.ShankDia / 2
    shank_length = 2*tc + tp
    head_length = bolt.HeadLength
    head_r = bolt.HeadDia / 2

    # Create sketch for shank
    center = (0,0)
    p1 = (shank_r,0)
    abaqus_model.ConstrainedSketch(name='__profile__', sheetSize=bolt.ShankDia)
    abaqus_model.sketches['__profile__'].CircleByCenterPerimeter(center=center, point1=p1)
    bolt_part = abaqus_model.Part(dimensionality=THREE_D, name=str(bolt_name), type=
        DEFORMABLE_BODY)
    bolt_part.BaseSolidExtrude(depth=shank_length, sketch=
        abaqus_model.sketches['__profile__'])
    del abaqus_model.sketches['__profile__']

    # Create sketch for head
    create_head_extrusion(abaqus_model,bolt_part,head_r,head_length,(0,0,shank_length),1,0)
    create_head_extrusion(abaqus_model,bolt_part,head_r,head_length,(0,0,0),4,3)



def run_script(logging,input_params):
    logging.info(" Starting script... ")
    models = input_params.Models
    for mi, model in enumerate(models):
        model_name = model.Name
        logging.info(" Starting model [" + model_name + "]...")
        abaqus_model = create_model(model_name)

        ## Part ---------------------------------------------------------------------

        beam = model.Geometry.Beam
        beam_conn_config = beam.ConnectionConfig
        column = model.Geometry.Column
        column_conn_config = column.ConnectionConfig
        bolt = model.Geometry.Bolt

        # Create part
        logging.info("Creating parts...")
        # Create beam part
        create_csection_part(abaqus_model,beam.Section,beam.Length,"beam",beam_conn_config)
        # Create column part
        create_csection_part(abaqus_model,column.Section,column.ClearHeight,"column",column_conn_config)
        # Create bolt part
        create_bolt_part(abaqus_model,bolt,column.Section.t,beam.Section.t)


        logging.info("Saving model...")
        mdb.saveAs(pathName=str(input_params.CaeName + ".cae"))
        logging.info(" Script finished... ")
       
    
    
    
    