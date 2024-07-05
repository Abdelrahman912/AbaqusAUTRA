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
    p1 = (-b/2.0, h/2.0)
    p2 = (-b/2.0, -h/2.0)
    p3 = (b/2.0, -h/2.0)
    p4 = (b/2.0, -h/2.0 + c)
    p5 = (b/2.0 - t, -h/2.0 + c)
    p6 = (b/2.0 -t, -h/2.0 + t)
    p7 = (-b/2.0 + t , -h/2.0 + t)
    p8 = (-b/2.0 + t, h/2.0 - t)
    p9 = (b/2.0 - t, h/2.0 - t)
    p10 = (b/2.0 - t,h/2.0  - c)
    p11 = (b/2.0, h/2.0 - c)
    p12 = (b/2.0, h/2.0)
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
    c_part = abaqus_model.Part(dimensionality=THREE_D, name=str(part_name), type=DEFORMABLE_BODY)
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
    sketchOrientation=RIGHT, origin=(-b/2, 0.0, length/2.0)))
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
    r = conn_config.HoleDia/2.0

    # create holes
    center = (-length/2.0 +  el, h/2.0 - et)
    abaqus_model.sketches['__profile__'].CircleByCenterPerimeter(
    center=center, point1=(-length/2.0 + el + r, h/2.0 -  et))

    # create linear pattern
    abaqus_model.sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    270.0, geomList=(abaqus_model.sketches['__profile__'].geometry[6], 
    ), number1=nl, number2=nt, spacing1=pl, spacing2=pt, vertexList=())

    # define extrusion
    abaqus_model.parts[str(part_name)].CutExtrude(flipExtrudeDirection=
    OFF, sketch=abaqus_model.sketches['__profile__'], 
    sketchOrientation=RIGHT, sketchPlane=
    abaqus_model.parts[str(part_name)].faces[10], sketchPlaneSide=
    SIDE1, sketchUpEdge=abaqus_model.parts[str(part_name)].edges[33], depth=t)

    #upToFace=abaqus_model.parts[str(part_name)].faces[4])
    del abaqus_model.sketches['__profile__']
    return c_part


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
    return bolt_part


