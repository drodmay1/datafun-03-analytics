''' David_Rm_utils, this module contains and provide a reusable byline for the autor services'''

byline = "David_Rm_utils, this module contains and provide a reusable \nbyline for the autor services"

import math
import statistics

company_name: str = "David Rm Inc."
count_active_projects: int = 4
count_total_projects: int = 10
has_international_presence: bool = True
count_countries_we_work: int = 3
average_client_satisfaction: float = 3.5

services_offered: list = ["Analytics Solutions", "Data Cleansing", "Data Integration", "Data Visualization", "Data Warehousing"]
satisfaction_scores: list = [3.2, 3.9, 4.1, 2.7, 3.6]

print(company_name)
print ('Services offered')
print(services_offered)

active_projects_string: str = f"Active Projects: {count_active_projects}"
international_presence_string: str = f"International Presence: {has_international_presence}"
countries_we_work: str = f"Countries We Work: {count_countries_we_work}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"
services_offered: str = f"services_offered: {services_offered}"

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

#calculate the average satisfaction score
average_satisfaction_score = statistics.mean(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

byline: str = f"""
{company_name}
{active_projects_string}
{international_presence_string}
{countries_we_work}
{client_satisfaction_string}
{stats_string}
"""

print(stats_string)
print("this is the smallest satisfaction scored by a client")
print(smallest)

print("this is the largest satisfaction scored by a client")
print(largest)

print(byline)

def main():
  ''' Display all output'''
  print(company_name)
  print(active_projects_string)
  print(international_presence_string)
  print(client_satisfaction_string)
  print(stats_string)
  print(byline)

if __name__ == "__main__":
  main()