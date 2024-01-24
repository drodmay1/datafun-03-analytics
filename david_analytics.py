''' Module for project 3 of 44608'''

# Import necessary modules, Standard library imports
import json
import os
import pathlib
import math
import davidrm_utils
import sys
sys.path.append("davidrodriguez@davids-mbp datafun-03-analytics %")
import requests
import csv
from pathlib import Path


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

# function to Write functions to save content to different file types
def write_txt_file(folder_name, filename, data):
  folder_path = Path(folder_name)
  folder_path.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist
  file_path = folder_path.joinpath(filename)      
  with file_path.open('w') as file:
      file.write(data)
      print(f"Text data saved to {file_path}")


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















