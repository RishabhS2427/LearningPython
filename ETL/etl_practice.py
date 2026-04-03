import pandas as pd
import glob
import xml.etree.ElementTree as ET
from datetime import datetime

source_output ='./datasource/output/'
source_input ='./datasource/'
log_file = source_output + "logFile.txt"
target_file = source_output + "transformed_file.csv"
target_file_excel = source_output + "transformed_file2.xlsx"
target_file_pdf = source_output + "transformed_file2.pdf"
# Extract
def extract_from_csv(file_to_process):
    df = pd.read_csv(file_to_process)
    return df

def extract_from_xml(file_to_process):
    df = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel'])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for child in root:
        carModel = child.find('car_model').text
        yearOfManufacture = child.find('year_of_manufacture').text
        price = float(child.find('price').text)
        fuel = child.find('fuel').text
        df = pd.concat([df,pd.DataFrame([{ "car_model" : carModel,"year_of_manufacture" : yearOfManufacture,"price": price, "fuel": fuel }] )], ignore_index=True)
    return df

def extract_from_json(file_to_process):
    df = pd.read_json(file_to_process,lines=True)
    return df

def extract():
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel'])
    for csvfile in glob.glob( source_input + '*.csv'):
        if csvfile != target_file:  # check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_csv(csvfile))], ignore_index=True)

        # process all csv files, except the target file
    for jsonfile in glob.glob(source_input + '*.json'):
        if jsonfile != target_file:  # check if the file is not the target file
            extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_json(jsonfile))], ignore_index=True)

    for xmlFile in glob.glob(source_input + '*.xml'):
        extracted_data = pd.concat([extracted_data, pd.DataFrame(extract_from_xml(xmlFile))], ignore_index=True)

    return extracted_data
#Transfrom

def transform_data(data):
    data['price'] = round(data.price, 2)
    return data

#Load

def load_data(target_file, transform_data):
    transform_data.to_csv(target_file, index=False)

def load_excel(target_file_excel , transform_data):
    transform_data.to_excel(target_file_excel, index=False)

def log_progress(log_message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    current_time = datetime.now()
    timestamp = current_time.strftime(timestamp_format)
    log = open(log_file, 'a+')
    log.write(timestamp+ '\t'+ log_message + '\n')


log_progress("Start ETL Process")
log_progress("Start Extracting Data")
ed = extract()
log_progress("End Extracting Data")
log_progress("Start Transforming Data")
transform_data = transform_data(ed)
print("Transformed Data")
print(transform_data)
log_progress("End Transforming Data")
log_progress("Start Loading Data")
load_data( target_file, transform_data)
load_excel(target_file_excel, transform_data)
log_progress("End Loading Data")
log_progress("End ETL Process")
