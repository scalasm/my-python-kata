# Find a peak

This is my implementation of finding a peak both in 1-dimensional and 2-dimensional arrays.

Note that in Java, 2D matrices are indexed by rows so I changed the algorithm to process rows instead of
columns (differently from the [MIT lesson](https://youtu.be/HtSuA80QTyo)).

The MIT algorithm was this:

1. Pick the middle column
1. Find the global max on column j at (i,j)
1. Compare (i,j-1), (i,j), (i,j+1)
1. Pick left cols if (i,j-1) > (i,j)
1. Pick right cols if (i,j+1) > (i,j)
