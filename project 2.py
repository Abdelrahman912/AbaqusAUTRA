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
# partion
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
# assembly
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


# step: static general
mdb.models['Model-1'].StaticStep(name='loading step', previous='Initial')


# contact
mdb.models['Model-1'].ContactProperty('contact peoperty')
mdb.models['Model-1'].interactionProperties['contact peoperty'].TangentialBehavior(
    dependencies=0, directionality=ISOTROPIC, elasticSlipStiffness=None, 
    formulation=PENALTY, fraction=0.005, maximumElasticSlip=FRACTION, 
    pressureDependency=OFF, shearStressLimit=None, slipRateDependency=OFF, 
    table=((0.35, ), ), temperatureDependency=OFF)

mdb.models['Model-1'].interactionProperties['contact peoperty'].NormalBehavior(
    allowSeparation=ON, constraintEnforcementMethod=DEFAULT, 
    pressureOverclosure=HARD)
mdb.models['Model-1'].ContactStd(createStepName='Initial', name='Int-1')
mdb.models['Model-1'].interactions['Int-1'].includedPairs.setValuesInStep(
    stepName='Initial', useAllstar=ON)
mdb.models['Model-1'].interactions['Int-1'].contactPropertyAssignments.appendInStep(
    assignments=((GLOBAL, SELF, 'contact peoperty'), ), stepName='Initial')

# Save by User on 2024_06_28-21.30.55; build 2020 2019_09_13-19.49.31 163176
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


# refrence points
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(91.5, -800.0, 1100.0))
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Csection-column-1'].edges.getSequenceFromMask(
    mask=('[#240000 #1f3c0 #0 #8400000 #70020000 #30 #0:6', 
    ' #58006800 #3c00 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Csection-column-2'].edges.getSequenceFromMask(
    mask=('[#240000 #1f3c0 #0 #8400000 #70020000 #30 #0:6', 
    ' #58006800 #3c00 ]', ), ), faces=
    mdb.models['Model-1'].rootAssembly.instances['Csection-column-1'].faces.getSequenceFromMask(
    mask=('[#5000 #20000000 #1 #0:2 #2001000 #1000 #0', ' #100 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Csection-column-2'].faces.getSequenceFromMask(
    mask=('[#5000 #20000000 #1 #0:2 #2001000 #1000 #0', ' #100 ]', ), ), name=
    'p_Set-1', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[59], ), vertices=
    mdb.models['Model-1'].rootAssembly.instances['Csection-column-1'].vertices.getSequenceFromMask(
    mask=('[#70033000 #f #8100e000 #11 #0:2 #c6000000 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Csection-column-2'].vertices.getSequenceFromMask(
    mask=('[#70033000 #f #8100e000 #11 #0:2 #c6000000 ]', ), ))

mdb.models['Model-1'].RigidBody(name='basement', pinRegion=
    mdb.models['Model-1'].rootAssembly.sets['p_Set-1'], refPointRegion=Region(
    referencePoints=(mdb.models['Model-1'].rootAssembly.referencePoints[59], 
    )))
mdb.models['Model-1'].rootAssembly.Set(name='Set-3', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[59], ))
mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Initial', 
    distributionType=UNIFORM, fieldName='', localCsys=None, name='BC-1', 
    region=mdb.models['Model-1'].rootAssembly.sets['Set-3'], u1=SET, u2=SET, 
    u3=SET, ur1=SET, ur2=SET, ur3=SET)
mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='RP-1', toName=
    'base reference point')
mdb.models['Model-1'].rootAssembly.ReferencePoint(point=(91.5, 200.0, 0.0))
mdb.models['Model-1'].rootAssembly.features.changeKey(fromName='RP-1', toName=
    'loading ref point')
mdb.models['Model-1'].rootAssembly.Set(edges=
    mdb.models['Model-1'].rootAssembly.instances['Csection-beam-1'].edges.getSequenceFromMask(
    mask=('[#4 #7804 #0:2 #100 #0 #ea000 #0:7', ' #84000000 #0 #31fa26a2 ]', ), 
    )+\
    mdb.models['Model-1'].rootAssembly.instances['Csection-beam-2'].edges.getSequenceFromMask(
    mask=('[#4 #7804 #0:2 #100 #0 #ea000 #0:7', ' #84000000 #0 #31fa26a2 ]', ), 
    ), faces=
    mdb.models['Model-1'].rootAssembly.instances['Csection-beam-1'].faces.getSequenceFromMask(
    mask=('[#1000 #20000000 #0:4 #80000 #0 #31800000 #4000000 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Csection-beam-2'].faces.getSequenceFromMask(
    mask=('[#1000 #20000000 #0:4 #80000 #0 #31800000 #4000000 ]', ), ), name=
    'p_Set-4', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[63], ), vertices=
    mdb.models['Model-1'].rootAssembly.instances['Csection-beam-1'].vertices.getSequenceFromMask(
    mask=('[#4000000c #70 #0 #30 #1e000 #0:3 #ffc0 ]', ), )+\
    mdb.models['Model-1'].rootAssembly.instances['Csection-beam-2'].vertices.getSequenceFromMask(
    mask=('[#4000000c #70 #0 #30 #1e000 #0:3 #ffc0 ]', ), ))
mdb.models['Model-1'].RigidBody(name='Constraint-2', pinRegion=
    mdb.models['Model-1'].rootAssembly.sets['p_Set-4'], refPointRegion=Region(
    referencePoints=(mdb.models['Model-1'].rootAssembly.referencePoints[63], 
    )))
mdb.models['Model-1'].constraints.changeKey(fromName='Constraint-2', toName=
    'loading-surface')
mdb.models['Model-1'].TabularAmplitude(data=((0.0, 0.0), (0.00625, 2.8), (
    0.0125, 0.0), (0.01875, -2.8), (0.025, 0.0), (0.03125, 2.8), (0.0375, 0.0), 
    (0.04375, -2.8), (0.05, 0.0), (0.05625, 2.8), (0.0625, 0.0), (0.06875, 
    -2.8), (0.075, 0.0), (0.08125, 2.8), (0.0875, 0.0), (0.09375, -2.8), (0.1, 
    0.0), (0.10625, 2.8), (0.1125, 0.0), (0.11875, -2.8), (0.125, 0.0), (
    0.13125, 2.8), (0.1375, 0.0), (0.14375, -2.8), (0.15, 0.0), (0.15625, 
    3.75), (0.1625, 0.0), (0.16875, -3.75), (0.175, 0.0), (0.18125, 3.75), (
    0.1875, 0.0), (0.19375, -3.75), (0.2, 0.0), (0.20625, 3.75), (0.2125, 0.0), 
    (0.21875, -3.75), (0.225, 0.0), (0.23125, 3.75), (0.2375, 0.0), (0.24375, 
    -3.75), (0.25, 0.0), (0.25625, 3.75), (0.2625, 0.0), (0.26875, -3.75), (
    0.275, 0.0), (0.28125, 3.75), (0.2875, 0.0), (0.29375, -3.75), (0.3, 0.0), 
    (0.30625, 5.63), (0.3125, 0.0), (0.31875, -5.63), (0.325, 0.0), (0.33125, 
    5.63), (0.3375, 0.0), (0.34375, -5.63), (0.35, 0.0), (0.35625, 5.63), (
    0.3625, 0.0), (0.36875, -5.63), (0.375, 0.0), (0.38125, 5.63), (0.3875, 
    0.0), (0.39375, -5.63), (0.4, 0.0), (0.40625, 5.63), (0.4125, 0.0), (
    0.41875, -5.63), (0.425, 0.0), (0.43125, 5.63), (0.4375, 0.0), (0.44375, 
    -5.63), (0.45, 0.0), (0.45625, 7.5), (0.4625, 0.0), (0.46875, -7.5), (
    0.475, 0.0), (0.48125, 7.5), (0.4875, 0.0), (0.49375, -7.5), (0.5, 0.0), (
    0.50625, 7.5), (0.5125, 0.0), (0.51875, -7.5), (0.525, 0.0), (0.53125, 
    7.5), (0.5375, 0.0), (0.54375, -7.5), (0.55, 0.0), (0.55625, 11.25), (
    0.5625, 0.0), (0.56875, -11.25), (0.575, 0.0), (0.58125, 11.25), (0.5875, 
    0.0), (0.59375, -11.25), (0.6, 0.0), (0.60625, 15.0), (0.6125, 0.0), (
    0.61875, -15.0), (0.625, 0.0), (0.63125, 15.0), (0.6375, 0.0), (0.64375, 
    -15.0), (0.65, 0.0), (0.65625, 22.5), (0.6625, 0.0), (0.66875, -22.5), (
    0.675, 0.0), (0.68125, 22.5), (0.6875, 0.0), (0.69375, -22.5), (0.7, 0.0), 
    (0.70625, 30.0), (0.7125, 0.0), (0.71875, -30.0), (0.725, 0.0), (0.73125, 
    30.0), (0.7375, 0.0), (0.74375, -30.0), (0.75, 0.0), (0.75625, 37.5), (
    0.7625, 0.0), (0.76875, -37.5), (0.775, 0.0), (0.78125, 37.5), (0.7875, 
    0.0), (0.79375, -37.5), (0.8, 0.0), (0.80625, 45.0), (0.8125, 0.0), (
    0.81875, -45.0), (0.825, 0.0), (0.83125, 45.0), (0.8375, 0.0), (0.84375, 
    -45.0), (0.85, 0.0), (0.85625, 52.5), (0.8625, 0.0), (0.86875, -52.5), (
    0.875, 0.0), (0.88125, 52.5), (0.8875, 0.0), (0.89375, -52.5), (0.9, 0.0), 
    (0.90625, 60.0), (0.9125, 0.0), (0.91875, -60.0), (0.925, 0.0), (0.93125, 
    60.0), (0.9375, 0.0), (0.94375, -60.0), (0.95, 0.0), (0.95625, 67.5), (
    0.9625, 0.0), (0.96875, -67.5), (0.975, 0.0), (0.98125, 67.5), (0.9875, 
    0.0), (0.99375, -67.5), (1.0, 0.0)), name='cyclic', smooth=SOLVER_DEFAULT, 
    timeSpan=STEP)
