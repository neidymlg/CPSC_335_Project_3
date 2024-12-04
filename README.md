Overview

This project addresses two algorithmic problems: the Coin Change Problem and the Network Delay Time Problem. Both algorithms are implemented in Python and are accompanied by pseudocode, mathematical analysis, and testing.
Problems Addressed

Coin Change Problem (Dynamic Programming)
Objective: Determine the minimum number of coins required to make a given amount. If it's not possible, return -1.
Implementation: A bottom-up dynamic programming approach with a list tracking coin combinations.
Network Delay Time Problem (Floyd-Warshall Algorithm)
Objective: Find the minimum time required for all nodes in a network to receive a signal from a given source. If some nodes can't be reached, return -1.
Implementation: Floyd-Warshall algorithm, used for finding shortest paths in a weighted graph.
Files

coin_change.py
Implements the solution to the Coin Change problem.
network_delay.py
Implements the solution to the Network Delay Time problem.
report_project3.pdf
Detailed report including pseudocode, mathematical analysis, and testing results.
This README file


Running the Programs

Ensure Python is installed.
Coin Change Problem
Run the script:
python coin_change.py
Example Output:
Coins used: [5, 5, 1]  
Number of coins used: 3  
Network Delay Time Problem
Run the script:
python network_delay.py
Example Output:
Minimum time for all nodes to get the message: 2  
0
