# AIVD Christmas Puzzle 2019 (Assignment 8)

To test whether assignment 8 of the AIVD Christmas puzzle 2019 had a (Nash) equilibrium, we wrote a genetic algorithm from scratch in Python to simulate a population of other participants. We wanted to see if evolving this population of strategies would converge to an "ultimate" strategy.

After 2000 generations out of a population of 1500, we found:
- no equilibrium was reached
- the average of all winners of each generation was (almost) a linear increase across the envelopes (`[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]`)
- a winning strategy should at least be able to beat this average
- this assignment is at least just as psychological as it is mathematical!

Results have not been published yet.

```
>>> df.describe()
                0            1            2            3            4           5            6            7            8            9
count  2000.00000  2000.000000  2000.000000  2000.000000  2000.000000  2000.00000  2000.000000  2000.000000  2000.000000  2000.000000
mean      1.17650     3.056500     5.441500     7.329000     9.324000    11.30650    13.441000    14.678000    17.202000    17.045000
std       1.12115     2.066747     3.111498     4.268591     5.536547     6.62265     7.740121     9.121234    10.248889     9.603285
min       0.00000     0.000000     0.000000     0.000000     0.000000     0.00000     0.000000     0.000000     0.000000     0.000000
25%       0.00000     1.000000     3.000000     4.000000     4.000000     5.00000     7.000000     6.000000     8.750000     8.000000
50%       1.00000     3.000000     6.000000     8.000000    10.000000    12.00000    14.000000    15.000000    17.000000    16.000000
75%       2.00000     4.000000     8.000000    11.000000    14.000000    17.00000    20.000000    23.000000    26.000000    26.000000
max       7.00000    10.000000    13.000000    18.000000    21.000000    25.00000    29.000000    33.000000    36.000000    37.000000
```

# Authors
- Jorijn Smit ([@jorijnsmit](https://github.com/jorijnsmit/))
- Maarten Smit ([@bakmaaier](https://github.com/bakmaaier/))

# References
- Holland, J. H. (1992). *Adaptation in natural and artificial systems: an introductory analysis with applications to biology, control, and artificial intelligence*. MIT press. (https://mitpress.mit.edu/books/adaptation-natural-and-artificial-systems)
- https://en.wikipedia.org/wiki/Nash_equilibrium
