## Follow python instruction from etl_lab_instruction
import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import  datetime

from jupyter_lsp.paths import file_uri_to_path

log_file = "./source/output/log_file.txt"
target_file = "./source/output/transformed_data.csv"

def extract_from_csv(file_to_process):
   data_frame = pd.read_csv(file_to_process)
   return data_frame

## It requires an extra argument lines=True to enable the function to read the file as a JSON object on line to line basis as follows.
def extract_from_json(file_to_process):
    data_frame = pd.read_json(file_to_process , lines=True)
    return data_frame

## we use pd.concat to append data to an existing DataFrame.
# Why use pd.concat:

# pd.concat is more efficient when adding rows or combining multiple DataFrames.
# It provides better control over the operation, allowing you to concatenate along rows or columns.
# It also includes the ignore_index=True argument, which resets the index to avoid duplication when combining DataFrames.


def extract_from_xml(file_to_process):
    data_frame = pd.DataFrame(columns=['name','height','weight'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find('name').text
        height =float(person.find('height').text)
        weight =float(person.find('weight').text)
        data_frame = pd.concat([data_frame, pd.DataFrame([{'name': name, 'height': height, 'weight': weight}])], ignore_index= True)
    return data_frame

# extract data from different file format
def extract():
    extracted_data = pd.DataFrame(columns=['name','height','weight']) # create an empty data frame to hold extracted data

    # process all csv files, except the target file './source/*.json'
    for csvfile in glob.glob('./source/*.csv'):
        if csvfile != target_file: # check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

    # process all csv files, except the target file
    for jsonfile in glob.glob('./source/*.json'):
        if jsonfile != target_file:  # check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

    for xmlFile in glob.glob('./source/*.xml'):
        extracted_data = pd.concat([extracted_data,pd.DataFrame(extract_from_xml(xmlFile))], ignore_index=True)

    return extracted_data


# Transform data

def transform(data):
    '''Convert inches to meters and round off to two decimals
    1 inch is 0.0254 meters '''
    data['height'] = round(data.height * 0.0254, 2 )
    '''Convert pounds to kilograms and round off to two decimals 
        1 pound is 0.45359237 kilograms '''
    data['weight'] = round(data.weight *0.45359237,2)
    return data

# convert data to csv load data to csv

def load_data(target_file, transformed_data):
    transformed_data.to_csv(target_file)

# log processes (message)

def log_progress(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open(log_file, 'a+') as f:
        f.write(timestamp + ' ' + message + '\n')

 # Log the init of the ETL process
log_progress("ETL Job Started")

# Log the beginning of the Extraction process
log_progress("Extract phase Started")
extracted_data = extract()
# Log the completion of the Extraction process
log_progress("Extract phase Ended")

# Log the beginning of the Transformation process
log_progress("Transform phase Started")
transformed_data = transform(extracted_data)
print("Transformed Data")
print(transformed_data)
log_progress("Transform phase Ended")

# Log the beginning of the Loading process
log_progress("Load phase Started")
load_data(target_file, transformed_data)

# Log the completion of the Loading process
log_progress("Load phase Ended")

# Log the completion of the ETL process
log_progress("ETL Job Ended")
