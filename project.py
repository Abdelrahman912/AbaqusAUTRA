# -*- coding: mbcs -*-
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

mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=200.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-30.0, 100.0), 
    point2=(-30.0, -100.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-30.0, -100.0), 
    point2=(30.0, -100.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, -100.0), 
    point2=(30.0, -76.25))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-30.0, 100.0), 
    point2=(30.0, 100.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, 100.0), 
    point2=(30.0, 73.75))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -76.3597717285156, -33.6916427612305), value=200.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    0.971880435943604, -109.753982543945), value=60.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -8.12269973754883, 115.462913513184), value=60.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    115.329849243164, 84.779167175293), value=20.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    103.734817504883, -91.8227615356445), value=20.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, 80.0), point2=
    (20.0, 80.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 80.0), point2=
    (20.0, 93.1319198608398))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(20.0, 
    93.1319198608398), point2=(-20.8456573486328, 93.1319198608398))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[8], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-20.8456573486328, 
    93.1319198608398), point2=(-20.8456573486328, -92.2037734985352))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-20.8456573486328, 
    -92.2037734985352), point2=(17.7379150390625, -92.2037734985352))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(17.7379150390625, 
    -92.2037734985352), point2=(17.7379150390624, -77.5))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[12])
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].constraints[43], ))
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[12], ))
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    20.0905914306641, 52.6779403686523), value=5.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[5], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[6])
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[9], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], textPoint=(
    145.251937866211, 99.7174606323242), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[10], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], textPoint=(
    -24.1393737792969, -118.545906066895), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[11], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], textPoint=(
    152.30989074707, -102.082069396973), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].DistanceDimension(entity1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[10], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], textPoint=(
    22.9137725830078, -53.1609802246094), value=5.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(30.0, -80.0), 
    point2=(25.0, -80.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[4], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(25.0, -80.0), 
    point2=(25.0, -95.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[14])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[13], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[14])
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='Csection-beam', type=
    DEFORMABLE_BODY)

mdb.models['Model-1'].parts['Csection-beam'].BaseSolidExtrude(depth=1200.0, 
    sketch=mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']


# create holes
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=60.84, name='__profile__', 
    sheetSize=2433.84, transform=
    mdb.models['Model-1'].parts['Csection-beam'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Csection-beam'].faces[10], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Csection-beam'].edges[33], 
    sketchOrientation=RIGHT, origin=(-30.0, 0.0, 600.0)))
mdb.models['Model-1'].parts['Csection-beam'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Model-1'].sketches['__profile__'])

mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    gridOrigin=(-600.0, 100.0))


mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -550.0, 50.0), point1=(-539.16, 54.37))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], radius=7.0, 
    textPoint=(-486.546508789063, 142.814453125))

mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    270.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[6], 
    ), number1=4, number2=3, spacing1=100.0, spacing2=50.0, vertexList=())
mdb.models['Model-1'].parts['Csection-beam'].CutExtrude(flipExtrudeDirection=
    OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=RIGHT, sketchPlane=
    mdb.models['Model-1'].parts['Csection-beam'].faces[10], sketchPlaneSide=
    SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['Csection-beam'].edges[33])
del mdb.models['Model-1'].sketches['__profile__']



mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=410.0)
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-200.0, 205.0), 
    point2=(-200.0, -205.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[2])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-200.0, -205.0), 
    point2=(-20.0, -205.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-20.0, -205.0), 
    point2=(130.0, -70.0))
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-200.0, 205.0), 
    point2=(130.0, 205.0))
mdb.models['Model-1'].sketches['__profile__'].HorizontalConstraint(
    addUndoState=False, entity=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(130.0, 205.0), 
    point2=(130.0, -70.0))
mdb.models['Model-1'].sketches['__profile__'].VerticalConstraint(addUndoState=
    False, entity=mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].PerpendicularConstraint(
    addUndoState=False, entity1=
    mdb.models['Model-1'].sketches['__profile__'].geometry[5], entity2=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -355.502075195313, -31.5676612854004), value=410.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -52.4679069519043, 259.212310791016), value=400.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[0], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    327.237609863281, 77.9310607910156), value=200.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[4], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[3])