mdb.models['Model-1'].rootAssembly.Set(name='Set-6', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[63], ))
mdb.models['Model-1'].DisplacementBC(amplitude='cyclic', createStepName=
    'loading step', distributionType=UNIFORM, fieldName='', fixed=OFF, 
    localCsys=None, name='cyclic load', region=
    mdb.models['Model-1'].rootAssembly.sets['Set-6'], u1=0.0, u2=1.0, u3=UNSET, 
    ur1=UNSET, ur2=0.0, ur3=0.0)
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=5.5)
mdb.models['Model-1'].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3f ]', ), ), ))
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=5.0)
mdb.models['Model-1'].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3f ]', ), ), ))
mdb.models['Model-1'].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT), ElemType(
    elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT)), regions=(
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3f ]', ), ), ))
mdb.models['Model-1'].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT), ElemType(
    elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT)), regions=(
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3f ]', ), ), ))
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh(regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3f ]', ), ))
mdb.models['Model-1'].parts['plate'].setMeshControls(elemShape=HEX_DOMINATED, 
    regions=mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3f ]', ), ))
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=3.0)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=7.0)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].Part(name='plate-Copy', objectToCopy=
    mdb.models['Model-1'].parts['plate'])
mdb.models['Model-1'].parts['plate-Copy'].deleteFeatures(('Partition cell-1', 
    'Partition cell-2', 'Partition cell-3', 'Partition cell-4', 
    'Partition cell-5', 'Partition cell-6', 'Partition cell-7', 
    'Partition cell-8', 'Partition cell-9', 'Partition cell-10', 
    'Partition cell-11'))
mdb.models['Model-1'].parts['plate-Copy'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['plate-Copy'].cells.getSequenceFromMask((
    '[#1 ]', ), ), ))
mdb.models['Model-1'].parts['plate-Copy'].generateMesh()
del mdb.models['Model-1'].parts['plate-Copy']
mdb.models['Model-1'].parts['plate'].deleteMesh(regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#1e9eed00 #30 ]', ), ))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#40ec000 ]', ), ), edge=mdb.models['Model-1'].parts['plate'].edges[248], 
    point=mdb.models['Model-1'].parts['plate'].vertices[157])
mdb.models['Model-1'].parts['plate'].deleteMesh(regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#b0116800 #340 ]', ), ))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#30080884 #44 ]', ), ), edge=
    mdb.models['Model-1'].parts['plate'].edges[517], point=
    mdb.models['Model-1'].parts['plate'].vertices[283])
mdb.models['Model-1'].parts['plate'].deleteMesh(regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#c0000000 ]', ), ))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#20880000 #481 ]', ), ), edge=
    mdb.models['Model-1'].parts['plate'].edges[464], point=
    mdb.models['Model-1'].parts['plate'].vertices[235])
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=3.6)
mdb.models['Model-1'].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT), ElemType(
    elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT)), regions=(
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3ffffff ]', ), ), ))
mdb.models['Model-1'].parts['plate'].setMeshControls(elemShape=HEX, regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3ffffff ]', ), ))
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=7.0)
mdb.models['Model-1'].parts['plate'].generateMesh()
del mdb.models['Model-1'].parts['plate'].features['Partition cell-14']
mdb.models['Model-1'].parts['plate'].deleteMesh(regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#c0447c00 #300 ]', ), ))
mdb.models['Model-1'].parts['plate'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#20880000 #481 ]', ), ), edge=
    mdb.models['Model-1'].parts['plate'].edges[245], point=
    mdb.models['Model-1'].parts['plate'].InterestingPoint(
    mdb.models['Model-1'].parts['plate'].edges[245], MIDDLE))
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=5.0)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh(regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3ffffff ]', ), ))
mdb.models['Model-1'].parts['plate'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['plate'].edges.getSequenceFromMask((
    '[#ffffffff:19 #1 ]', ), ), minSizeFactor=0.1, size=5.0)
mdb.models['Model-1'].parts['plate'].setSeedConstraints(constraint=FIXED, 
    edges=mdb.models['Model-1'].parts['plate'].edges.getSequenceFromMask((
    '[#ffffffff:19 #1 ]', ), ))
mdb.models['Model-1'].parts['plate'].seedEdgeByNumber(constraint=FIXED, edges=
    mdb.models['Model-1'].parts['plate'].edges.getSequenceFromMask((
    '[#ffffffff:19 #1 ]', ), ), number=5)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].generateMesh(seedConstraintOverride=ON)
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].deleteSeeds()
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh(regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3ffffff ]', ), ))
mdb.models['Model-1'].parts['plate'].deleteSeeds(regions=
    mdb.models['Model-1'].parts['plate'].edges.getSequenceFromMask((
    '[#ffffffff:19 #1 ]', ), ))
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=3.6)
mdb.models['Model-1'].parts['plate'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD, 
    secondOrderAccuracy=OFF, distortionControl=DEFAULT), ElemType(
    elemCode=C3D4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT)), regions=(
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3ffffff ]', ), ), ))
mdb.models['Model-1'].parts['plate'].setMeshControls(algorithm=MEDIAL_AXIS, 
    elemShape=HEX, regions=
    mdb.models['Model-1'].parts['plate'].cells.getSequenceFromMask((
    '[#ffffffff #3ffffff ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['plate'].deleteMesh()
mdb.models['Model-1'].parts['plate'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=7.0)
mdb.models['Model-1'].parts['plate'].generateMesh()
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#b0008080 #51 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-beam'].edges[329], point=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[329], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#40200000 #c6c ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-beam'].edges[365], point=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[365], MIDDLE))
del mdb.models['Model-1'].parts['Csection-beam'].features['Partition cell-3']
#* Regeneration Failed
del mdb.models['Model-1'].parts['Csection-beam'].features['Partition cell-13']
del mdb.models['Model-1'].parts['Csection-beam'].features['Partition cell-12']
mdb.models['Model-1'].parts['Csection-beam'].deleteFeatures((
    'Partition cell-1', 'Partition cell-2', 'Partition cell-4', 
    'Partition cell-5', 'Partition cell-6', 'Partition cell-7', 
    'Partition cell-8', 'Partition cell-9', 'Partition cell-10', 
    'Partition cell-11'))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#1 ]', ), ), edge=mdb.models['Model-1'].parts['Csection-beam'].edges[29], 
    point=mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[29], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#3 ]', ), ), edge=mdb.models['Model-1'].parts['Csection-beam'].edges[66], 
    point=mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[66], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#3 ]', ), ), edge=mdb.models['Model-1'].parts['Csection-beam'].edges[1], 
    point=mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[1], MIDDLE))
del mdb.models['Model-1'].parts['Csection-beam'].features['Partition cell-3']
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#3 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[113], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[74], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[60], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#a ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[161], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[142], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[84], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#9 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[216], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[40], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[151], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#22 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[82], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[112], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[57], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#5a5 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[75], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[71], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[80], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#33d5b ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[81], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[60], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[58], CENTER))
#* Feature creation failed.
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#32d00 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[153], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[151], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[210], CENTER))
del mdb.models['Model-1'].parts['Csection-beam'].features['Partition cell-1']
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#1000 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[137], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[141], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[118], CENTER))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#c108 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-beam'].edges[354], point=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[354], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#c02100 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-beam'].edges[106], point=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[106], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#3044000 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-beam'].edges[329], point=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[329], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].DatumPlaneByOffset(flip=SIDE2, 
    offset=400.0, plane=
    mdb.models['Model-1'].parts['Csection-beam'].faces[122])
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#3a000000 ]', ), ), datumPlane=
    mdb.models['Model-1'].parts['Csection-beam'].datums[30])
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#78 ]', ), ), edge=mdb.models['Model-1'].parts['Csection-beam'].edges[50]
    , point=mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[50], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#78 ]', ), ), edge=mdb.models['Model-1'].parts['Csection-beam'].edges[92]
    , point=mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[92], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#4380 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-beam'].edges[94], point=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[94], MIDDLE))
