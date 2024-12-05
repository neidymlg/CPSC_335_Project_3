The goal of this problem is to determine the minimum number of coins required to make up a given amount of money using coins of specified denominations. If the amount cannot be formed, the output should be -1.
Approach

This solution uses dynamic programming to compute the minimum coin combination for each possible amount up to the target value.
Algorithm
Create a list coin_combo of size amount + 1, initialized with None.
Set coin_combo[0] to an empty list, representing no coins needed for zero amount.
Iterate through each amount from 1 to the target amount:
For each coin denomination, check if it can contribute to the current amount.
Update coin_combo[i] with the smallest combination that sums to the amount.
Return the combination of coins for the target amount, or -1 if no solution exists.

Code Usage

Requirements
Python 3.
Running the Code
Save the file as coin_change.py.
Run the script:
python coin_change.py
