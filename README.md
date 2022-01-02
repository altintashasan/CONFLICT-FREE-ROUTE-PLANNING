# CONFLICT-FREE-ROUTE-PLANNING

*TABLE OF CONTENTS*
- [LIVE DEMO](#live-demo)
- [Problem:](#problem)
- [Project Goal:](#project-goal)
- [Constraints](#constraints)
- [Algorithms:](#algorithms)
- [Tools:](#tools)
- [The situations that they are not regarded:](#the-situations-that-they-are-not-regarded)
- [How the Project Works?](#how-the-project-works)


# LIVE DEMO

You can find how the algoritm works here --> [HIT ME - 1](https://youtu.be/D676NAfTBGo) [HIT ME - 2](https://youtu.be/HPg3c6FQCkY)

# Problem:
*Conflicts in route for AGVs which are used in industrial zones.*

# Project Goal:
* Defining a route for each AGV.
* AGVs stay in pre-specified route.
* Conflicts are avoided.
* Defined routes will be efficient in case of performance measure

# Constraints
* Static Environment
* Every AGV will have the same properties
* Layout of the routes will be a grid (10x10)
* 3 AGVs will be present
* Every unit path will be the same length
* Some AGVs have a priority

# Algorithms:
A*, 
Dijkstra

# Tools:
* Language: ​ Python
* Simulation: ​ Pygame Library

# The situations that they are not regarded:
* Speed of all AGVs are static or equal.
* Roads work for one type of car, we have selected AGV.
* On routes, there are no traffic rules/elements like traffic lambs or crosswalk which
could change the arrival time.
* If there are any traffic rules, they don’t work dynamically.
* Performance measure can be selected only for one goal not multi.

# How the Project Works?

*Firstly, the algorithms which are to be used in the project were determined. The
algorithms which are more efficient was decided. Two algorithms that are efficient from these
algorithms were determined. These algorithms are A * and dijkstra algorithms. These are the
most commonly used algorithms for this field. As we have seen in our studies, these algorithms
proved to be really applicable to conflict route-planning.*

*In the beginning of the project, the path of an AGV is determined by using A * algorithm on
3 * 3 grid area. After that, the size of grid area is increased to 10 * 10. Then, second AGV is added
to the environment and the path of each AGVs are determined . At that point, there were some
conflicts occurred. To solve this problem, priority is assigned to each AGV.
First solution was if there is a conflict at a node, the AGV which has less priority is waited in
the node before the conflict node on its path. There would be no change for the path of AGV
which has a high priority. After that the third AGV is added on 10 * 10 grid area and different
experiments are tested, any conflict is prohibited by using that solution.*

![image](https://user-images.githubusercontent.com/68166794/147891734-92b35501-9784-4527-8f57-1b7604caa938.png)

**Figure 1- Block Diagram of the Conflict-Free Route Planning for adding a delay case.**

*The second solution is basically works like, if there is a conflict at a node, the path of AGV
which has a less priority is again determined without using that node (like if there is an obstacle
in that node) by using A * algorithm. Hereby, two AGVs can move on from desired beginning
node to any desired end node without conflict. Moreover, the third AGV is added on 10 * 10 grid
area and different experiments are tested, any conflict is prohibited by using that solution. In
addition, AGVs cannot have a same beginning point because any node can be used one time at
the same moment by an AGV.*

![image](https://user-images.githubusercontent.com/68166794/147891762-fbcdb3cf-9103-428a-a08b-e21222ac3dec.png)

**Figure 2- Block Diagram of the Conflict-Free Route Planning for replanning case.**

*To conclude, there are two solution ways that are tested to solve this problem. Both
solutions are successfully solved the problem. The first solution increased the time with
adding a delay node on the less priority AGV’s route. Nevertheless, the second solution is
finding a new path without losing time. At the beginning, second solution could be seen that
is more optimized than first one. However, According to the results, it can be clearly said that
first solution is solved more optimized.*