mdb.models['Model-1'].parts['Csection-beam'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['Csection-beam'].setElementType(elemTypes=(
    ElemType(elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#ffffffff #ffff ]', ), ), ))
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#ffffffff #ffff ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[298], point2=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[520], MIDDLE), point3=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[297])
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#ff800000 #7fff ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[81], point2=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[82], point3=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[354])
mdb.models['Model-1'].parts['Csection-beam'].setElementType(elemTypes=(
    ElemType(elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#ffffffff:3 ]', ), ), ))
mdb.models['Model-1'].parts['Csection-beam'].generateMesh()
mdb.models['Model-1'].parts['Csection-beam'].deleteMesh()
mdb.models['Model-1'].parts['Csection-beam'].deleteSeeds()
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#7fffff #3fe00000 #243 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[149], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[101], point3=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[164])
mdb.models['Model-1'].parts['Csection-beam'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#0 #f0000000 #ffffffff ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-beam'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-beam'].edges[314], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[195], point3=
    mdb.models['Model-1'].parts['Csection-beam'].vertices[218])
mdb.models['Model-1'].parts['Csection-beam'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['Csection-beam'].setElementType(elemTypes=(
    ElemType(elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#ffffffff:4 #ffff ]', ), ), ))
mdb.models['Model-1'].parts['Csection-beam'].generateMesh()
mdb.models['Model-1'].parts['Csection-beam'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#ffffffff:4 #ffff ]', ), ))
mdb.models['Model-1'].parts['Csection-beam'].setMeshControls(algorithm=
    MEDIAL_AXIS, regions=
    mdb.models['Model-1'].parts['Csection-beam'].cells.getSequenceFromMask((
    '[#ffffffff:4 #ffff ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Csection-beam'].generateMesh()
# Save by User on 2024_06_29-00.54.21; build 2020 2019_09_13-19.49.31 163176
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
del mdb.models['Model-1'].parts['Csection-column'].features['Partition cell-1']
#* Regeneration Failed
mdb.models['Model-1'].parts['Csection-column'].deleteFeatures((
    'Partition cell-2', 'Partition cell-3', 'Partition cell-4', 
    'Partition cell-5', 'Partition cell-6', 'Partition cell-7', 
    'Partition cell-8', 'Partition cell-9', 'Partition cell-10'))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#1 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[15], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[14], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[0], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#2 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[63], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[77], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[81], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#1 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[51], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[66], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[65], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#f ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[159], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[155], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[108], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#96 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[88], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[57], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[182], CENTER))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#924 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[44], CENTER), point2=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[40], CENTER), point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[18], CENTER))
mdb.models['Model-1'].parts['Csection-column'].DatumPlaneByOffset(flip=SIDE2, 
    offset=200.0, plane=
    mdb.models['Model-1'].parts['Csection-column'].faces[25])
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#1822 ]', ), ), datumPlane=
    mdb.models['Model-1'].parts['Csection-column'].datums[21])
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#138 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-column'].edges[26], point=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[26], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#438 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-column'].edges[106], point=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[106], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneNormalToEdge(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#b80 ]', ), ), edge=
    mdb.models['Model-1'].parts['Csection-column'].edges[90], point=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[90], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#ec4916ad ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].vertices[233], point2=
    mdb.models['Model-1'].parts['Csection-column'].vertices[232], point3=
    mdb.models['Model-1'].parts['Csection-column'].vertices[224])
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#bfc0407f #fffe ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[447], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-column'].vertices[108], point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[156], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#c03f807f #1007f ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[83], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-column'].vertices[16], point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[22], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].PartitionCellByPlaneThreePoints(
    cells=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#0 #ff7fbfc0 ]', ), ), point1=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[162], MIDDLE), point2=
    mdb.models['Model-1'].parts['Csection-column'].vertices[80], point3=
    mdb.models['Model-1'].parts['Csection-column'].InterestingPoint(
    mdb.models['Model-1'].parts['Csection-column'].edges[135], MIDDLE))
mdb.models['Model-1'].parts['Csection-column'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=10.0)
mdb.models['Model-1'].parts['Csection-column'].setElementType(elemTypes=(
    ElemType(elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#ffffffff:3 ]', ), ), ))
mdb.models['Model-1'].parts['Csection-column'].setMeshControls(algorithm=
    MEDIAL_AXIS, regions=
    mdb.models['Model-1'].parts['Csection-column'].cells.getSequenceFromMask((
    '[#ffffffff:3 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Csection-column'].generateMesh()
mdb.models['Model-1'].parts['bolt'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#bf8 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['bolt'].datums[7])
#* Feature creation failed.
mdb.models['Model-1'].parts['bolt'].seedPart(deviationFactor=0.1, 
    minSizeFactor=0.1, size=1.3)
mdb.models['Model-1'].parts['bolt'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#fff ]', 
    ), ), ))
mdb.models['Model-1'].parts['bolt'].generateMesh()
mdb.models['Model-1'].parts['bolt'].deleteMesh(regions=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#fff ]', 
    ), ))
mdb.models['Model-1'].parts['bolt'].setMeshControls(algorithm=MEDIAL_AXIS, 
    regions=mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask((
    '[#fff ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['bolt'].generateMesh()
# Save by User on 2024_06_29-01.21.50; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].parts['bolt'].deleteMesh(regions=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#f87 ]', 
    ), ))
mdb.models['Model-1'].parts['bolt'].setMeshControls(elemShape=WEDGE, regions=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#f87 ]', 
    ), ))
mdb.models['Model-1'].parts['bolt'].generateMesh()
mdb.models['Model-1'].parts['bolt'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#fff ]', 
    ), ), ))
mdb.models['Model-1'].parts['bolt'].generateMesh()
mdb.models['Model-1'].parts['bolt'].deleteMesh(regions=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#f87 ]', 
    ), ))
mdb.models['Model-1'].parts['bolt'].setMeshControls(elemShape=HEX, regions=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#fff ]', 
    ), ))
mdb.models['Model-1'].parts['bolt'].generateMesh()
mdb.models['Model-1'].parts['bolt'].DatumPlaneByOffset(flip=SIDE1, offset=0.0, 
    plane=mdb.models['Model-1'].parts['bolt'].faces[28])
mdb.models['Model-1'].parts['bolt'].deleteMesh(regions=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#fff ]', 
    ), ))
mdb.models['Model-1'].parts['bolt'].PartitionCellByDatumPlane(cells=
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#b80 ]', 
    ), ), datumPlane=mdb.models['Model-1'].parts['bolt'].datums[17])
#* Feature creation failed.
del mdb.models['Model-1'].parts['bolt'].features['Datum plane-3']
mdb.models['Model-1'].parts['bolt'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['bolt'].cells.getSequenceFromMask(('[#fff ]', 
    ), ), ))
mdb.models['Model-1'].parts['bolt'].generateMesh()
# Save by User on 2024_06_29-01.27.22; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].rootAssembly.regenerate()
#* FeatureError: Regeneration failed
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 30424, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 2906.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
    'jobName': 'Job-1', 'severe': 1, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Sat Jun 29 01:32:00 2024', 
    'jobName': 'Job-1'})
# Save by User on 2024_06_29-01.32.55; build 2020 2019_09_13-19.49.31 163176
# Save by User on 2024_06_29-01.34.09; build 2020 2019_09_13-19.49.31 163176
# Save by User on 2024_06_29-01.34.29; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Csection-beam'].features['Cut extrude-1'].sketch)
mdb.models['Model-1'].parts['Csection-beam'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Csection-beam'].features['Cut extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Csection-beam'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Csection-beam'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Csection-beam'].features['Solid extrude-1'])
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Csection-beam'].features['Cut extrude-1'].sketch)
mdb.models['Model-1'].parts['Csection-beam'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Csection-beam'].features['Cut extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
# Save by User on 2024_06_29-10.32.06; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['plate'].features['Cut extrude-1'].sketch)
mdb.models['Model-1'].parts['plate'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=mdb.models['Model-1'].parts['plate'].features['Cut extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['plate'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['plate'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['plate'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
# Save by User on 2024_06_29-15.00.46; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Csection-beam'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Csection-beam'].projectReferencesOntoSketch(
    filter=COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Csection-beam'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
# Save by User on 2024_06_29-20.33.23; build 2020 2019_09_13-19.49.31 163176
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
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 33808, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 2906.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
    'jobName': 'Job-1', 'severe': 1, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Fri Jul  5 00:10:18 2024', 
    'jobName': 'Job-1'})
mdb.models['Model-1'].steps['loading step'].setValues(initialInc=40.0, maxInc=
    40.0, minInc=0.0004, timePeriod=40.0)
del mdb.models['Model-1'].amplitudes['cyclic']
mdb.models['Model-1'].TabularAmplitude(data=((0.0, 0.0), (0.25, 2.8), (0.5, 
    0.0), (0.75, -2.8), (1.0, 0.0), (1.25, 2.8), (1.5, 0.0), (1.75, -2.8), (
    2.0, 0.0), (2.25, 2.8), (2.5, 0.0), (2.75, -2.8), (3.0, 0.0), (3.25, 2.8), 
    (3.5, 0.0), (3.75, -2.8), (4.0, 0.0), (4.25, 2.8), (4.5, 0.0), (4.75, 
    -2.8), (5.0, 0.0), (5.25, 2.8), (5.5, 0.0), (5.75, -2.8), (6.0, 0.0), (
    6.25, 3.75), (6.5, 0.0), (6.75, -3.75), (7.0, 0.0), (7.25, 3.75), (7.5, 
    0.0), (7.75, -3.75), (8.0, 0.0), (8.25, 3.75), (8.5, 0.0), (8.75, -3.75), (
    9.0, 0.0), (9.25, 3.75), (9.5, 0.0), (9.75, -3.75), (10.0, 0.0), (10.25, 
    3.75), (10.5, 0.0), (10.75, -3.75), (11.0, 0.0), (11.25, 3.75), (11.5, 
    0.0), (11.75, -3.75), (12.0, 0.0), (12.25, 5.63), (12.5, 0.0), (12.75, 
    -5.63), (13.0, 0.0), (13.25, 5.63), (13.5, 0.0), (13.75, -5.63), (14.0, 
    0.0), (14.25, 5.63), (14.5, 0.0), (14.75, -5.63), (15.0, 0.0), (15.25, 
    5.63), (15.5, 0.0), (15.75, -5.63), (16.0, 0.0), (16.25, 5.63), (16.5, 
    0.0), (16.75, -5.63), (17.0, 0.0), (17.25, 5.63), (17.5, 0.0), (17.75, 
    -5.63), (18.0, 0.0), (18.25, 7.5), (18.5, 0.0), (18.75, -7.5), (19.0, 0.0), 
    (19.25, 7.5), (19.5, 0.0), (19.75, -7.5), (20.0, 0.0), (20.25, 7.5), (20.5, 
    0.0), (20.75, -7.5), (21.0, 0.0), (21.25, 7.5), (21.5, 0.0), (21.75, -7.5), 
    (22.0, 0.0), (22.25, 11.25), (22.5, 0.0), (22.75, -11.25), (23.0, 0.0), (
    23.25, 11.25), (23.5, 0.0), (23.75, -11.25), (24.0, 0.0), (24.25, 15.0), (
    24.5, 0.0), (24.75, -15.0), (25.0, 0.0), (25.25, 15.0), (25.5, 0.0), (
    25.75, -15.0), (26.0, 0.0), (26.25, 22.5), (26.5, 0.0), (26.75, -22.5), (
    27.0, 0.0), (27.25, 22.5), (27.5, 0.0), (27.75, -22.5), (28.0, 0.0), (
    28.25, 30.0), (28.5, 0.0), (28.75, -30.0), (29.0, 0.0), (29.25, 30.0), (
    29.5, 0.0), (29.75, -30.0), (30.0, 0.0), (30.25, 37.5), (30.5, 0.0), (
    30.75, -37.5), (31.0, 0.0), (31.25, 37.5), (31.5, 0.0), (31.75, -37.5), (
    32.0, 0.0), (32.25, 45.0), (32.5, 0.0), (32.75, -45.0), (33.0, 0.0), (
    33.25, 45.0), (33.5, 0.0), (33.75, -45.0), (34.0, 0.0), (34.25, 52.5), (
    34.5, 0.0), (34.75, -52.5), (35.0, 0.0), (35.25, 52.5), (35.5, 0.0), (
    35.75, -52.5), (36.0, 0.0), (36.25, 60.0), (36.5, 0.0), (36.75, -60.0), (
    37.0, 0.0), (37.25, 60.0), (37.5, 0.0), (37.75, -60.0), (38.0, 0.0), (
    38.25, 67.5), (38.5, 0.0), (38.75, -67.5), (39.0, 0.0), (39.25, 67.5), (
    39.5, 0.0), (39.75, -67.5), (40.0, 0.0)), name='cyclic load', smooth=
    SOLVER_DEFAULT, timeSpan=STEP)
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(amplitude=
    'cyclic load')
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 32384, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 2906.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 40.0, 'attempts': 1, 
    'timeIncrement': 40.0, 'increment': 1, 'stepTime': 40.0, 'step': 1, 
    'jobName': 'Job-1', 'severe': 1, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Fri Jul  5 15:21:38 2024', 
    'jobName': 'Job-1'})
