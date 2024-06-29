# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-19.49.31 163176
# Run by User on Sat Jun 29 12:18:36 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(1.21563, 1.21528), width=178.941, 
    height=120.556)
session.viewports['Viewport: 1'].makeCurrent()
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
execfile('main.py', __main__.__dict__)
#: SteelConnection
#: The model "Model - Steel Connection" has been created.
#: The model database has been saved to "C:\Users\User\OneDrive\RUB\Master\Second Semester\Applied FEM\Abaqus\AbaqusScriptingRubProject\output\SteelConnection.cae".
print 'RT script done'
#: RT script done