def create_plate_part(abaqus_model,plate,beam,column,beam_col_clearance):
    beam_height = beam.Section.h
    column_height = column.Section.h
    b_nl = beam.ConnectionConfig.NoL
    b_nt = beam.ConnectionConfig.NoT
    b_pl = beam.ConnectionConfig.PL
    b_pt = beam.ConnectionConfig.PT
    b_el = beam.ConnectionConfig.EL
    b_et = beam.ConnectionConfig.ET
    c_nl = column.ConnectionConfig.NoL
    c_nt = column.ConnectionConfig.NoT
    c_pl = column.ConnectionConfig.PL
    c_pt = column.ConnectionConfig.PT
    c_el = column.ConnectionConfig.EL
    c_et = column.ConnectionConfig.ET
    tp = plate.t

    # define gusset plate axis aligned lines
    L1 = beam_height
    L2 = (b_nl -1) * b_pl + 2 * b_el
    L3 = L1 + beam_col_clearance + (c_nl - 1) * c_pl + 2 * c_el
    L4 = column_height

    # define gusset plate points
    p1 = (L2, -L1)
    p2 = (L2,0)
    p3 = (0,0)
    p4 = (0,-L3)
    p5 = (L4, -L3)

    # create sketch
    abaqus_model.ConstrainedSketch(name='__profile__', sheetSize=2*L2)
    abaqus_model.sketches['__profile__'].Line(point1=p1, point2=p2)
    abaqus_model.sketches['__profile__'].Line(point1=p2, point2=p3)
    abaqus_model.sketches['__profile__'].Line(point1=p3, point2=p4)
    abaqus_model.sketches['__profile__'].Line(point1=p4, point2=p5)
    abaqus_model.sketches['__profile__'].Line(point1=p5, point2=p1)
    plate_part = abaqus_model.Part(dimensionality=THREE_D, name=str(plate.Name), type=DEFORMABLE_BODY)

    # create solid part (extrusion)
    plate_part.BaseSolidExtrude(depth=plate.t, sketch=abaqus_model.sketches['__profile__'])
    del abaqus_model.sketches['__profile__']
    
    # create holes
   
    abaqus_model.ConstrainedSketch(gridSpacing=28.64, name='__profile__', 
        sheetSize=2 * L3, transform=plate_part.MakeSketchTransform(sketchPlane=plate_part.faces[5], sketchPlaneSide=SIDE1, 
        sketchUpEdge=plate_part.edges[12], 
        sketchOrientation=RIGHT, origin=(0, 0, 0)))
    
    plate_part.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=abaqus_model.sketches['__profile__'])
    # mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    #     gridOrigin=(-180.41958, 185.174825))
    # create holes due to beam connection
    beam_hole_r = beam.ConnectionConfig.HoleDia / 2
    abaqus_model.sketches['__profile__'].CircleByCenterPerimeter(center=(b_el, -b_et), point1=(b_el + beam_hole_r, -b_et))
    
    # create linear pattern
    abaqus_model.sketches['__profile__'].linearPattern(angle1=0.0, angle2=
        270.0, geomList=(abaqus_model.sketches['__profile__'].geometry[7], 
        ), number1=b_nl, number2=b_nt, spacing1=b_pl, spacing2=b_pt, vertexList=())
    
    # create holes due to column connection
    column_hole_r = column.ConnectionConfig.HoleDia / 2
    # # mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    # #     gridOrigin=(-180.41958, -224.825175))

    geom = abaqus_model.sketches['__profile__'].CircleByCenterPerimeter(center=(c_et, -(beam_height + beam_col_clearance + c_el)), 
                                                                 point1=(c_et + column_hole_r, -(beam_height + beam_col_clearance + c_el)))
    
    # create linear pattern
    abaqus_model.sketches['__profile__'].linearPattern(angle1=0.0, angle2=
        270, geomList=(geom, 
        ), number1=c_nt, number2=c_nl, spacing1=c_pt, spacing2=c_pl, vertexList=())
    
    #define cut extrusion
    plate_part.CutExtrude(flipExtrudeDirection=OFF, 
        sketch=abaqus_model.sketches['__profile__'], sketchOrientation=
        RIGHT, sketchPlane=plate_part.faces[5], 
        sketchPlaneSide=SIDE1, sketchUpEdge= plate_part.edges[12])
    del abaqus_model.sketches['__profile__']
    return plate_part