mdb.models['Model-1'].steps['loading step'].setValues(nlgeom=ON)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 31152, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 2906.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 40.0, 'attempts': 1, 
    'timeIncrement': 40.0, 'increment': 1, 'stepTime': 40.0, 'step': 1, 
    'jobName': 'Job-1', 'severe': 1, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Fri Jul  5 15:25:21 2024', 
    'jobName': 'Job-1'})
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(u1=UNSET, 
    ur2=UNSET, ur3=UNSET)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 5008, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 2906.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 40.0, 'attempts': 1, 
    'timeIncrement': 40.0, 'increment': 1, 'stepTime': 40.0, 'step': 1, 
    'jobName': 'Job-1', 'severe': 1, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Fri Jul  5 15:37:25 2024', 
    'jobName': 'Job-1'})
mdb.models['Model-1'].steps['loading step'].setValues(initialInc=0.25, 
    maxNumInc=1000)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 6532, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 2875.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 1U', 
    'timeIncrement': 0.25, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-1', 'severe': 16, 'iterations': 16, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['Job-1']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Process terminated by external request (SIGTERM or SIGINT received).', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(INTERRUPTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis interrupted by external signal', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-1'})
mdb.Model(name='Model-1-linear', objectToCopy=mdb.models['Model-1'])
del mdb.models['Model-1-linear'].steps['loading step']
mdb.models['Model-1-linear'].StaticStep(name='Step-1', previous='Initial')
mdb.models['Model-1-linear'].rootAssembly.Set(name='Set-7', referencePoints=(
    mdb.models['Model-1-linear'].rootAssembly.referencePoints[63], ))
mdb.models['Model-1-linear'].DisplacementBC(amplitude='cyclic load', 
    createStepName='Step-1', distributionType=UNIFORM, fieldName='', fixed=OFF, 
    localCsys=None, name='BC-2', region=
    mdb.models['Model-1-linear'].rootAssembly.sets['Set-7'], u1=UNSET, u2=1.0, 
    u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET)
mdb.models['Model-1-linear'].steps['Step-1'].setValues(initialInc=0.25, maxInc=
    40.0, minInc=0.0004, timePeriod=40.0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Process terminated by external request (SIGTERM or SIGINT received).', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(INTERRUPTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis interrupted by external signal', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'Job-1'})
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1-linear', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job-2', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
    ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-2.odb', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 33084, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-2', 'memory': 3037.0})
mdb.jobs['Job-2']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MINIMUM_MEMORY, {'minimum_memory': 391.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 1U', 
    'timeIncrement': 0.25, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 27, 'iterations': 27, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['Job-2']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Process terminated by external request (SIGTERM or SIGINT received).', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(INTERRUPTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis interrupted by external signal', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
mdb.models['Model-1-linear'].boundaryConditions['BC-2'].setValues(amplitude=
    UNSET, u2=60.0)
mdb.models['Model-1-linear'].steps['Step-1'].setValues(initialInc=0.01, maxInc=
    1.0, maxNumInc=10000, minInc=1e-05, timePeriod=1.0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-2.odb', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 33036, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-2', 'memory': 3037.0})
mdb.jobs['Job-2']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MINIMUM_MEMORY, {'minimum_memory': 391.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-3.160 D.O.F. 3 ratio = 4.76154E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 1U', 
    'timeIncrement': 0.01, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 17, 'iterations': 17, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-3.165 D.O.F. 2 ratio = 4.52041E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-3.165 D.O.F. 3 ratio = 5.06969E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 2U', 
    'timeIncrement': 0.0025, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 10, 'iterations': 10, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-2.163 D.O.F. 2 ratio = 9.10823E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-2.163 D.O.F. 3 ratio = 11.7787E+09 .', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-2.164 D.O.F. 3 ratio = 4.98312E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 3U', 
    'timeIncrement': 0.000625, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 7, 'iterations': 7, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 4U', 
    'timeIncrement': 0.00015625, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-3.161 D.O.F. 2 ratio = 64.5281E+09 .', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-3.161 D.O.F. 3 ratio = 27.6587E+09 .', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-2.164 D.O.F. 2 ratio = 5.83674E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-2.164 D.O.F. 3 ratio = 7.56936E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Solver problem. Numerical singularity when processing node BOLT-1-LIN-1-2-1-LIN-4-3.164 D.O.F. 3 ratio = 5.32709E+09.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 5U', 
    'timeIncrement': 3.90625e-05, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'Job-2', 'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-2']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Too many attempts made for this increment', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
mdb.models['Model-1-linear'].steps['Step-1'].setValues(initialInc=1.0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-2.odb', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 28836, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-2', 'memory': 2906.0})
mdb.jobs['Job-2']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 52 POINTS', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 44 negative eigenvalues.', 
    'jobName': 'Job-2'})
mdb.models['Model-1-linear'].boundaryConditions['BC-2'].setValues(u1=0.0, u2=
    -60.0, ur2=0.0, ur3=0.0)
mdb.jobs['Job-2']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Process terminated by external request (SIGTERM or SIGINT received).', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(INTERRUPTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis interrupted by external signal', 'jobName': 'Job-2'})
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
mdb.jobs['Job-2']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-2'})
del mdb.models['Model-1-linear']
del mdb.jobs['Job-2']
mdb.models['Model-1'].steps['loading step'].setValues(nlgeom=OFF)
mdb.models['Model-1'].steps['loading step'].setValues(initialInc=40.0)
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(u1=0.0, ur2=
    0.0, ur3=0.0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 32552, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 2906.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STATUS, {'totalTime': 40.0, 'attempts': 1, 
    'timeIncrement': 40.0, 'increment': 1, 'stepTime': 40.0, 'step': 1, 
    'jobName': 'Job-1', 'severe': 1, 'iterations': 1, 'phase': STANDARD_PHASE, 
    'equilibrium': 0})
mdb.jobs['Job-1']._Message(END_STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_COMPLETED, {'time': 'Fri Jul  5 16:52:44 2024', 
    'jobName': 'Job-1'})