mdb.models['Model-1'].sketches['__profile__'].ObliqueDimension(textPoint=(
    -87.7610626220703, -246.915176391602), value=200.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[1], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[2])
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='plate', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['plate'].BaseSolidExtrude(depth=3.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=28.64, name='__profile__', 
    sheetSize=1145.61, transform=
    mdb.models['Model-1'].parts['plate'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['plate'].faces[5], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['plate'].edges[0], 
    sketchOrientation=RIGHT, origin=(-19.58042, 19.825175, 3.0)))
mdb.models['Model-1'].parts['plate'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    gridOrigin=(-180.41958, 185.174825))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -130.41958, 135.174825), point1=(-151.77958, 156.534825))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[7], radius=7.0, 
    textPoint=(-257.415948408203, 111.651830004883))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    270.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[7], 
    ), number1=4, number2=3, spacing1=100.0, spacing2=50.0, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    gridOrigin=(-180.41958, -224.825175))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -130.41958, -174.825175), point1=(-123.13958, -167.545175))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[19], radius=7.0, 
    textPoint=(-208.534234541016, -125.704897595215))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    90.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[19], 
    ), number1=3, number2=3, spacing1=50.0, spacing2=50.0, vertexList=())
mdb.models['Model-1'].sketches['__profile__'].VerticalDimension(textPoint=(
    -274.112939375, -41.0067202575684), value=110.0, vertex1=
    mdb.models['Model-1'].sketches['__profile__'].vertices[21], vertex2=
    mdb.models['Model-1'].sketches['__profile__'].vertices[41])
mdb.models['Model-1'].parts['plate'].CutExtrude(flipExtrudeDirection=OFF, 
    sketch=mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=
    RIGHT, sketchPlane=mdb.models['Model-1'].parts['plate'].faces[5], 
    sketchPlaneSide=SIDE1, sketchUpEdge=
    mdb.models['Model-1'].parts['plate'].edges[0])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].Part(name='Csection-column', objectToCopy=
    mdb.models['Model-1'].parts['Csection-beam'])
mdb.models['Model-1'].parts['Csection-column'].features['Solid extrude-1'].setValues(
    depth=890.0)
mdb.models['Model-1'].parts['Csection-column'].regenerate()
del mdb.models['Model-1'].parts['Csection-column'].features['Cut extrude-1']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=45.63, name='__profile__', 
    sheetSize=1825.37, transform=
    mdb.models['Model-1'].parts['Csection-column'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Csection-column'].faces[10], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Csection-column'].edges[32], 
    sketchOrientation=RIGHT, origin=(-30.0, 0.0, 445.0)))
mdb.models['Model-1'].parts['Csection-column'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].sketchOptions.setValues(
    gridOrigin=(-100.0, 445.0))
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    -50.0, 395.0), point1=(-42.9625, 410.7775))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[6], radius=7.0, 
    textPoint=(-431.173400878906, 340.966156005859))
mdb.models['Model-1'].sketches['__profile__'].linearPattern(angle1=0.0, angle2=
    270.0, geomList=(mdb.models['Model-1'].sketches['__profile__'].geometry[6], 
    ), number1=3, number2=3, spacing1=50.0, spacing2=50.0, vertexList=())
mdb.models['Model-1'].parts['Csection-column'].CutExtrude(flipExtrudeDirection=
    OFF, sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchOrientation=RIGHT, sketchPlane=
    mdb.models['Model-1'].parts['Csection-column'].faces[10], sketchPlaneSide=
    SIDE1, sketchUpEdge=
    mdb.models['Model-1'].parts['Csection-column'].edges[32])
del mdb.models['Model-1'].sketches['__profile__']
# Save by User on 2024_06_24-21.36.33; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=12.0)
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(0.35, -0.35))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[2], radius=6.0, 
    textPoint=(-2.74163675308228, 0.888970077037811))
mdb.models['Model-1'].Part(dimensionality=THREE_D, name='bolt', type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].parts['bolt'].BaseSolidExtrude(depth=13.0, sketch=
    mdb.models['Model-1'].sketches['__profile__'])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.06, name='__profile__', 
    sheetSize=42.7, transform=
    mdb.models['Model-1'].parts['bolt'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['bolt'].faces[1], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['bolt'].edges[0], 
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 13.0)))
mdb.models['Model-1'].parts['bolt'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(7.685, 0.795))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], radius=9.0, 
    textPoint=(-9.1439037322998, 0.315985441207886))
