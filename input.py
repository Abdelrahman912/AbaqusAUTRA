import json
import logging
import os
from sys import __stdout__

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def set_up_logger(logfile_path):

    # Configure logging
    logging.basicConfig(
        filename=logfile_path,  # Path to the log file
        filemode='w',  # Overwrite the log file each time
        level=logging.DEBUG,  # Logging level
        format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
    )

    return logging

class StandardLogger:
    def __init__(self):
        pass
    
    def info(self, message):
       print >> __stdout__, message

    def error(self, message):
        print >> __stdout__, message


    def warning(self, message):
        print >> __stdout__, message

    def debug(self, message):
        print >> __stdout__, message


def change_to_output_directory(dir):
    # Check if the directory exists
    if not os.path.exists(dir):
        # Create the directory if it doesn't exist
        os.makedirs(dir)
    # Set the directory where you want to store the files
    os.chdir(dir)





import json

class ConnectionConfig:
    def __init__(self, NoL, NoT, PL, PT, EL, ET, HoleDia):
        self.NoL = NoL
        self.NoT = NoT
        self.PL = PL
        self.PT = PT
        self.EL = EL
        self.ET = ET
        self.HoleDia = HoleDia

class Section:
    def __init__(self, h, b, t, c):
        self.h = h
        self.b = b
        self.t = t
        self.c = c

class Beam:
    def __init__(self, Length, Name, Section, ConnectionConfig):
        self.Length = Length
        self.Name = Name
        self.Section = Section
        self.ConnectionConfig = ConnectionConfig

class Column:
    def __init__(self, ClearHeight, Name, Section, ConnectionConfig):
        self.ClearHeight = ClearHeight
        self.Name = Name
        self.Section = Section
        self.ConnectionConfig = ConnectionConfig

class Bolt:
    def __init__(self, Name, ShankDia, HeadLength, HeadDia):
        self.Name = Name
        self.ShankDia = ShankDia
        self.HeadLength = HeadLength
        self.HeadDia = HeadDia

class Plate:
    def __init__(self, Name, t):
        self.Name = Name
        self.t = t

class Geometry:
    def __init__(self, Beam, BeamColumnClearance, Column, Bolt, Plate):
        self.Beam = Beam
        self.BeamColumnClearance = BeamColumnClearance
        self.Column = Column
        self.Bolt = Bolt
        self.Plate = Plate

class Model:
    def __init__(self, Name, Geometry,SteelMaterial,BoltMaterial):
        self.Name = Name
        self.Geometry = Geometry
        self.SteelMaterial = SteelMaterial
        self.BoltMaterial = BoltMaterial


class InputParameter:
    def __init__(self, CaeName, Models):
        self.CaeName = CaeName
        self.Models = Models

class BiLinearMaterial:
    def __init__(self, Fy, Fu, EpsPlasticY, EpsPlasticU, Name, Description, E, v):
        self.Fy = Fy
        self.Fu = Fu
        self.EpsPlasticY = EpsPlasticY
        self.EpsPlasticU = EpsPlasticU
        self.Name = Name
        self.Description = Description
        self.E = E
        self.v = v


def map_json_to_objects(file_path):
    json_data = read_json_file(file_path)
    models = []
    for model_data in json_data['Models']:
        beam_data = model_data['Geometry']['Beam']
        column_data = model_data['Geometry']['Column']
        bolt_data = model_data['Geometry']['Bolt']
        plate_data = model_data['Geometry']['Plate']
        beam_column_clearance = model_data['Geometry']['BeamColumnClearance']
        
        beam_section = Section(**beam_data['Section'])
        beam_connection_config = ConnectionConfig(**beam_data['ConnectionConfig'])
        beam = Beam(beam_data['Length'], beam_data['Name'], beam_section, beam_connection_config)
        
        column_section = Section(**column_data['Section'])
        column_connection_config = ConnectionConfig(**column_data['ConnectionConfig'])
        column = Column(column_data['ClearHeight'], column_data['Name'], column_section, column_connection_config)
        
        bolt = Bolt(**bolt_data)
        plate = Plate(**plate_data)
        
        geometry = Geometry(beam, beam_column_clearance, column, bolt, plate)
        steel_material = BiLinearMaterial(**model_data['SteelMaterial'])
        bolt_material = BiLinearMaterial(**model_data['BoltMaterial'])
        model = Model(model_data['Name'], geometry, steel_material, bolt_material)
        models.append(model)
    
    return InputParameter(json_data['CaeName'], models)













