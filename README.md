This solution uses the Floyd-Warshall algorithm to compute the shortest paths between all pairs of nodes in the network.
Algorithm
Create an n × n
n×n matrix initialized with infinity (inf) for all distances, except for self-loops (set to 0).
Update the matrix with direct travel times from the input edges.
Use the Floyd-Warshall algorithm to compute the shortest paths:
For each intermediate node k, update paths between every pair of nodes i and 
j to use k as an intermediate step if it reduces the travel time.
Find the maximum time for the signal to reach any node from the start. If some nodes remain unreachable, return -1.

Code Usage

Requirements
Python 3.
Running the Code
Save the file as network_delay.py.
Run the script:
python network_delay.py