mdb.models['Model-1'].parts['bolt'].SolidExtrude(depth=4.0, 
    flipExtrudeDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, 
    sketchPlane=mdb.models['Model-1'].parts['bolt'].faces[1], sketchPlaneSide=
    SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['bolt'].edges[0])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=1.06, name='__profile__', 
    sheetSize=42.7, transform=
    mdb.models['Model-1'].parts['bolt'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['bolt'].faces[4], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['bolt'].edges[3], 
    sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
mdb.models['Model-1'].parts['bolt'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].CircleByCenterPerimeter(center=(
    0.0, 0.0), point1=(8.745, 1.325))
mdb.models['Model-1'].sketches['__profile__'].RadialDimension(curve=
    mdb.models['Model-1'].sketches['__profile__'].geometry[3], radius=9.0, 
    textPoint=(-13.4586305618286, -0.912706673145294))
mdb.models['Model-1'].parts['bolt'].SolidExtrude(depth=4.0, 
    flipExtrudeDirection=OFF, sketch=
    mdb.models['Model-1'].sketches['__profile__'], sketchOrientation=RIGHT, 
    sketchPlane=mdb.models['Model-1'].parts['bolt'].faces[4], sketchPlaneSide=
    SIDE1, sketchUpEdge=mdb.models['Model-1'].parts['bolt'].edges[3])
del mdb.models['Model-1'].sketches['__profile__']
# Save by User on 2024_06_24-21.42.14; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].Material(description=
    'this is the mterial of beams, columns and plate', name='steel')
mdb.models['Model-1'].materials['steel'].Elastic(table=((210000.0, 0.33), ))
mdb.models['Model-1'].materials['steel'].Plastic(table=((350.0, 0.0), (520.0, 
    0.11083)))
mdb.models['Model-1'].Material(name='steel-bolt', objectToCopy=
    mdb.models['Model-1'].materials['steel'])
mdb.models['Model-1'].materials['steel-bolt'].setValues(description=
    'this is the mterial of bolts')
mdb.models['Model-1'].HomogeneousSolidSection(material='steel', name=
    'Csection-plate', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='steel-bolt', name=
    'bolt-section', thickness=None)
mdb.models['Model-1'].parts['bolt'].Set(cells=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), name='Set-1')
mdb.models['Model-1'].parts['bolt'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['bolt'].sets['Set-1'], sectionName=
    'bolt-section', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['plate'].Set(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), name='Set-1')
mdb.models['Model-1'].parts['plate'].SectionAssignment(offset=0.0, offsetField=
    '', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['plate'].sets['Set-1'], sectionName=
    'Csection-plate', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Csection-column'].Set(cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#1 ]', ), ), name='Set-1')
mdb.models['Model-1'].parts['Csection-column'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Csection-column'].sets['Set-1'], sectionName=
    'Csection-plate', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Csection-beam'].Set(cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#1 ]', ), ), name='Set-1')
mdb.models['Model-1'].parts['Csection-beam'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=
    mdb.models['Model-1'].parts['Csection-beam'].sets['Set-1'], sectionName=
    'Csection-plate', thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#1 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[36], point2=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[38], point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[37], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#4 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[46], point2=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[47], point3=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[16])
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#1f ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[73], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[0], MIDDLE), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[76], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlanePointNormal(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#1f0 ]', ), ), normal=
    mdb.models['Model-1'].parts['Csection-beam'].edges[80], point=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[80], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#822 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[147], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[46], MIDDLE), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[136], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#101f0 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[49], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[49], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[48], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#f0c00 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[157], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[192], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[145], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#30006c ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[65], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[260], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[60], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#39c ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[100], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[76], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[154], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#10084005 #24 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[74], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[73], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[172], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#2c0000 #1a01 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[158], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[166], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[251], CENTER))
# Save by User on 2024_06_24-22.01.11; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#1 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[23], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[29], MIDDLE), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[25], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#2 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[30], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[26], MIDDLE), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[56], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#7 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[71], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[46], MIDDLE), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[44], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#2c ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[78], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[106], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[69], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#160 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[172], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[123], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[174], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#14a ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[169], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[61], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[133], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#14a0 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[94], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[233], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[65], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#10a02 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[58], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[73], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[177], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#783995 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].vertices[189], point2=
    mdb.models['Model-1'].parts['Csection-column'].vertices[188], point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[369], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#ffa0fbe0 #f ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[85], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-column'].vertices[60], point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[347], MIDDLE))
# Save by User on 2024_06_24-22.06.15; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].parts['bolt'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), point1=mdb.models['Model-1'].parts['bolt'].InterestingPoint(
    mdb.models['Model-1'].parts['bolt'].edges[5], CENTER), point2=
    mdb.models['Model-1'].parts['bolt'].vertices[5], point3=
    mdb.models['Model-1'].parts['bolt'].vertices[3])
