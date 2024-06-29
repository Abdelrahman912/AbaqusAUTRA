import json
import logging
import os

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



def change_to_output_directory(dir):
    # Check if the directory exists
    if not os.path.exists(dir):
        # Create the directory if it doesn't exist
        os.makedirs(dir)
    # Set the directory where you want to store the files
    os.chdir(dir)



import json

class ConnectionConfig:
    def __init__(self, NoX, NoY, PX, PY, EX, EY):
        self.NoX = NoX
        self.NoY = NoY
        self.PX = PX
        self.PY = PY
        self.EX = EX
        self.EY = EY

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

class Geometry:
    def __init__(self, Beam, Column):
        self.Beam = Beam
        self.Column = Column

class Model:
    def __init__(self, Name, Geometry):
        self.Name = Name
        self.Geometry = Geometry

class InputParameter:
    def __init__(self, CaeName, Models):
        self.CaeName = CaeName
        self.Models = Models

def map_json_to_objects(file_path):
    json_data = read_json_file(file_path)
    models = []
    for model_data in json_data['Models']:
        beam_data = model_data['Geometry']['Beam']
        column_data = model_data['Geometry']['Column']
        
        beam_section = Section(**beam_data['Section'])
        beam_connection_config = ConnectionConfig(**beam_data['ConnectionConfig'])
        beam = Beam(beam_data['Length'], beam_data['Name'], beam_section, beam_connection_config)
        
        column_section = Section(**column_data['Section'])
        column_connection_config = ConnectionConfig(**column_data['ConnectionConfig'])
        column = Column(column_data['ClearHeight'], column_data['Name'], column_section, column_connection_config)
        
        geometry = Geometry(beam, column)
        model = Model(model_data['Name'], geometry)
        models.append(model)
    
    return InputParameter(json_data['CaeName'], models)










