# AI_HW1

Rush Hour game solver with A* algorithm :)

This application inputs the initial state of the board and solves the game and prints the minimum number of moves to solve it.

input sample:

8 6 6
1 2 h 2
0 1 v 3
0 0 h 2
3 1 v 3
2 5 h 3
0 4 v 2
4 4 h 2
5 0 v 3

the first line shows number of cars, game width and game height

in the above example:

8 6 6

8: number of cars
6: board width
6: board height

each one of the next 8 lines represents position of a car in the initial state. the first line shows position of the red car.

in the above example:

1 2 h 2

1 2: position of the red car in the board (x y)
h: car is horizonal (vs vertical)
2: car length is 2