def assemble_parts(abaqus_model,beam,column,plate,bolt,beam_part,column_part,bolt_part,plate_part,beam_col_clearance):
    # define coordinate system
    abaqus_model.rootAssembly.DatumCsysByDefault(CARTESIAN)
    
    # create beam instances
    bh = beam.Section.h
    bl = beam.Length
    bb = beam.Section.b
    bt = beam.Section.t
    tp = plate.t

    beam1__inst_name = str(beam.Name + '-1')
    beam1_inst = abaqus_model.rootAssembly.Instance(dependent=ON, name= beam1__inst_name, part=beam_part)

    abaqus_model.rootAssembly.translate(instanceList=(beam1__inst_name, ), 
         vector=(bb/2.0 + tp, -bh/2.0, -bl))


    beam2__inst_name = str(beam.Name + '-2')
    beam2_inst = abaqus_model.rootAssembly.Instance(dependent=ON, name= beam2__inst_name, part=beam_part)
    abaqus_model.rootAssembly.rotate(angle=180, axisDirection=(0.0, 
        0.0, 1.0), axisPoint=(0, 0, 0), instanceList=(beam2__inst_name, ))
    
    abaqus_model.rootAssembly.translate(instanceList=(beam2__inst_name, ), 
         vector=(-(bb/2.0), -bh/2.0, -bl))

    # create plate instance
    plate_inst_name= str(plate.Name + '-1')
    abaqus_model.rootAssembly.Instance(dependent=ON, name=plate_inst_name, part=plate_part)
    abaqus_model.rootAssembly.rotate(angle=270, axisDirection=(0.0, 
        -10.0, 0.0), axisPoint=(0, 0, 0), instanceList=(plate_inst_name, ))
    
    # create column instance
    ch = column.Section.h
    cl = column.ClearHeight
    cb = column.Section.b

    column1__inst_name = str(column.Name + '-1')
    column1_inst = abaqus_model.rootAssembly.Instance(dependent=ON, name= column1__inst_name, part=column_part)

    abaqus_model.rootAssembly.rotate(angle=90, axisDirection=(1.0, 
        0.0, 0.0), axisPoint=(0, 0, 0), instanceList=(column1__inst_name, ))
    
    abaqus_model.rootAssembly.rotate(angle=180, axisDirection=(1.0, 
        0.0, 0.0), axisPoint=(0, -cl/2.0, 0 ), instanceList=(column1__inst_name, ))
    
    abaqus_model.rootAssembly.translate(instanceList=(column1__inst_name, ), 
         vector=((cb/2.0+tp), -bh -beam_col_clearance , -ch/2.0))
    

    column2__inst_name = str(column.Name + '-2')
    column2_inst = abaqus_model.rootAssembly.Instance(dependent=ON, name= column2__inst_name, part=column_part)

    abaqus_model.rootAssembly.rotate(angle=90, axisDirection=(1.0, 
        0.0, 0.0), axisPoint=(0, 0, 0), instanceList=(column2__inst_name, ))
    
    abaqus_model.rootAssembly.rotate(angle=180, axisDirection=(1.0, 
        0.0, 0.0), axisPoint=(0, -cl/2.0, 0 ), instanceList=(column2__inst_name, ))
    
    abaqus_model.rootAssembly.rotate(angle=180, axisDirection=(0.0, 
        1.0, 0.0), axisPoint=(0, 0, 0 ), instanceList=(column2__inst_name, ))
    
    abaqus_model.rootAssembly.translate(instanceList=(column2__inst_name, ), 
         vector=((-cb/2.0), -bh -beam_col_clearance , -ch/2.0))
    
    # create bolt instances
    beam_conn_config = beam.ConnectionConfig
    b_el = beam_conn_config.EL
    b_et = beam_conn_config.ET
    b_nl = beam_conn_config.NoL
    b_nt = beam_conn_config.NoT
    b_pl = beam_conn_config.PL
    b_pt = beam_conn_config.PT

    head_length = bolt.HeadLength
    shank_Length = 2*bt + tp

    # bolts in beam
    bolt_name = bolt.Name
    bolt_inst_name = str(bolt_name + '-1')
    bolt_inst = abaqus_model.rootAssembly.Instance(dependent=ON, name= bolt_inst_name, part=bolt_part)

    abaqus_model.rootAssembly.rotate(angle=90, axisDirection=(0.0, 
        1.0, 0.0), axisPoint=(0, 0, 0 ), instanceList=(bolt_inst_name, ))
    
    abaqus_model.rootAssembly.translate(instanceList=(bolt_inst_name, ), 
         vector=(-shank_Length/2.0 + tp/2.0 ,(-b_et), -b_el ))
    
    abaqus_model.rootAssembly.LinearInstancePattern(direction1=(0.0, 0.0, 
    -1.0), direction2=(0.0, -1.0, 0.0), instanceList=(bolt_inst_name, ), number1=b_nl, 
        number2=b_nt, spacing1=b_pl, spacing2=b_pt)
    
    # bolts in column
    column_conn_config = column.ConnectionConfig
    c_el = column_conn_config.EL
    c_et = column_conn_config.ET
    c_nl = column_conn_config.NoL
    c_nt = column_conn_config.NoT
    c_pl = column_conn_config.PL
    c_pt = column_conn_config.PT

    bolt_inst_name = str(bolt_name + '-2')
    bolt_inst = abaqus_model.rootAssembly.Instance(dependent=ON, name= bolt_inst_name, part=bolt_part)

    abaqus_model.rootAssembly.rotate(angle=90, axisDirection=(0.0, 
        1.0, 0.0), axisPoint=(0, 0, 0 ), instanceList=(bolt_inst_name, ))
    
    abaqus_model.rootAssembly.translate(instanceList=(bolt_inst_name, ), 
         vector=(-shank_Length/2.0 + tp/2.0 ,(-bh - beam_col_clearance-c_el), -c_et ))
    
    abaqus_model.rootAssembly.LinearInstancePattern(direction1=(0.0, 0.0, 
    -1.0), direction2=(0.0, -1.0, 0.0), instanceList=(bolt_inst_name, ), number1=c_nt, 
        number2=c_nl, spacing1=c_pl, spacing2=c_pt)
    
   
