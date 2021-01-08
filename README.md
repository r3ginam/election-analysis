# Colorado Congressional Election Audit

## Project Overview
A Colorado Board of Elections employee has tasked the analyst with the following list to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Challenge Overview
The election commission has requested some additional data to complete the elections audit:

1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.1, Visial Studio Code 1.52.1

## Election Audit Results
The analysis of the election show that:

- There were 369,711 votes cast in the congressional election.

- The table below shows the counties that participated in the election and the votes they contributed:


| County: | Denver | Jefferson | Arapahoe |
| :------------- | :-------------: | :-------------: | :-------------: |
| Votes:  | 272,892 | 38,855 | 11,606 |
| Percentage:  | 73.8% | 23.0% | 6.7% |


The county with the largest voter turnout was Denver.

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidate results were:
  - Charles Casper Stockham recieved 23.0% of the final vote and 85,213 votes.
  - Diana DeGette recieved 73.8% of the final vote and 272,892 votes.
  - Raymon Anthony Doane recieved 3.1% of the final vote and 11,606 votes.
  
- The winner of the election was
  - Diana DeGette recieved 73.8% of the final vote and 272,892 votes.

## Election Audit Summary

In conclusion, this script may be used to audit results of future elections. While it was designed with this election in mind, small modifications can be applied to the script to work with any election. A few modifications are listed below:
- In line 6 (shown below), "election_results.csv" would need to be changed to the name of the file containing the election data

  ```Python
  file_to_load = os.path.join("Resources", "election_results.csv")
  ```
- If the file contains different headers, lines 48 and 51 would need to be changed.
  ```Python
   candidate_name = row[2]
   county_name = row[1]
   ```