mdb.models['Model-1'].parts['bolt'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#3 ]', ), 
    ), point1=mdb.models['Model-1'].parts['bolt'].InterestingPoint(
    mdb.models['Model-1'].parts['bolt'].edges[14], CENTER), point2=
    mdb.models['Model-1'].parts['bolt'].InterestingPoint(
    mdb.models['Model-1'].parts['bolt'].edges[14], MIDDLE), point3=
    mdb.models['Model-1'].parts['bolt'].InterestingPoint(
    mdb.models['Model-1'].parts['bolt'].edges[16], MIDDLE))
mdb.models['Model-1'].parts['bolt'].DatumPlaneByOffset(flip=SIDE1, offset=0.0, 
    plane=mdb.models['Model-1'].parts['bolt'].faces[28])
mdb.models['Model-1'].parts['bolt'].DatumPlaneByOffset(flip=SIDE1, offset=0.0, 
    plane=mdb.models['Model-1'].parts['bolt'].faces[13])
mdb.models['Model-1'].parts['bolt'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#f ]', ), 
    ), datumPlane=mdb.models['Model-1'].parts['bolt'].datums[7])
mdb.models['Model-1'].parts['bolt'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#b8 ]', ), 
    ), datumPlane=mdb.models['Model-1'].parts['bolt'].datums[8])
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[40], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[41], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[36], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#1 ]', ), 
    ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[58], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[89], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[56], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#2 ]', ), 
    ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[54], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[55], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[125], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#f ]', ), 
    ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[164], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[100], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[117], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#f0 ]', 
    ), ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[102], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[73], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[193], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#a0a ]', 
    ), ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[175], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[70], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[165], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#4028 ]', 
    ), ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[284], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[32], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[33], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#4 ]', ), 
    ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[325], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[75], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[76], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#10cb ]', 
    ), ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[361], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[162], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[141], CENTER))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#458a ]', 
    ), ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[270], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[56], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[270], MIDDLE))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask(('[#8525 ]', 
    ), ), point1=mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[51], CENTER), point2=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[68], CENTER), point3=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[51], MIDDLE))
# Save by User on 2024_06_24-22.18.21; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name=
    'Csection-beam-1', part=mdb.models['Model-1'].parts['Csection-beam'])
mdb.models['Model-1'].rootAssembly.rotate(angle=180.0, axisDirection=(0.0, 0.0, 
    -10.0), axisPoint=(30.0, 100.0, 1150.0), instanceList=('Csection-beam-1', 
    ))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='plate-1', part=
    mdb.models['Model-1'].parts['plate'])
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 
    -10.0, 0.0), axisPoint=(200.0, 105.0, 3.0), instanceList=('plate-1', ))
