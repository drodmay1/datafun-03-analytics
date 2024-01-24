''' Module for project 2 of 44608 includes functions '''

#import modules
import math
import statistics
import pathlib
import os
import time
import sys
import davidrm_utils

"""" Function 1. For item in Range: Create a function to generate folders for a given range (e.g., years) """


def create_folders_for_range(start_year, end_year):
  """ Creates folders for a given years range 2020 - 2024 """
  for year in range(start_year, end_year + 1):
    pathlib.Path(str(year)).mkdir(exist_ok=True)


""" Function 2. For Item in list: Develop a function to create folders from a list of names """


def create_folders_from_list(folder_names):
  """ Creates folders from a list of names """


#creates folder from  list of names
list = ['name1', 'name2', 'name3', 'name4']
for items in list:
  pathlib.Path(str(items)).mkdir(exist_ok=True)
""" 
Function 3. Create prefixed folders by transforming a list of names and combining each with a prefix (e.g., "Data-")"""


def create_prefixed_folders(folder_list, prefix):
  """ 
  Creates prefixed folders by transforming a list of names and combining each 
with a prefix.
  """


#creates prefixed folders from a list of names (states)
states = ['MD', 'VA', 'AZ', 'DE', 'WV', 'MA', 'VT', 'ME']
prefix = "Data-"
pre_res = []
for item in states:
  pre_res.append(prefix + item)

#create folders for new prefixed names list
list = [
    'Data-MD', 'Data-VA', 'Data-AZ', 'Data-DE', 'Data-WV', 'Data-MA',
    'Data-VT', 'Data-ME'
]
for item in list:
  if not os.path.exists(item):
    os.mkdir(item)
    
"""Function 4. While Loop: Write a function to create folders periodically (e.g., one folder every 5 seconds)."""


def create_folders_periodically(duration):
  """Creates folders periodically (e.g., one folder every 5 seconds)"""


#creates folders periodically
routers = 5  #number of routers deployed today
while routers > 0:
  routers -= 1
  time.sleep(5)
  pathlib.Path("Data-MD").mkdir(exist_ok=True)


def main():
  ''' Main function to demonstrate module capabilities. '''

  # Print byline from imported module
  print(f"Byline: {davidrm_utils.byline}")

  # Call function 1 to create folders for a range (e.g. years)
  create_folders_for_range(start_year=2020, end_year=2024)

  # Call function 2 to create folders given a list
  list = ['name1', 'name2', 'name3', 'name4']
  create_folders_from_list(list)

  # Call function 3 to create folders using comprehension
  folder_list = ['MD', 'VA', 'AZ', 'DE', 'WV', 'MA', 'VT', 'ME']
  prefix = 'data-'
  create_prefixed_folders(folder_list, prefix)

  # Call function 4 to create folders periodically using while
  duration_secs = 5  # duration in seconds
  create_folders_periodically(duration_secs)

  # Add options e.g., to force lowercase and remove spaces
  # to one or more of your functions (e.g. function 2)
  # Call your function and test these options
  regions = [
      'North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania',
      'Middle East'
  ]
  create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)

  if __name__ == '__main__':
    main()
