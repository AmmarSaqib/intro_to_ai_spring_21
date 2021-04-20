"""
Intro. To AI

Lab 4: Hill Climb Algorithm


In this lab you'll be implementing a Hill Climb algorithm on a very simple Graph.

Hill climb is a heurisitc search used for mathematical optimization problems in the field of Artificial Intelligence. Given a large set 
of inputs and a good heuristic function, it tried to find a sufficiently
good solution to the problem. This solution may not be the global maximum.

In this lab you'll be implementing a basic version of the algorithm on 
a graph. For representing a Graph you may modify the class in the 
graph.py file accordingly.

In this task you will create a function named hill_climb_search() that
will take in the graph along with the start and the goal node. The 
function will print the path it took after reaching the goal node.

You will need to use data structures in this implementation my suggestion would be to make use of the stack. You can add the stack
class that you created it Lab 1 for this after a few modifications.

The graph that you will work on is as follows, where the representation
includes the node and the heuristic of that (node, heuristic):

# A is the root node with B, C, D as successors
(A,3) -> (B, 4), (C, 6), (D, 5) 
(B,4) -> (E, 3), (F, 2) 
(C,6) -> (G, 7), (H, 8)
(D,5) -> (I, 6), (J, 7)
(H,8) -> (K, 9)


Initial node to start is "A" and the goal node is "K"
"""