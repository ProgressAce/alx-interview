# The Coin Change Problem

Lovely stuff

### Explaination on solution:

coins = [1, 2, 5]

coins = [1, 2, 5]
amount/change = 12

recorded/dynamic_amounts = [len change]
eg. 0 1 2 3 4 5 6 7 8 9 10 11 12
-1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

working out.
change 0 1 2 3 4 5 6 7 8 9 10 11 12
min_coins 0 1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
to make R1 change: since we can use R1 coin we say index 1 - 1 = 0. At 0 the best min coin answer is 0.
since we use the R1 coin we add one to the min coin answer, 0 + 1, to get the min coin for
change 1.
if the amount was higher and we could use other coins, then we repeat the process with them
individually as well and compare it to the lowest found minimum coin and then choose the
lowest coin number.
Essentially we use the answers to the previous subproblems to eventually find the answer or final
amount we are looking for.
Thus, dynamic programming (using answers of previous subproblems; builds up to the solution)

working out.
change 0 1 2 3 4 5 6 7 8 9 10 11 12
min_coins 0 1 1 2 -1 -1 -1 -1 -1 -1 -1 -1 -1

working out.
change 0 1 2 3 4 5 6 7 8 9 10 11 12
min_coins 0 1 1 2 2 1 2 2 3 3 2 3 3