def partition_bolt(bolt_part):
    # Longitudinal partition of bolt
    bolt_part.PartitionCellByPlaneThreePoints(cells=
        bolt_part.cells.getSequenceFromMask(('[#1 ]', ), 
        ), point1=bolt_part.InterestingPoint(bolt_part.edges[5], CENTER), point2=bolt_part.vertices[5], point3=bolt_part.vertices[3])
        
    
    bolt_part.PartitionCellByPlaneThreePoints(cells=
        bolt_part.cells.getSequenceFromMask(('[#3 ]', ), 
        ), point1=bolt_part.InterestingPoint(
        bolt_part.edges[14], CENTER), point2=
        bolt_part.InterestingPoint(
        bolt_part.edges[14], MIDDLE), point3=
        bolt_part.InterestingPoint(
        bolt_part.edges[16], MIDDLE))
    
    datum1 = bolt_part.DatumPlaneByOffset(flip=SIDE1, offset=0.0,  plane=bolt_part.faces[28])
    datum2 = bolt_part.DatumPlaneByOffset(flip=SIDE1, offset=0.0, plane=bolt_part.faces[13])
    bolt_part.PartitionCellByDatumPlane(cells= bolt_part.cells.getSequenceFromMask(('[#f ]', ), 
        ), datumPlane=bolt_part.datums[datum1.id])
    bolt_part.PartitionCellByDatumPlane(cells=
        bolt_part.cells.getSequenceFromMask(('[#b8 ]', ), 
        ), datumPlane=bolt_part.datums[datum2.id])


def get_conn_length_L(conn_config):
    return (conn_config.NoL - 1) * conn_config.PL + 2 * conn_config.EL

def get_conn_length_T(conn_config):
    return (conn_config.NoT - 1) * conn_config.PT + 2 * conn_config.ET

def partition_c_part(c_part,c_input_model,part_length):
    conn_config = c_input_model.ConnectionConfig
    nl = conn_config.NoL
    nt = conn_config.NoT
    pl = conn_config.PL
    pt = conn_config.PT
    el = conn_config.EL
    et = conn_config.ET
    r = conn_config.HoleDia/2.0
    h = c_input_model.Section.h
    t = c_input_model.Section.t
    # Longitudinal partition of column.s
    length = part_length
    zo =   length - el
    yo = -h/2.0 + et
    for i in range(nt):
        y = yo + i * pt
        datum_plane = c_part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y)
        c_part.PartitionCellByDatumPlane(datumPlane=c_part.datums[datum_plane.id], cells=c_part.cells)
    
    
    long_range =2*nl - 1
    long_div =2.0
    if(0.75 * pl <= el ):
        long_range = nl
        long_div = 1.0
    for i in range( long_range):
        z = zo - i * pl/long_div
        datum_plane = c_part.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=z)
        c_part.PartitionCellByDatumPlane(datumPlane=c_part.datums[datum_plane.id], cells=c_part.cells)
    
    z = zo - (nl-1) * pl - el
    datum_plane = c_part.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=z)
    c_part.PartitionCellByDatumPlane(datumPlane=c_part.datums[datum_plane.id], cells=c_part.cells)

    # seperate the web from the flanges
    y_l = -h/2.0 + t
    y_u = h/2.0 - t

    lower_datum = c_part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y_l)
    upper_datum = c_part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y_u)
    c_part.PartitionCellByDatumPlane(datumPlane=c_part.datums[lower_datum.id], cells=c_part.cells)
    c_part.PartitionCellByDatumPlane(datumPlane=c_part.datums[upper_datum.id], cells=c_part.cells)

    # partition the remaining part of the column (i.e. part with no holes)
    n_part = 3.0
    part_step = ( z ) / n_part
    for i in range(1,int(n_part)):
        z = z - part_step
        datum_plane = c_part.DatumPlaneByPrincipalPlane(principalPlane=XYPLANE, offset=z)
        c_part.PartitionCellByDatumPlane(datumPlane=c_part.datums[datum_plane.id], cells=c_part.cells)
    
