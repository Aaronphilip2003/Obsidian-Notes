
# A* Algorithm
https://www.youtube.com/watch?v=tvAh0JZF2YE&ab_channel=GateSmashers

```
The A* (pronounced "A-star") algorithm is a widely used pathfinding algorithm in computer science and artificial intelligence. It is designed to find the shortest path between two points on a weighted graph, while considering the actual cost of reaching the destination and an estimated cost to reach the goal.

A* combines elements of both uniform-cost search and greedy search to be efficient and optimal. It uses a heuristic function to estimate the cost from a given node to the goal node. This heuristic guides the algorithm towards exploring paths that are likely to be shorter and reaching the goal more quickly.
```

```
OPEN=nodes on the frontier
OPEN={<s,nil>}
while OPEN is not empty
	remove from OPEN the node <n,p> with minimum f(n)
	place <n,p> on CLOSED
	if n is a goal node,
		retrun success(pathx p)
	for each edge connecting n&m with cost c
		if <m,q> is on CLOSED and {p|e} is cheaper than q
			then remove n from CLOSED
				put <m,{p|e}> on OPEN
		else if <m,q> is on OPEN and {p|e} us cheaper than q
			then replace q with {p|e}
		else if m is not OPEN
			then put <m,{p|e}> on OPEN
return failure
```
