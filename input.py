import json
import logging
import os
from sys import __stdout__, __stderr__ 
import csv

def read_csv_to_tuples(file_path):
    # Initialize an empty list to store the tuples
    data_tuples = []
    
    # Open the CSV file and create a reader object
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Skip the header row
        next(csv_reader)
        
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            # Convert each row to a tuple and append to the list
            data_tuples.append((float(row[0]), float(row[1])))
    
    # Convert the list of tuples to a tuple of tuples
    result = tuple(data_tuples)
    
    return result

# Example usage (commented out to prevent execution here):
# file_path = 'path_to_your_file.xlsx'
# data_tuples = read_excel_to_tuples(file_path)
# print(data_tuples)

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
        print >> __stderr__, message


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
    def __init__(self, Name, Geometry,SteelMaterial,BoltMaterial,LoadingStep,Contact,load):
        self.Name = Name
        self.Geometry = Geometry
        self.SteelMaterial = SteelMaterial
        self.BoltMaterial = BoltMaterial
        self.LoadingStep = LoadingStep
        self.Contact = Contact
        self.Load = load



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


class LoadingStep:
    def __init__(self, Name, StepType, TimePeriod, InitialInc, MinInc, MaxNumInc):
        self.Name = Name
        self.StepType = StepType
        self.TimePeriod = TimePeriod
        self.InitialInc = InitialInc
        self.MinInc = MinInc
        self.MaxNumInc = MaxNumInc

class Contact:
    def __init__(self, Name, FrictionCoeff):
        self.Name = Name
        self.FrictionCoeff = FrictionCoeff



class Load:
    def __init__(self, Name, load):
        self.Name = Name
        self.LoadData = load



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
        loading_step = LoadingStep(**model_data['LoadingStep'])
        contact = Contact(**model_data['Contact'])
        load_name = model_data['Load']['Name']
        load_file_name = model_data['Load']['File']
        load_data = read_csv_to_tuples(load_file_name)
        load = Load(load_name, load_data)
        model = Model(model_data['Name'], geometry, steel_material, bolt_material, loading_step, contact,load)
        models.append(model)
    
    return InputParameter(json_data['CaeName'], models)