def partition_plate(plate_part,beam,column,beam_col_clearance):
    # beam part
    beam_height = beam.Section.h
    b_nl = beam.ConnectionConfig.NoL
    b_nt = beam.ConnectionConfig.NoT
    b_pl = beam.ConnectionConfig.PL
    b_pt = beam.ConnectionConfig.PT
    b_el = beam.ConnectionConfig.EL
    b_et = beam.ConnectionConfig.ET

    #partitions that are extended in the direction of the beam (Longitudinal partitions)
    yo = -b_et
    for i in range(b_nt):
        y = yo - i * b_pt
        datum_plane = plate_part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y)
        plate_part.PartitionCellByDatumPlane(datumPlane=plate_part.datums[datum_plane.id], cells=plate_part.cells)
    

    # partition the mid of the clearance between the beam and the column
    y = -beam_height - beam_col_clearance/2.0
    datum_plane = plate_part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y)
    plate_part.PartitionCellByDatumPlane(datumPlane=plate_part.datums[datum_plane.id], cells=plate_part.cells)

    # partitions that are extended in the direction of the column (Transverse partitions)
    long_range =2*b_nl - 1
    long_div =2.0
    if(0.75 * b_pl <= b_el ):
        long_range = b_nl
        long_div = 1.0
    xo = b_el
    for i in range(long_range):
        x = xo + i * b_pl/long_div
        datum_plane = plate_part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=x)
        plate_part.PartitionCellByDatumPlane(datumPlane=plate_part.datums[datum_plane.id], cells=plate_part.cells)

    # column part
    column_height = column.Section.h
    c_nl = column.ConnectionConfig.NoL
    c_nt = column.ConnectionConfig.NoT
    c_pl = column.ConnectionConfig.PL
    c_pt = column.ConnectionConfig.PT
    c_el = column.ConnectionConfig.EL
    c_et = column.ConnectionConfig.ET

    #partitions that are extended in the direction of the beam (Longitudinal partitions)
    yo = -beam_height - beam_col_clearance - c_el
    for i in range(c_nl):
        y = yo - i * c_pl
        datum_plane = plate_part.DatumPlaneByPrincipalPlane(principalPlane=XZPLANE, offset=y)
        plate_part.PartitionCellByDatumPlane(datumPlane=plate_part.datums[datum_plane.id], cells=plate_part.cells)
    
    # partitions that are extended in the direction of the column (Transverse partitions)
    #TODO: find a better way to partition the plate in the area where the column is connected
    #xo = c_et
    #for i in range(c_nt):
        #x = xo + i * c_pt
        #datum_plane = plate_part.DatumPlaneByPrincipalPlane(principalPlane=YZPLANE, offset=x)
        #plate_part.PartitionCellByDatumPlane(datumPlane=plate_part.datums[datum_plane.id], cells=plate_part.cells)



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
        plate = model.Geometry.Plate
        beam_col_clearance = model.Geometry.BeamColumnClearance

        # Create part
        logging.info("Creating parts...")
        # Create beam part
        beam_part = create_csection_part(abaqus_model,beam.Section,beam.Length,"beam",beam_conn_config)
        # Create column part
        col_part = create_csection_part(abaqus_model,column.Section,column.ClearHeight,"column",column_conn_config)
        # Create bolt part
        bolt_part = create_bolt_part(abaqus_model,bolt,plate.t,beam.Section.t)
        # Create plate part
        plate_part = create_plate_part(abaqus_model,plate,beam,column,model.Geometry.BeamColumnClearance)
        
        ## Partitioning ---------------------------------------------------------------------
        logging.info("Partitioning parts...")
        partition_bolt(bolt_part)
        partition_c_part(col_part,column,column.ClearHeight)
        partition_c_part(beam_part,beam,beam.Length)
        partition_plate(plate_part,beam,column,beam_col_clearance)

        ## Assembly ---------------------------------------------------------------------
        logging.info("Assembling parts...")
        assemble_parts(abaqus_model,beam,column,plate,bolt,beam_part,col_part,bolt_part,plate_part,beam_col_clearance)
        
        logging.info("Saving model...")
        mdb.saveAs(pathName=str(input_params.CaeName + ".cae"))
        logging.info(" Script finished... ")
       
    
    
    
    