mdb.models['Model-1'].steps['loading step'].setValues(initialInc=0.1, 
    maxNumInc=10000)
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(amplitude=
    UNSET, u2=-60.0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
mdb.jobs['Job-1']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\Job-1.odb', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 35304, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'Job-1', 'memory': 3037.0})
mdb.jobs['Job-1']._Message(PHYSICAL_MEMORY, {'phase': STANDARD_PHASE, 
    'physical_memory': 16104.0, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(MINIMUM_MEMORY, {'minimum_memory': 391.0, 
    'phase': STANDARD_PHASE, 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Process terminated by external request (SIGTERM or SIGINT received).', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(INTERRUPTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis interrupted by external signal', 'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-1'})
mdb.jobs['Job-1']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'Job-1'})
# Save by User on 2024_07_05-17.04.29; build 2020 2019_09_13-19.49.31 163176
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
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(amplitude=
    'cyclic load', u2=50.0)
mdb.models['Model-1'].TabularAmplitude(data=((0.0, 0.0), (0.25, 0.5), (0.5, 
    -0.5), (0.75, 1.0), (0.9, -1.0), (1.0, 0.0)), name='cyclic-test', smooth=
    SOLVER_DEFAULT, timeSpan=STEP)
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(amplitude=
    'cyclic-test')
mdb.models['Model-1'].steps['loading step'].setValues(initialInc=0.001, maxInc=
    0.1, maxNumInc=1000, minInc=1e-05, nlgeom=ON, timePeriod=1.0)


mdb.models['Model-1'].ImplicitDynamicsStep(alpha=DEFAULT, amplitude=RAMP, 
    application=QUASI_STATIC, initialConditions=OFF, initialInc=0.1, 
    maintainAttributes=True, maxNumInc=10000, minInc=1e-15, name='loading step'
    , nlgeom=ON, nohaf=OFF, previous='Initial', timePeriod=40.0)
mdb.models['Model-1'].rootAssembly.Set(name='loading-set', referencePoints=(
    mdb.models['Model-1'].rootAssembly.referencePoints[63], ))
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(rebar=
    EXCLUDE, region=mdb.models['Model-1'].rootAssembly.sets['loading-set'], 
    sectionPoints=DEFAULT, variables=('U2', 'RF2'))
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(amplitude=
    'cyclic load')
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='dynamic-implicit', nodalOutputPrecision=
    SINGLE, numCpus=4, numDomains=4, numGPUs=1, queue=None, resultsFormat=ODB, 
    scratch='', type=ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['dynamic-implicit'].submit(consistencyChecking=OFF)
mdb.jobs['dynamic-implicit']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IN THIS TYPE OF ANALYSIS ONE WOULD NORMALLY EXPECT THAT A DENSITY FOR MATERIAL STEEL WOULD BE DEFINED.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IN THIS TYPE OF ANALYSIS ONE WOULD NORMALLY EXPECT THAT A DENSITY FOR MATERIAL STEEL-BOLT WOULD BE DEFINED.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'IT IS NECESSARY TO DEFINE A MATERIAL DENSITY OR LUMPED MASS OR INPUT THE MASS MATRIX FOR A PART OF THE MODEL USING THE MATRIX INPUT CAPABILITY FOR DYNAMIC ANALYSIS OR FOR GRAVITY LOADS.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\dynamic-implicit.odb', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'dynamic-implicit'})
mdb.models['Model-1'].materials['steel'].Density(table=((7850.0, ), ))
mdb.models['Model-1'].materials['steel-bolt'].Density(table=((7850.0, ), ))
mdb.jobs['dynamic-implicit'].submit(consistencyChecking=OFF)
mdb.jobs['dynamic-implicit']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\dynamic-implicit.odb', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 33832, 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 0, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'dynamic-implicit', 'memory': 2997.0})
mdb.jobs['dynamic-implicit']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 16104.0, 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 21 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 14 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 2.50000E-02', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0, 
    'attempts': ' 1U', 'timeIncrement': 0.1, 'increment': 1, 'stepTime': 0.0, 
    'step': 1, 'jobName': 'dynamic-implicit', 'severe': 0, 'iterations': 1, 
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 26 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 6.25000E-03', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0, 
    'attempts': ' 2U', 'timeIncrement': 0.025, 'increment': 1, 'stepTime': 0.0, 
    'step': 1, 'jobName': 'dynamic-implicit', 'severe': 0, 'iterations': 1, 
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.00625, 
    'attempts': 3, 'timeIncrement': 0.00625, 'increment': 1, 
    'stepTime': 0.00625, 'step': 1, 'jobName': 'dynamic-implicit', 'severe': 3, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 1, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0125, 
    'attempts': 1, 'timeIncrement': 0.00625, 'increment': 2, 
    'stepTime': 0.0125, 'step': 1, 'jobName': 'dynamic-implicit', 'severe': 2, 
    'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 2, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 17 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 2.34375E-03', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0125, 
    'attempts': ' 1U', 'timeIncrement': 0.009375, 'increment': 3, 
    'stepTime': 0.0125, 'step': 1, 'jobName': 'dynamic-implicit', 'severe': 0, 
    'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.01484375, 
    'attempts': 2, 'timeIncrement': 0.00234375, 'increment': 3, 
    'stepTime': 0.01484375, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 3, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 8.78906E-04', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.01484375, 
    'attempts': ' 1U', 'timeIncrement': 0.003515625, 'increment': 4, 
    'stepTime': 0.01484375, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.01572265625, 
    'attempts': 2, 'timeIncrement': 0.00087890625, 'increment': 4, 
    'stepTime': 0.01572265625, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 4, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.017041015625, 
    'attempts': 1, 'timeIncrement': 0.001318359375, 'increment': 5, 
    'stepTime': 0.017041015625, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 5, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 4.94385E-04', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.017041015625, 
    'attempts': ' 1U', 'timeIncrement': 0.0019775390625, 'increment': 6, 
    'stepTime': 0.017041015625, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.017535400390625, 
    'attempts': 2, 'timeIncrement': 0.000494384765625, 'increment': 6, 
    'stepTime': 0.017535400390625, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 6, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 1.85394E-04', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.017535400390625, 
    'attempts': ' 1U', 'timeIncrement': 0.0007415771484375, 'increment': 7, 
    'stepTime': 0.017535400390625, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0177207946777344, 
    'attempts': 2, 'timeIncrement': 0.000185394287109375, 'increment': 7, 
    'stepTime': 0.0177207946777344, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 7, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 6.95229E-05', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0177207946777344, 
    'attempts': ' 1U', 'timeIncrement': 0.000278091430664063, 'increment': 8, 
    'stepTime': 0.0177207946777344, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0177903175354004, 
    'attempts': 2, 'timeIncrement': 6.95228576660156e-05, 'increment': 8, 
    'stepTime': 0.0177903175354004, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 8, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 2.60711E-05', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0177903175354004, 
    'attempts': ' 1U', 'timeIncrement': 0.000104284286499023, 'increment': 9, 
    'stepTime': 0.0177903175354004, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178163886070252, 
    'attempts': 2, 'timeIncrement': 2.60710716247559e-05, 'increment': 9, 
    'stepTime': 0.0178163886070252, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 9, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 9.77665E-06', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178163886070252, 
    'attempts': ' 1U', 'timeIncrement': 3.91066074371338e-05, 'increment': 10, 
    'stepTime': 0.0178163886070252, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178261652588844, 
    'attempts': 2, 'timeIncrement': 9.77665185928345e-06, 'increment': 10, 
    'stepTime': 0.0178261652588844, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 10, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178408302366734, 
    'attempts': 1, 'timeIncrement': 1.46649777889252e-05, 'increment': 11, 
    'stepTime': 0.0178408302366734, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 11, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 5.49937E-06', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178408302366734, 
    'attempts': ' 1U', 'timeIncrement': 2.19974666833878e-05, 'increment': 12, 
    'stepTime': 0.0178408302366734, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178463296033442, 
    'attempts': 2, 'timeIncrement': 5.49936667084694e-06, 'increment': 12, 
    'stepTime': 0.0178463296033442, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 1, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 12, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178545786533505, 
    'attempts': 1, 'timeIncrement': 8.24905000627041e-06, 'increment': 13, 
    'stepTime': 0.0178545786533505, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 13, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 3.09339E-06', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178545786533505, 
    'attempts': ' 1U', 'timeIncrement': 1.23735750094056e-05, 'increment': 14, 
    'stepTime': 0.0178545786533505, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178576720471028, 
    'attempts': 2, 'timeIncrement': 3.0933937523514e-06, 'increment': 14, 
    'stepTime': 0.0178576720471028, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 14, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 2 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 1.16002E-06', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178576720471028, 
    'attempts': ' 1U', 'timeIncrement': 4.64009062852711e-06, 'increment': 15, 
    'stepTime': 0.0178576720471028, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.01785883206976, 
    'attempts': 2, 'timeIncrement': 1.16002265713178e-06, 'increment': 15, 
    'stepTime': 0.01785883206976, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 15, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178605721037457, 
    'attempts': 1, 'timeIncrement': 1.74003398569766e-06, 'increment': 16, 
    'stepTime': 0.0178605721037457, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 16, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 6.52513E-07', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178605721037457, 
    'attempts': ' 1U', 'timeIncrement': 2.6100509785465e-06, 'increment': 17, 
    'stepTime': 0.0178605721037457, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178612246164903, 
    'attempts': 2, 'timeIncrement': 6.52512744636624e-07, 'increment': 17, 
    'stepTime': 0.0178612246164903, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 17, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178622033856073, 
    'attempts': 1, 'timeIncrement': 9.78769116954936e-07, 'increment': 18, 
    'stepTime': 0.0178622033856073, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 18, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 3.67038E-07', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178622033856073, 
    'attempts': ' 1U', 'timeIncrement': 1.4681536754324e-06, 'increment': 19, 
    'stepTime': 0.0178622033856073, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178625704240261, 
    'attempts': 2, 'timeIncrement': 3.67038418858101e-07, 'increment': 19, 
    'stepTime': 0.0178625704240261, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 19, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178631209816544, 
    'attempts': 1, 'timeIncrement': 5.50557628287152e-07, 'increment': 20, 
    'stepTime': 0.0178631209816544, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 20, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 2.06459E-07', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178631209816544, 
    'attempts': ' 1U', 'timeIncrement': 8.25836442430728e-07, 'increment': 21, 
    'stepTime': 0.0178631209816544, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 2 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 5.16148E-08', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178631209816544, 
    'attempts': ' 2U', 'timeIncrement': 2.06459110607682e-07, 'increment': 21, 
    'stepTime': 0.0178631209816544, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 4 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178631209816544, 
    'attempts': ' 3U', 'timeIncrement': 5.16147776519205e-08, 'increment': 21, 
    'stepTime': 0.0178631209816544, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.0178631209816544, 
    'attempts': ' 4U', 'timeIncrement': 1.29036944129801e-08, 'increment': 21, 
    'stepTime': 0.0178631209816544, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.models['Model-1'].boundaryConditions['cyclic load'].setValues(u2=1.0)
mdb.jobs['dynamic-implicit']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Process terminated by external request (SIGTERM or SIGINT received).', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(INTERRUPTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis interrupted by external signal', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit'].submit(consistencyChecking=OFF)
mdb.jobs['dynamic-implicit']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 0, 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'THE RATIO OF THE MAXIMUM INCREMENTAL ADJUSTMENT TO THE AVERAGE CHARACTERISTIC LENGTH IS 1.58419E-02 AT NODE 43 INSTANCE BOLT-1 ON THE SURFACE PAIR (General_Contact_Faces,General_Contact_Faces). MAGNITUDES OF STRAIN-FREE NODAL POSITION ADJUSTMENTS CAN BE OBSERVED IN CONTOUR PLOTS AND SYMBOL PLOTS OF THE "STRAINFREE" OUTPUT VARIABLE AT TIME=0.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '21 nodes have been adjusted. The nodes have been identified in node set WarnNodeAdjust.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': 'C:\\Users\\User\\Desktop\\Abaqus\\dynamic-implicit.odb', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'DESKTOP-423DLGJ', 'handle': 5368, 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 0, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(MEMORY_ESTIMATE, {
    'phase': STANDARD_PHASE, 'jobName': 'dynamic-implicit', 'memory': 2997.0})