mdb.models['Model-1'].rootAssembly.rotate(angle=180.0, axisDirection=(0.0, 
    -10.0, 0.0), axisPoint=(203.0, 55.0, 3.0), instanceList=('plate-1', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('plate-1', ), 
    vector=(-113.0, 95.0, 797.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name=
    'Csection-beam-2', part=mdb.models['Model-1'].parts['Csection-beam'])
mdb.models['Model-1'].rootAssembly.instances['Csection-beam-2'].translate(
    vector=(129.0, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Csection-beam-2', )
    , vector=(-6.0, 200.0, 0.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name=
    'Csection-column-1', part=mdb.models['Model-1'].parts['Csection-column'])
mdb.models['Model-1'].rootAssembly.instances['Csection-column-1'].translate(
    vector=(189.0, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.rotate(angle=270.0, axisDirection=(-10.0, 
    0.0, 0.0), axisPoint=(214.0, -95.0, 890.0), instanceList=(
    'Csection-column-1', ))
mdb.models['Model-1'].rootAssembly.rotate(angle=180.0, axisDirection=(0.0, 
    -10.0, 0.0), axisPoint=(159.0, 645.0, 1085.0), instanceList=(
    'Csection-column-1', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Csection-column-1', 
    ), vector=(-69.0, -705.0, -85.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name=
    'Csection-column-2', part=mdb.models['Model-1'].parts['Csection-column'])
mdb.models['Model-1'].rootAssembly.instances['Csection-column-2'].translate(
    vector=(189.0, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.rotate(angle=270.0, axisDirection=(-10.0, 
    0.0, 0.0), axisPoint=(214.0, -95.0, 890.0), instanceList=(
    'Csection-column-2', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('Csection-column-2', 
    ), vector=(-66.0, -705.0, 115.0))
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bolt-1', part=
    mdb.models['Model-1'].parts['bolt'])
mdb.models['Model-1'].rootAssembly.instances['bolt-1'].translate(vector=(
    164.88, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(1.028992, 
    -9.946918, 0.0), axisPoint=(163.953908, 8.952226, 17.0), instanceList=(
    'bolt-1', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bolt-1', ), vector=
    (-83.789761, 248.250714, 1133.000001))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bolt-1', ), vector=
    (-71.052675, 20.636177, 49.999999))
del mdb.models['Model-1'].rootAssembly.features['bolt-1']
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bolt-1', part=
    mdb.models['Model-1'].parts['bolt'])
mdb.models['Model-1'].rootAssembly.instances['bolt-1'].translate(vector=(
    164.88, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(0.0, 
    -10.0, 0.0), axisPoint=(153.0, -60.0, 1000.0), instanceList=('bolt-1', ))
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bolt-1', ), vector=
    (-1060.0, 145.050253, 133.170253))
del mdb.models['Model-1'].rootAssembly.features['bolt-1']
mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='bolt-1', part=
    mdb.models['Model-1'].parts['bolt'])
mdb.models['Model-1'].rootAssembly.instances['bolt-1'].translate(vector=(
    164.88, 0.0, 0.0))
mdb.models['Model-1'].rootAssembly.rotate(angle=90.0, axisDirection=(-1.028992, 
    9.946918, 0.0), axisPoint=(164.88, 0.0, -4.0), instanceList=('bolt-1', ))
mdb.models['Model-1'].rootAssembly.ParallelFace(fixedPlane=
    mdb.models['Model-1'].rootAssembly.instances['Csection-beam-2'].faces[303], 
    flip=OFF, movablePlane=
    mdb.models['Model-1'].rootAssembly.instances['bolt-1'].faces[46])
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bolt-1', ), vector=
    (-83.375482, 37.859393, 1154.0))
mdb.models['Model-1'].rootAssembly.LinearInstancePattern(direction1=(0.0, 0.0, 
    -1.0), direction2=(0.0, -1.0, 0.0), instanceList=('bolt-1', ), number1=3, 
    number2=3, spacing1=50.0, spacing2=50.0)
mdb.models['Model-1'].rootAssembly.LinearInstancePattern(direction1=(-1.0, 0.0, 
    0.0), direction2=(0.0, 1.0, 0.0), instanceList=('bolt-1', ), number1=1, 
    number2=2, spacing1=21.0, spacing2=500.0)
mdb.models['Model-1'].rootAssembly.translate(instanceList=('bolt-1-lin-1-2-1', 
    ), vector=(0.0, -290.0, 0.0))
mdb.models['Model-1'].rootAssembly.LinearInstancePattern(direction1=(0.0, 0.0, 
    -1.0), direction2=(0.0, -1.0, 0.0), instanceList=('bolt-1-lin-1-2-1', ), 
    number1=4, number2=3, spacing1=100.0, spacing2=50.0)
# Save by User on 2024_06_24-22.53.07; build 2020 2019_09_13-19.49.31 163176
# Save by User on 2024_06_24-22.53.38; build 2020 2019_09_13-19.49.31 163176
# Save by User on 2024_06_24-23.36.58; build 2020 2019_09_13-19.49.31 163176
