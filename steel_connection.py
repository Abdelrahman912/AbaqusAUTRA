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
import regionToolset
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


def define_bilinear_material(abaqus_model,material):
    name = material.Name
    E = material.E
    v = material.v
    description = material.Description
    Fy = material.Fy
    Fu = material.Fu
    EpsPlasticY = material.EpsPlasticY
    EpsPlasticU = material.EpsPlasticU
    abaqus_mat = abaqus_model.Material(description=str(description), name=str(name))
    abaqus_mat.Elastic(table=((E, v), ))
    abaqus_mat.Plastic(table=((Fy, EpsPlasticY), (Fu, EpsPlasticU)))
    return abaqus_mat
    
def define_solid_section(abaqus_model,material_name,section_name):
    return abaqus_model.HomogeneousSolidSection(material=str(material_name), name=str(section_name), thickness=None)

def assign_section_to_part(part,part_name,section_name):
    set_name = part_name + '-Set'
    part.Set(cells=part.cells.getSequenceFromMask(('[#1 ]', ), ), name=str(set_name))
    part.SectionAssignment(region=part.sets[str(set_name)], sectionName=section_name, offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


DYNAMIC_IMPLICIT = 'DYNAMIC_IMPLICIT'
STATIC_GENERAL = 'STATIC_GENERAL'

def define_dynamic_implicit_step(abaqus_model,loading_step):
    name = loading_step.Name
    time_period = loading_step.TimePeriod
    initial_inc = loading_step.InitialInc
    min_inc = loading_step.MinInc
    max_num_inc = loading_step.MaxNumInc
    return abaqus_model.ImplicitDynamicsStep(alpha=DEFAULT, amplitude=RAMP, 
        application=QUASI_STATIC, initialConditions=OFF, initialInc=initial_inc, 
        maxNumInc=max_num_inc, minInc=min_inc, name=str(name)
        , nlgeom=ON, nohaf=OFF, previous='Initial', timePeriod=time_period)
   

def define_contact_interaction(abaqus_model,contact):
    name = contact.Name
    fric_coeff = contact.FrictionCoeff
    contact_prop = abaqus_model.ContactProperty(str(name))
    contact_prop.TangentialBehavior(
        dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
        formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
        pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
        table=((fric_coeff, ), ), temperatureDependency=OFF)

    contact_prop.NormalBehavior(
        allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
        pressureOverclosure=HARD)
    int_name = 'Int - ' + name
    int_prop = abaqus_model.ContactStd(createStepName='Initial', name=str(int_name))
    int_prop.includedPairs.setValuesInStep(
        stepName='Initial', useAllstar=ON)
    int_prop.contactPropertyAssignments.appendInStep(
        assignments=((GLOBAL, SELF, str(name)), ), stepName='Initial')


def get_beam_loading_ref_point_coords(beam,plate):
    tp = plate.t
    x = tp/2.0
    y = -beam.Section.h/2.0
    z = -beam.Length
    return (x,y,z)

def get_fixed_support_coords(column,beam,plate,beam_col_clearance):
    tp = plate.t
    b_h = beam.Section.h
    col_length = column.ClearHeight
    x = tp/2.0
    y = -b_h - beam_col_clearance - col_length
    z = -column.Section.h/2.0
    return (x,y,z)

def define_ref_point(abaqus_model,coords,name):
    ref_point =  abaqus_model.rootAssembly.ReferencePoint(point=coords)
    abaqus_model.rootAssembly.features.changeKey(fromName=ref_point.name, toName=str(name))
    return ref_point



def is_face_within_bbox(face, bbox):
    """Check if all nodes of the face are within the bounding box."""
    for node in face.getNodes():
        x, y, z = node.coordinates
        if not (bbox[0] <= x <= bbox[1] and bbox[2] <= y <= bbox[3] and bbox[4] <= z <= bbox[5]):
            return False
    return True

def get_by_bbox(geom, bbox):
    xMin = bbox[0]
    xMax = bbox[1]
    yMin = bbox[2]
    yMax = bbox[3]
    zMin = bbox[4]
    zMax = bbox[5]
    return geom.getByBoundingBox(xMin, yMin, zMin, xMax, yMax, zMax)

def create_set_of_faces_by_bbox(abaqus_model,part_name, bbox, set_name):
    """Create a set of faces within the given bounding box."""
    inst_1 = part_name + '-1'
    inst_2 = part_name + '-2'
    #faces = part.faces.getByBoundingBox(-100,-250,-1100,1000.003,5,-1300)
    faces =get_by_bbox(abaqus_model.rootAssembly.instances[str(inst_1)].faces, bbox)
    faces += get_by_bbox(abaqus_model.rootAssembly.instances[str(inst_2)].faces, bbox)
    return abaqus_model.rootAssembly.Set(faces=faces, name=set_name)

def get_beam_loading_point_boundingbox(ref_point_coords,beam):
    db = beam.Section.b * 1.5
    dh = beam.Section.h * 1.5
    x = ref_point_coords[0]
    y = ref_point_coords[1]
    z = ref_point_coords[2]
    return [x-db, x+db, y-dh, y+dh, z-10, z+10]

def get_column_fixed_point_boundingbox(ref_point_coords,column):
    db = column.Section.b * 1.5
    dh = column.Section.h * 1.5
    x = ref_point_coords[0]
    y = ref_point_coords[1]
    z = ref_point_coords[2]
    return [x-db, x+db, y-10, y+10, z-dh, z+dh]

def define_rigid_body_constraint(abaqus_model, part_name,bounding_box, ref_point,constraint_name, set_name):
    """Define a rigid body."""
    set = create_set_of_faces_by_bbox(abaqus_model,part_name, bounding_box, set_name)
    abaqus_model.RigidBody(name=str(constraint_name), pinRegion= set
    , refPointRegion=Region(
        referencePoints=(abaqus_model.rootAssembly.referencePoints[ref_point.id], )))
    

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

        ## Material ---------------------------------------------------------------------
        logging.info("Defining materials...")
        steel_material = model.SteelMaterial
        bolt_material = model.BoltMaterial
        abaqus_steel_mat = define_bilinear_material(abaqus_model,steel_material)
        abaqus_bolt_mat = define_bilinear_material(abaqus_model,bolt_material)

        ## Section ---------------------------------------------------------------------
        logging.info("Defining sections...")
        steel_section_name = "steel_section"
        bolt_section_name = "bolt_section"
        abaqus_steel_section = define_solid_section(abaqus_model,steel_material.Name,steel_section_name)
        abaqus_bolt_section = define_solid_section(abaqus_model,bolt_material.Name,bolt_section_name)
        assign_section_to_part(beam_part,beam.Name,steel_section_name)
        assign_section_to_part(col_part,column.Name,steel_section_name)
        assign_section_to_part(bolt_part,bolt.Name,bolt_section_name)
        assign_section_to_part(plate_part,plate.Name,steel_section_name)

        ## Partitioning ---------------------------------------------------------------------
        logging.info("Partitioning parts...")
        partition_bolt(bolt_part)
        partition_c_part(col_part,column,column.ClearHeight)
        partition_c_part(beam_part,beam,beam.Length)
        partition_plate(plate_part,beam,column,beam_col_clearance)

        ## Assembly ---------------------------------------------------------------------
        logging.info("Assembling parts...")
        assemble_parts(abaqus_model,beam,column,plate,bolt,beam_part,col_part,bolt_part,plate_part,beam_col_clearance)
        
        ## Step ---------------------------------------------------------------------
        logging.info("Defining steps...")
        loading_step = model.LoadingStep
        step_type = loading_step.StepType
        if step_type == DYNAMIC_IMPLICIT:
            abaqus_step = define_dynamic_implicit_step(abaqus_model,loading_step)
        else:
            logging.error("Saving model...")
            raise ValueError("Step type not supported")
        
        ## Interaction ---------------------------------------------------------------------
        logging.info("Defining interactions...")
        contact = model.Contact
        define_contact_interaction(abaqus_model,contact)

        ## Boundary Conditions ---------------------------------------------------------------------
        logging.info("Defining boundary conditions...")
        # Define beam loading reference point
        beam_loading_ref_point_coords = get_beam_loading_ref_point_coords(beam,plate)
        beam_loading_ref_point = define_ref_point(abaqus_model,beam_loading_ref_point_coords,"beam_loading_ref_point")
        # Define beam loading ref point constraint
        beam_loading_ref_point_constraint_name = "loading_point_constraint"
        beam_loading_ref_point_set_name = "loading_point_set"
        beam_bb = get_beam_loading_point_boundingbox(beam_loading_ref_point_coords,beam)
        define_rigid_body_constraint(abaqus_model,beam.Name,beam_bb,beam_loading_ref_point,beam_loading_ref_point_constraint_name,beam_loading_ref_point_set_name)
        # Define fixed support reference point
        fixed_support_coords = get_fixed_support_coords(column,beam,plate,beam_col_clearance)
        fixed_support_ref_point = define_ref_point(abaqus_model,fixed_support_coords,"fixed_support_ref_point")
        # Define fixed support ref point constraint
        fixed_support_constraint_name = "fixed_support_constraint"
        fixed_support_set_name = "fixed_support_set"
        fixed_support_bb = get_column_fixed_point_boundingbox(fixed_support_coords,column)
        define_rigid_body_constraint(abaqus_model,column.Name,fixed_support_bb,fixed_support_ref_point,fixed_support_constraint_name,fixed_support_set_name)


        logging.info("Saving model...")
        mdb.saveAs(pathName=str(input_params.CaeName + ".cae"))
        logging.info("Script finished... ")
       
    
    
    
    