mdb.jobs['dynamic-implicit']._Message(PHYSICAL_MEMORY, {
    'phase': STANDARD_PHASE, 'physical_memory': 16104.0, 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(MINIMUM_MEMORY, {'minimum_memory': 388.0, 
    'phase': STANDARD_PHASE, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.1, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 1, 'stepTime': 0.1, 'step': 1, 
    'jobName': 'dynamic-implicit', 'severe': 3, 'iterations': 3, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 1, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.2, 'attempts': 1, 
    'timeIncrement': 0.1, 'increment': 2, 'stepTime': 0.2, 'step': 1, 
    'jobName': 'dynamic-implicit', 'severe': 3, 'iterations': 3, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 2, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.35, 
    'attempts': 1, 'timeIncrement': 0.15, 'increment': 3, 'stepTime': 0.35, 
    'step': 1, 'jobName': 'dynamic-implicit', 'severe': 3, 'iterations': 3, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 3, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.575, 
    'attempts': 1, 'timeIncrement': 0.225, 'increment': 4, 'stepTime': 0.575, 
    'step': 1, 'jobName': 'dynamic-implicit', 'severe': 3, 'iterations': 3, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 4, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 0.9125, 
    'attempts': 1, 'timeIncrement': 0.3375, 'increment': 5, 'stepTime': 0.9125, 
    'step': 1, 'jobName': 'dynamic-implicit', 'severe': 4, 'iterations': 4, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 5, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 1.41875, 
    'attempts': 1, 'timeIncrement': 0.50625, 'increment': 6, 
    'stepTime': 1.41875, 'step': 1, 'jobName': 'dynamic-implicit', 'severe': 4, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 6, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 2.178125, 
    'attempts': 1, 'timeIncrement': 0.759375, 'increment': 7, 
    'stepTime': 2.178125, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 7, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 18 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 18 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 18 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 3.3171875, 
    'attempts': 1, 'timeIncrement': 1.1390625, 'increment': 8, 
    'stepTime': 3.3171875, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 8, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 5.02578125, 
    'attempts': 1, 'timeIncrement': 1.70859375, 'increment': 9, 
    'stepTime': 5.02578125, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 9, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 5.02578125, 
    'attempts': ' 1U', 'timeIncrement': 2.562890625, 'increment': 10, 
    'stepTime': 5.02578125, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 34, 'iterations': 34, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 5.66650390625, 
    'attempts': 2, 'timeIncrement': 0.64072265625, 'increment': 10, 
    'stepTime': 5.66650390625, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 10, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 6.627587890625, 
    'attempts': 1, 'timeIncrement': 0.961083984375, 'increment': 11, 
    'stepTime': 6.627587890625, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 11, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 22 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 18 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 18 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 18 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 8.0692138671875, 
    'attempts': 1, 'timeIncrement': 1.4416259765625, 'increment': 12, 
    'stepTime': 8.0692138671875, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 12, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 10.2316528320313, 
    'attempts': 1, 'timeIncrement': 2.16243896484375, 'increment': 13, 
    'stepTime': 10.2316528320313, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 13, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 36 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 35 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 3 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 14 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 0.81091', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 10.2316528320313, 
    'attempts': ' 1U', 'timeIncrement': 3.24365844726563, 'increment': 14, 
    'stepTime': 10.2316528320313, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 1, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 24 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 11.0425674438477, 
    'attempts': 2, 'timeIncrement': 0.810914611816406, 'increment': 14, 
    'stepTime': 11.0425674438477, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 14, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 38 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 12.2589393615723, 
    'attempts': 1, 'timeIncrement': 1.21637191772461, 'increment': 15, 
    'stepTime': 12.2589393615723, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 15, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 34 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 14.0834972381592, 
    'attempts': 1, 'timeIncrement': 1.82455787658691, 'increment': 16, 
    'stepTime': 14.0834972381592, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 8, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 16, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 36 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 16.8203340530396, 
    'attempts': 1, 'timeIncrement': 2.73683681488037, 'increment': 17, 
    'stepTime': 16.8203340530396, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 17, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 36 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 36 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 12 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 6 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 6 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 6 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 6 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 6 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 16.8203340530396, 
    'attempts': ' 1U', 'timeIncrement': 4.10525522232056, 'increment': 18, 
    'stepTime': 16.8203340530396, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 8, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 17.8466478586197, 
    'attempts': 2, 'timeIncrement': 1.02631380558014, 'increment': 18, 
    'stepTime': 17.8466478586197, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 18, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 10 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 19.3861185669899, 
    'attempts': 1, 'timeIncrement': 1.53947070837021, 'increment': 19, 
    'stepTime': 19.3861185669899, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 19, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 50 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 56 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 29 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 1 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 12 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 0.57730', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 19.3861185669899, 
    'attempts': ' 1U', 'timeIncrement': 2.30920606255531, 'increment': 20, 
    'stepTime': 19.3861185669899, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 1, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 6 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 19.9634200826287, 
    'attempts': 2, 'timeIncrement': 0.577301515638828, 'increment': 20, 
    'stepTime': 19.9634200826287, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 20, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 32 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 30 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 30 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 30 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 20.829372356087, 
    'attempts': 1, 'timeIncrement': 0.865952273458243, 'increment': 21, 
    'stepTime': 20.829372356087, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 21, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 29 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT IS SO LARGE THAT THE PROGRAM WILL NOT ATTEMPT THE PLASTICITY CALCULATION AT 5 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 18 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 0.32473', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 20.829372356087, 
    'attempts': ' 1U', 'timeIncrement': 1.29892841018736, 'increment': 22, 
    'stepTime': 20.829372356087, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 1, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 21.1541044586338, 
    'attempts': 2, 'timeIncrement': 0.324732102546841, 'increment': 22, 
    'stepTime': 21.1541044586338, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 22, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 21.6412026124541, 
    'attempts': 1, 'timeIncrement': 0.487098153820261, 'increment': 23, 
    'stepTime': 21.6412026124541, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 23, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 22.3718498431845, 
    'attempts': 1, 'timeIncrement': 0.730647230730392, 'increment': 24, 
    'stepTime': 22.3718498431845, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 24, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 36 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 23.4678206892801, 
    'attempts': 1, 'timeIncrement': 1.09597084609559, 'increment': 25, 
    'stepTime': 23.4678206892801, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 25, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 30 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 30 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 30 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 30 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 25.1117769584234, 
    'attempts': 1, 'timeIncrement': 1.64395626914338, 'increment': 26, 
    'stepTime': 25.1117769584234, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 26, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 0.61648', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 25.1117769584234, 
    'attempts': ' 1U', 'timeIncrement': 2.46593440371507, 'increment': 27, 
    'stepTime': 25.1117769584234, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 2 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 41 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 42 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 25.1117769584234, 
    'attempts': ' 2U', 'timeIncrement': 0.616483600928768, 'increment': 27, 
    'stepTime': 25.1117769584234, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 10, 'iterations': 10, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 25.2658978586556, 
    'attempts': 3, 'timeIncrement': 0.154120900232192, 'increment': 27, 
    'stepTime': 25.2658978586556, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 27, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 41 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 44 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 25.4970792090039, 
    'attempts': 1, 'timeIncrement': 0.231181350348288, 'increment': 28, 
    'stepTime': 25.4970792090039, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 6, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 28, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 25.8438512345263, 
    'attempts': 1, 'timeIncrement': 0.346772025522432, 'increment': 29, 
    'stepTime': 25.8438512345263, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 29, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 26.36400927281, 
    'attempts': 1, 'timeIncrement': 0.520158038283648, 'increment': 30, 
    'stepTime': 26.36400927281, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 7, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 30, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 38 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 15 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 16 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 13 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 1 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 20 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The system matrix has 6 negative eigenvalues.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 28 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'CONVERGENCE JUDGED UNLIKELY.  INCREMENT WILL BE ATTEMPTED AGAIN WITH A TIME INCREMENT OF 0.19506', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 26.36400927281, 
    'attempts': ' 1U', 'timeIncrement': 0.780237057425472, 'increment': 31, 
    'stepTime': 26.36400927281, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'THE STRAIN INCREMENT HAS EXCEEDED FIFTY TIMES THE STRAIN TO CAUSE FIRST YIELD AT 40 POINTS', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'Warning message limit reached. No further warning messages will be reported.\nPlease see the dat file for more warnings.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 26.5590685371664, 
    'attempts': 2, 'timeIncrement': 0.195059264356368, 'increment': 31, 
    'stepTime': 26.5590685371664, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 31, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 26.8516574337009, 
    'attempts': 1, 'timeIncrement': 0.292588896534552, 'increment': 32, 
    'stepTime': 26.8516574337009, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 32, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.2905407785027, 
    'attempts': 1, 'timeIncrement': 0.438883344801828, 'increment': 33, 
    'stepTime': 27.2905407785027, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 7, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 33, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.2905407785027, 
    'attempts': ' 1U', 'timeIncrement': 0.658325017202742, 'increment': 34, 
    'stepTime': 27.2905407785027, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.4551220328034, 
    'attempts': 2, 'timeIncrement': 0.164581254300686, 'increment': 34, 
    'stepTime': 27.4551220328034, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 34, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.4551220328034, 
    'attempts': ' 1U', 'timeIncrement': 0.246871881451028, 'increment': 35, 
    'stepTime': 27.4551220328034, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 7, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.5168400031662, 
    'attempts': 2, 'timeIncrement': 0.0617179703627571, 'increment': 35, 
    'stepTime': 27.5168400031662, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 35, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.6094169587103, 
    'attempts': 1, 'timeIncrement': 0.0925769555441356, 'increment': 36, 
    'stepTime': 27.6094169587103, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 36, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.7482823920265, 
    'attempts': 1, 'timeIncrement': 0.138865433316203, 'increment': 37, 
    'stepTime': 27.7482823920265, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 37, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 27.9565805420008, 
    'attempts': 1, 'timeIncrement': 0.208298149974305, 'increment': 38, 
    'stepTime': 27.9565805420008, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 38, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 28.2690277669623, 
    'attempts': 1, 'timeIncrement': 0.312447224961458, 'increment': 39, 
    'stepTime': 28.2690277669623, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 7, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 39, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 28.2690277669623, 
    'attempts': ' 1U', 'timeIncrement': 0.468670837442187, 'increment': 40, 
    'stepTime': 28.2690277669623, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 28.3861954763228, 
    'attempts': 2, 'timeIncrement': 0.117167709360547, 'increment': 40, 
    'stepTime': 28.3861954763228, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 40, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 28.5619470403637, 
    'attempts': 1, 'timeIncrement': 0.17575156404082, 'increment': 41, 
    'stepTime': 28.5619470403637, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 41, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 28.8255743864249, 
    'attempts': 1, 'timeIncrement': 0.26362734606123, 'increment': 42, 
    'stepTime': 28.8255743864249, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 8, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 42, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 28.8255743864249, 
    'attempts': ' 1U', 'timeIncrement': 0.395441019091845, 'increment': 43, 
    'stepTime': 28.8255743864249, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 7, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 28.9244346411978, 
    'attempts': 2, 'timeIncrement': 0.0988602547729612, 'increment': 43, 
    'stepTime': 28.9244346411978, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 43, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.0727250233573, 
    'attempts': 1, 'timeIncrement': 0.148290382159442, 'increment': 44, 
    'stepTime': 29.0727250233573, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 44, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.0727250233573, 
    'attempts': ' 1U', 'timeIncrement': 0.222435573239163, 'increment': 45, 
    'stepTime': 29.0727250233573, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 11, 'iterations': 11, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.1283339166671, 
    'attempts': 2, 'timeIncrement': 0.0556088933097907, 'increment': 45, 
    'stepTime': 29.1283339166671, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 45, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.2117472566318, 
    'attempts': 1, 'timeIncrement': 0.083413339964686, 'increment': 46, 
    'stepTime': 29.2117472566318, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 46, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.3368672665788, 
    'attempts': 1, 'timeIncrement': 0.125120009947029, 'increment': 47, 
    'stepTime': 29.3368672665788, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 47, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.5245472814993, 
    'attempts': 1, 'timeIncrement': 0.187680014920544, 'increment': 48, 
    'stepTime': 29.5245472814993, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 6, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 48, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.8060673038802, 
    'attempts': 1, 'timeIncrement': 0.281520022380815, 'increment': 49, 
    'stepTime': 29.8060673038802, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 49, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.8060673038802, 
    'attempts': ' 1U', 'timeIncrement': 0.422280033571223, 'increment': 50, 
    'stepTime': 29.8060673038802, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 29.911637312273, 
    'attempts': 2, 'timeIncrement': 0.105570008392806, 'increment': 50, 
    'stepTime': 29.911637312273, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 50, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.0699923248622, 
    'attempts': 1, 'timeIncrement': 0.158355012589209, 'increment': 51, 
    'stepTime': 30.0699923248622, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 51, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.0699923248622, 
    'attempts': ' 1U', 'timeIncrement': 0.237532518883813, 'increment': 52, 
    'stepTime': 30.0699923248622, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 9, 'iterations': 9, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.1293754545831, 
    'attempts': 2, 'timeIncrement': 0.0593831297209532, 'increment': 52, 
    'stepTime': 30.1293754545831, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 52, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.2184501491645, 
    'attempts': 1, 'timeIncrement': 0.0890746945814299, 'increment': 53, 
    'stepTime': 30.2184501491645, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 6, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 53, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.3520621910367, 
    'attempts': 1, 'timeIncrement': 0.133612041872145, 'increment': 54, 
    'stepTime': 30.3520621910367, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 54, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.5524802538449, 
    'attempts': 1, 'timeIncrement': 0.200418062808217, 'increment': 55, 
    'stepTime': 30.5524802538449, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 55, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.8531073480572, 
    'attempts': 1, 'timeIncrement': 0.300627094212326, 'increment': 56, 
    'stepTime': 30.8531073480572, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 56, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.8531073480572, 
    'attempts': ' 1U', 'timeIncrement': 0.450940641318489, 'increment': 57, 
    'stepTime': 30.8531073480572, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 30.9658425083869, 
    'attempts': 2, 'timeIncrement': 0.112735160329622, 'increment': 57, 
    'stepTime': 30.9658425083869, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 57, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.1349452488813, 
    'attempts': 1, 'timeIncrement': 0.169102740494433, 'increment': 58, 
    'stepTime': 31.1349452488813, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 58, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.3885993596229, 
    'attempts': 1, 'timeIncrement': 0.25365411074165, 'increment': 59, 
    'stepTime': 31.3885993596229, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 59, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.3885993596229, 
    'attempts': ' 1U', 'timeIncrement': 0.380481166112475, 'increment': 60, 
    'stepTime': 31.3885993596229, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 6, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.4837196511511, 
    'attempts': 2, 'timeIncrement': 0.0951202915281187, 'increment': 60, 
    'stepTime': 31.4837196511511, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 60, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.4837196511511, 
    'attempts': ' 1U', 'timeIncrement': 0.142680437292178, 'increment': 61, 
    'stepTime': 31.4837196511511, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 10, 'iterations': 10, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.5193897604741, 
    'attempts': 2, 'timeIncrement': 0.0356701093230445, 'increment': 61, 
    'stepTime': 31.5193897604741, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 61, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.5728949244587, 
    'attempts': 1, 'timeIncrement': 0.0535051639845668, 'increment': 62, 
    'stepTime': 31.5728949244587, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 62, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.6531526704355, 
    'attempts': 1, 'timeIncrement': 0.0802577459768501, 'increment': 63, 
    'stepTime': 31.6531526704355, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 63, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.7735392894008, 
    'attempts': 1, 'timeIncrement': 0.120386618965275, 'increment': 64, 
    'stepTime': 31.7735392894008, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 7, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 64, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.9541192178487, 
    'attempts': 1, 'timeIncrement': 0.180579928447913, 'increment': 65, 
    'stepTime': 31.9541192178487, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 65, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 31.9541192178487, 
    'attempts': ' 1U', 'timeIncrement': 0.270869892671869, 'increment': 66, 
    'stepTime': 31.9541192178487, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 8, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.0218366910167, 
    'attempts': 2, 'timeIncrement': 0.0677174731679673, 'increment': 66, 
    'stepTime': 32.0218366910167, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 66, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.1234129007686, 
    'attempts': 1, 'timeIncrement': 0.101576209751951, 'increment': 67, 
    'stepTime': 32.1234129007686, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 67, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.2757772153966, 
    'attempts': 1, 'timeIncrement': 0.152364314627926, 'increment': 68, 
    'stepTime': 32.2757772153966, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 68, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.5043236873384, 
    'attempts': 1, 'timeIncrement': 0.22854647194189, 'increment': 69, 
    'stepTime': 32.5043236873384, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 69, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.5043236873384, 
    'attempts': ' 1U', 'timeIncrement': 0.342819707912834, 'increment': 70, 
    'stepTime': 32.5043236873384, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 6, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.5900286143167, 
    'attempts': 2, 'timeIncrement': 0.0857049269782086, 'increment': 70, 
    'stepTime': 32.5900286143167, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 70, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.718586004784, 
    'attempts': 1, 'timeIncrement': 0.128557390467313, 'increment': 71, 
    'stepTime': 32.718586004784, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 71, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.9114220904849, 
    'attempts': 1, 'timeIncrement': 0.192836085700969, 'increment': 72, 
    'stepTime': 32.9114220904849, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 72, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.9114220904849, 
    'attempts': ' 1U', 'timeIncrement': 0.289254128551454, 'increment': 73, 
    'stepTime': 32.9114220904849, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 32.9837356226228, 
    'attempts': 2, 'timeIncrement': 0.0723135321378635, 'increment': 73, 
    'stepTime': 32.9837356226228, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 73, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.0922059208296, 
    'attempts': 1, 'timeIncrement': 0.108470298206795, 'increment': 74, 
    'stepTime': 33.0922059208296, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 74, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.2549113681398, 
    'attempts': 1, 'timeIncrement': 0.162705447310193, 'increment': 75, 
    'stepTime': 33.2549113681398, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 75, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.2549113681398, 
    'attempts': ' 1U', 'timeIncrement': 0.244058170965289, 'increment': 76, 
    'stepTime': 33.2549113681398, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.3159259108811, 
    'attempts': 2, 'timeIncrement': 0.0610145427413223, 'increment': 76, 
    'stepTime': 33.3159259108811, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 76, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.4074477249931, 
    'attempts': 1, 'timeIncrement': 0.0915218141119835, 'increment': 77, 
    'stepTime': 33.4074477249931, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 77, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.5447304461611, 
    'attempts': 1, 'timeIncrement': 0.137282721167975, 'increment': 78, 
    'stepTime': 33.5447304461611, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 78, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.750654527913, 
    'attempts': 1, 'timeIncrement': 0.205924081751963, 'increment': 79, 
    'stepTime': 33.750654527913, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 79, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.750654527913, 
    'attempts': ' 1U', 'timeIncrement': 0.308886122627944, 'increment': 80, 
    'stepTime': 33.750654527913, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.750654527913, 
    'attempts': ' 2U', 'timeIncrement': 0.0772215306569861, 'increment': 80, 
    'stepTime': 33.750654527913, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 11, 'iterations': 11, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.7699599105773, 
    'attempts': 3, 'timeIncrement': 0.0193053826642465, 'increment': 80, 
    'stepTime': 33.7699599105773, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 80, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.7989179845737, 
    'attempts': 1, 'timeIncrement': 0.0289580739963698, 'increment': 81, 
    'stepTime': 33.7989179845737, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 81, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.8423550955682, 
    'attempts': 1, 'timeIncrement': 0.0434371109945547, 'increment': 82, 
    'stepTime': 33.8423550955682, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 82, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 33.90751076206, 
    'attempts': 1, 'timeIncrement': 0.065155666491832, 'increment': 83, 
    'stepTime': 33.90751076206, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 83, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.0052442617978, 
    'attempts': 1, 'timeIncrement': 0.097733499737748, 'increment': 84, 
    'stepTime': 34.0052442617978, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 84, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.1518445114044, 
    'attempts': 1, 'timeIncrement': 0.146600249606622, 'increment': 85, 
    'stepTime': 34.1518445114044, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 85, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.1518445114044, 
    'attempts': ' 1U', 'timeIncrement': 0.219900374409933, 'increment': 86, 
    'stepTime': 34.1518445114044, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.2068196050069, 
    'attempts': 2, 'timeIncrement': 0.0549750936024833, 'increment': 86, 
    'stepTime': 34.2068196050069, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 86, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.2892822454106, 
    'attempts': 1, 'timeIncrement': 0.0824626404037249, 'increment': 87, 
    'stepTime': 34.2892822454106, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 87, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.4129762060162, 
    'attempts': 1, 'timeIncrement': 0.123693960605587, 'increment': 88, 
    'stepTime': 34.4129762060162, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 88, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.4129762060162, 
    'attempts': ' 1U', 'timeIncrement': 0.185540940908381, 'increment': 89, 
    'stepTime': 34.4129762060162, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 13, 'iterations': 13, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.4593614412433, 
    'attempts': 2, 'timeIncrement': 0.0463852352270953, 'increment': 89, 
    'stepTime': 34.4593614412433, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 89, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.528939294084, 
    'attempts': 1, 'timeIncrement': 0.0695778528406429, 'increment': 90, 
    'stepTime': 34.528939294084, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 90, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.6333060733449, 
    'attempts': 1, 'timeIncrement': 0.104366779260964, 'increment': 91, 
    'stepTime': 34.6333060733449, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 91, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.6333060733449, 
    'attempts': ' 1U', 'timeIncrement': 0.156550168891446, 'increment': 92, 
    'stepTime': 34.6333060733449, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 10, 'iterations': 10, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.6724436155678, 
    'attempts': 2, 'timeIncrement': 0.0391375422228616, 'increment': 92, 
    'stepTime': 34.6724436155678, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 92, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.7311499289021, 
    'attempts': 1, 'timeIncrement': 0.0587063133342924, 'increment': 93, 
    'stepTime': 34.7311499289021, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 93, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.8192093989035, 
    'attempts': 1, 'timeIncrement': 0.0880594700014387, 'increment': 94, 
    'stepTime': 34.8192093989035, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 94, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 34.9512986039057, 
    'attempts': 1, 'timeIncrement': 0.132089205002158, 'increment': 95, 
    'stepTime': 34.9512986039057, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 5, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 95, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.1494324114089, 
    'attempts': 1, 'timeIncrement': 0.198133807503237, 'increment': 96, 
    'stepTime': 35.1494324114089, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 6, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 96, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.1494324114089, 
    'attempts': ' 1U', 'timeIncrement': 0.297200711254855, 'increment': 97, 
    'stepTime': 35.1494324114089, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.2237325892226, 
    'attempts': 2, 'timeIncrement': 0.0743001778137139, 'increment': 97, 
    'stepTime': 35.2237325892226, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 97, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.2237325892226, 
    'attempts': ' 1U', 'timeIncrement': 0.111450266720571, 'increment': 98, 
    'stepTime': 35.2237325892226, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.2515951559028, 
    'attempts': 2, 'timeIncrement': 0.0278625666801427, 'increment': 98, 
    'stepTime': 35.2515951559028, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 98, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.293389005923, 
    'attempts': 1, 'timeIncrement': 0.0417938500202141, 'increment': 99, 
    'stepTime': 35.293389005923, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 99, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.3560797809533, 
    'attempts': 1, 'timeIncrement': 0.0626907750303211, 'increment': 100, 
    'stepTime': 35.3560797809533, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 100, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.4501159434988, 
    'attempts': 1, 'timeIncrement': 0.0940361625454816, 'increment': 101, 
    'stepTime': 35.4501159434988, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 101, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.591170187317, 
    'attempts': 1, 'timeIncrement': 0.141054243818222, 'increment': 102, 
    'stepTime': 35.591170187317, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 4, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 102, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.591170187317, 
    'attempts': ' 1U', 'timeIncrement': 0.211581365727334, 'increment': 103, 
    'stepTime': 35.591170187317, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6440655287488, 
    'attempts': 2, 'timeIncrement': 0.0528953414318334, 'increment': 103, 
    'stepTime': 35.6440655287488, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 103, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6440655287488, 
    'attempts': ' 1U', 'timeIncrement': 0.0793430121477501, 'increment': 104, 
    'stepTime': 35.6440655287488, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6639012817858, 
    'attempts': 2, 'timeIncrement': 0.0198357530369375, 'increment': 104, 
    'stepTime': 35.6639012817858, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 104, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6639012817858, 
    'attempts': ' 1U', 'timeIncrement': 0.0297536295554063, 'increment': 105, 
    'stepTime': 35.6639012817858, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6713396891746, 
    'attempts': 2, 'timeIncrement': 0.00743840738885157, 'increment': 105, 
    'stepTime': 35.6713396891746, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 105, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6824973002579, 
    'attempts': 1, 'timeIncrement': 0.0111576110832774, 'increment': 106, 
    'stepTime': 35.6824973002579, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 106, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6824973002579, 
    'attempts': ' 1U', 'timeIncrement': 0.016736416624916, 'increment': 107, 
    'stepTime': 35.6824973002579, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6866814044141, 
    'attempts': 2, 'timeIncrement': 0.00418410415622901, 'increment': 107, 
    'stepTime': 35.6866814044141, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 107, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6866814044141, 
    'attempts': ' 1U', 'timeIncrement': 0.00627615623434351, 'increment': 108, 
    'stepTime': 35.6866814044141, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6882504434727, 
    'attempts': 2, 'timeIncrement': 0.00156903905858588, 'increment': 108, 
    'stepTime': 35.6882504434727, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 108, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6882504434727, 
    'attempts': ' 1U', 'timeIncrement': 0.00235355858787882, 'increment': 109, 
    'stepTime': 35.6882504434727, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6888388331197, 
    'attempts': 2, 'timeIncrement': 0.000588389646969705, 'increment': 109, 
    'stepTime': 35.6888388331197, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 3, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 109, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6888388331197, 
    'attempts': ' 1U', 'timeIncrement': 0.000882584470454557, 'increment': 110, 
    'stepTime': 35.6888388331197, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6890594792373, 
    'attempts': 2, 'timeIncrement': 0.000220646117613639, 'increment': 110, 
    'stepTime': 35.6890594792373, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 110, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6890594792373, 
    'attempts': ' 1U', 'timeIncrement': 0.000330969176420459, 'increment': 111, 
    'stepTime': 35.6890594792373, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891422215314, 
    'attempts': 2, 'timeIncrement': 8.27422941051147e-05, 'increment': 111, 
    'stepTime': 35.6891422215314, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 111, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891422215314, 
    'attempts': ' 1U', 'timeIncrement': 0.000124113441157672, 'increment': 112, 
    'stepTime': 35.6891422215314, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891422215314, 
    'attempts': ' 2U', 'timeIncrement': 3.1028360289418e-05, 'increment': 112, 
    'stepTime': 35.6891422215314, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891499786215, 
    'attempts': 3, 'timeIncrement': 7.7570900723545e-06, 'increment': 112, 
    'stepTime': 35.6891499786215, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 112, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891616142566, 
    'attempts': 1, 'timeIncrement': 1.16356351085318e-05, 'increment': 113, 
    'stepTime': 35.6891616142566, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 113, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891616142566, 
    'attempts': ' 1U', 'timeIncrement': 1.74534526627976e-05, 'increment': 114, 
    'stepTime': 35.6891616142566, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891659776198, 
    'attempts': 2, 'timeIncrement': 4.36336316569941e-06, 'increment': 114, 
    'stepTime': 35.6891659776198, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 114, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891659776198, 
    'attempts': ' 1U', 'timeIncrement': 6.54504474854911e-06, 'increment': 115, 
    'stepTime': 35.6891659776198, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891676138809, 
    'attempts': 2, 'timeIncrement': 1.63626118713728e-06, 'increment': 115, 
    'stepTime': 35.6891676138809, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 115, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891676138809, 
    'attempts': ' 1U', 'timeIncrement': 2.45439178070592e-06, 'increment': 116, 
    'stepTime': 35.6891676138809, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891676138809, 
    'attempts': ' 2U', 'timeIncrement': 6.13597945176479e-07, 'increment': 116, 
    'stepTime': 35.6891676138809, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891676138809, 
    'attempts': ' 3U', 'timeIncrement': 1.5339948629412e-07, 'increment': 116, 
    'stepTime': 35.6891676138809, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 1, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891676138809, 
    'attempts': ' 4U', 'timeIncrement': 3.834987157353e-08, 'increment': 116, 
    'stepTime': 35.6891676138809, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['dynamic-implicit']._Message(STATUS, {'totalTime': 35.6891676138809, 
    'attempts': ' 5U', 'timeIncrement': 9.58746789338249e-09, 'increment': 116, 
    'stepTime': 35.6891676138809, 'step': 1, 'jobName': 'dynamic-implicit', 
    'severe': 2, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['dynamic-implicit']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Too many attempts made for this increment', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 
    'step': 0, 'frame': 116, 'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'THE ANALYSIS HAS BEEN TERMINATED DUE TO PREVIOUS ERRORS. ALL OUTPUT REQUESTS HAVE BEEN WRITTEN FOR THE LAST CONVERGED INCREMENT.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'dynamic-implicit'})
mdb.jobs['dynamic-implicit']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'dynamic-implicit'})
# Save by User on 2024_07_06-06.43.25; build 2020 2019_09_13-19.49.31 163176
