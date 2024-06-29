from input import  StandardLogger, set_up_logger, change_to_output_directory, map_json_to_objects
from steel_connection import * 


# Example usage
# Set the input file path
file_path = "input.json"
input_params = map_json_to_objects(file_path)
print(input_params.CaeName)
dir = "output"
change_to_output_directory(dir)
#logfile_path = "abaqus_connection_script.log"
#logging = set_up_logger(logfile_path)
logging = StandardLogger()
run_script(logging, input_params)


