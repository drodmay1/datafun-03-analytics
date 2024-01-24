''' Module for project 3 of 44608'''

# Import necessary modules
import json
import os
import pathlib
import math
import davidrm_utils


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















