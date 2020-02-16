# Pyramid
For instance the pyramid is:

![](https://i.imgur.com/DazKFt3.png)

It takes a 2D list containing list of Integers as input. The input 2D lists length have to increase by one from top to down.

### Task:
Find the slope which is yield the max.
The 'slope' is the maximum sum of **consecutive** numbers from the top to the bottom of the pyramid.

> *consecutive:* From top to down goes, in the next row, the choosed number's index must be as was, or one bigger.

### Solution&Approach
My first thought was brute force, but the possibilities -> 2 on power of (rows-1), so it's inefficient with large Pyramids.
Than I thought I have to find the route, which is lead me to wasting my time. 

*The solution is to calculating the rows from down to up.*
 ##### Hint:
 
 [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/6zcFB1nIoq8/0.jpg)](http://www.youtube.com/watch?v=6zcFB1nIoq8)
 
 Youtube

### TDD (more functions = more unit tests)
That is a TDD practice, so thats why it's containing some not necesarry code in order to write more tests.
