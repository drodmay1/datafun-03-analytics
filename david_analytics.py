''' Module for project 3 of 44608'''

# Import necessary modules, Standard library imports
import json
import os
import pathlib
import math
import sys
sys.path.append("davidrodriguez@davids-mbp datafun-03-analytics %")
import csv
from pathlib import Path
from collections import Counter
import string

#External library imports
import requests
import pandas as pd
import openpyxl

#import my modules
import davidrm_utils
import david_projsetup

''' data acquisition '''

#function to fetch txt data from the web
def fetch_and_write_text_data(folder_name, filename, url):
  response = requests.get(url)
  if response.status_code == 200:
      write_text_data(folder_name, filename, response.text)
  else:
      print(f"Failed to fetch text data: {response.status_code}")

def write_text_data(folder_name, filename, text_data):
  with open(f"{folder_name}/{filename}", "w", encoding="utf-8") as text_file:
      text_file.write(text_data)

''' write data '''

# function to Write functions to save content to different file types
def write_txt_file(folder_name, filename, data):
  folder_path = Path(folder_name)
  folder_path.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
  file_path = folder_path.joinpath(filename)      
  with file_path.open('w') as file:
      file.write(data)
      print(f"Text data saved to {file_path}")

''' Process data and generate output '''

#function to process text data, word count
def process_text_data(input_file, output_file):
  with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()
           
    words = text.split()  
    word_count = len(words)

#function to process CSV data
def process_csv_data(input_csv, output_text):
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        headers = next(csv_reader)
        
        # Initialize variables for analysis
        total_rows = 0
        column_sums = {header: 0 for header in headers}

        # Process each row in the CSV
        for row in csv_reader:
            total_rows += 1
            for header, value in zip(headers, row):
                try:
                    column_sums[header] += float(value)
                except ValueError:
                  pass

        # Calculate averages for each column
        column_averages = {header: column_sums[header] / total_rows for header in headers}

    # Generate insights
    insights = f"Total Rows: {total_rows}\n\nColumn Averages:\n"
    for header, average in column_averages.items():
        insights += f"{header}: {average:.2f}\n"

    # Save insights to text file
    with open(output_text, 'w', encoding='utf-8') as output_file:
        output_file.write(insights)

#function to process excel data
def process_excel_data(input_excel, output_text):
    try:
        # Read Excel file
        df = pd.read_excel(input_excel)

        # Get basic statistics and information about the data
        summary = df.describe()

        # Convert the summary to a string for saving
        summary_str = summary.to_string()

        # Save the summary to a text file
        with open(output_text, 'w', encoding='utf-8') as output_file:
            output_file.write(summary_str)

        print(f"Summary saved to {output_text}")
    except Exception as e:
        print(f"An error occurred: {e}")

#function to process JSON data
def process_json_data_from_url(json_url):
  try:
      # Fetch JSON data from the URL
      response = requests.get(json_url)
      response.raise_for_status()  # Raise an HTTPError for bad responses

      # Load JSON data
      data = response.json()

      # Extract relevant information (modify as per your JSON structure)
      name = data.get('name', 'N/A')
      code = data.get('code', 'N/A')
      city = data.get('city', 'N/A')

      # Create a human-readable text format
      result_text = f"Name: {name}\nCode: {code}\nCity: {city}"

      return result_text
  except requests.exceptions.RequestException as e:
      return f"Error fetching data from URL: {e}"
  except json.JSONDecodeError as e:
      return f"Error decoding JSON: {e}"
  except Exception as e:
      return f"An error occurred: {e}"
  
  ''' extra functions '''

# function to get square numbers of each number of a list
def get_square_numbers(numbers):
  """Get the square of each number in the list."""
  square_numbers = [num ** 2 for num in numbers]
  return square_numbers

numbers_list = [1, 2, 3, 4, 5]
result = get_square_numbers(numbers_list)
print(result)

# function to save data to a file
def save_to_file(data, filename):
  """Save data to a file."""
  with open(filename, 'w') as file:
    json.dump(data, file)
    
data_to_save = {'Router1': 'Model_CBA850', 'Router2': 'Model_CX467'}
save_to_file(data_to_save, 'router_models.json')

# function to save data to a file in a specified folder
def save_to_folder(data, folder_path, filename):
  """Save data to a file in the specified folder."""
  os.makedirs(folder_path, exist_ok=True)

  file_path = os.path.join(folder_path, filename)

  with open(file_path, 'w') as file:
      json.dump(data, file)
  print(f"Data saved to: {file_path}")

data_to_save = {'sim ': 'tmobile', 'sim2': 'verizon'}
folder_to_save = 'sim_cards'
file_to_save = 'sim_cards.txt'

# Call the function to save data to a file in the specified folder
save_to_folder(data_to_save, folder_to_save, file_to_save)
             
# function to create folders from a list
def create_folders_from_list(folder_names):
  list = ['cradlepoint', 'ciena', 'accedian', 'mpls']
  for item in list:
    pathlib.Path(str(item)).mkdir(exist_ok=True)

def main():
  ''' Main function '''

# Print byline from imported module
print(f"Byline: {davidrm_utils.byline}")

#call function to fetch txt data from the web
fetch_and_write_text_data("output_folder", "README.txt", "https://pasteur.epa.gov/uploads/10.23719/1518467/README.txt")

# Call function to write_txt_file
folder_name = "Text File"
filename = "air_quality.txt"
text_data = "The meteorological input data for CMAQ were derived from outputs of the Community Earth System Model and the Coupled Model version 3 following Representative Concentration Pathway 8.5, which represents a relatively high warming scenario."

write_txt_file(folder_name, filename, text_data)

#call function to process text data
input_file = "company.txt"
output_file = "word_count.txt"

process_text_data(input_file, output_file)

#call function to process CSV data
input_csv = "freshman_kgs.csv"
output_text = "insights.txt"

process_csv_data(input_csv, output_text)

#call function to process excel data
input_excel = 'modem_upgrades.xlsx'
output_text = 'summary_excel.txt'

process_excel_data(input_excel, output_text)

#call function to process JSON data
json_url = "https://freetestdata.com/wp-content/uploads/2023/04/2.4KB_JSON-File_FreeTestData.json"
result = process_json_data_from_url(json_url)
process_json_data_from_url(json_url)

print(result)


#call function to to get square numbers of each number of a list
get_square_numbers([6, 8, 10 ,12])
result = get_square_numbers([6, 8, 10 ,12])
print(result)

#call function to to save data to a file
data_to_save = {'equipment1': 'nokia', 'equipment2': 'samsung'}
save_to_file(data_to_save, 'equipment.txt')

#call function to save data to a file in a specified folder
data_to_save = {'sim ': 'att', 'sim2': 'sprint'}
folder_to_save = 'extra_sim_cards'
file_to_save = 'extra_sim_cards.txt'
save_to_folder(data_to_save, folder_to_save, file_to_save)

#call function to create folders from a list
list = ['fiber', 'copper', 'rj45', 'sfp']
create_folders_from_list(list)

if __name__ == '__main__':
    main()















