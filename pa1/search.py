
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    
    startState = problem.getStartState()
    dfsStack = util.Stack()
    dfsStack.push(startState)
    actionList = [[]]
    visited = []
    pathList = []
    goalState=(0, 0)
    successorList=[]
    
    visited.append(startState)
    
    while dfsStack.isEmpty() == False:
        currentState  = dfsStack.pop()
        visited.append(currentState)
        if not problem.isGoalState(currentState):
            successorList = problem.getSuccessors(currentState)
            for nextState,action,cost in successorList:
                if nextState not in visited:
                    dfsStack.push(nextState)
                    actionList.append([currentState,nextState,action])
        else:
            actionLists = [action for action in actionList if action != []]
            goalState = currentState
            while startState != goalState:
                for action in reversed(actionLists):
                     if goalState == action[1]:
                        pathList.append(action[2])
                        goalState = action[0]
                       
                        
            break
    pathList.reverse()        
    return pathList
                
                

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    

    startState = problem.getStartState()
    bfsQueue = util.Queue()
    bfsQueue.push(startState)
    actionList = [[]]
    visited = []
    pathList = []
    goalState=(0, 0)
    successorList=[]
    
    visited.append(startState)
    
    while bfsQueue.isEmpty() == False:
        currentState  = bfsQueue.pop()
        if not problem.isGoalState(currentState):
            successorList = problem.getSuccessors(currentState)
            for nextState,action,cost in successorList:
                if nextState not in visited:
                    bfsQueue.push(nextState)
                    visited.append(nextState)
                    actionList.append([currentState,nextState,action])
        else:
            actionLists = [action for action in actionList if action != []]
            goalState = currentState
            while startState != goalState:
                for action in actionLists:
                    if goalState == action[1]:
                        pathList.append(action[2])
                        goalState = action[0]
            break
    pathList.reverse()
    return pathList
                
  

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    startState = problem.getStartState()
    ucsQueue = util.PriorityQueue()
    visited.append(startState)
    ucsQueue.push(startState,0)
    goalState=(0, 0)
    actionList = []
    queueItems = []
    pathList1 = []
    pathList2 = []
    costList1 = []
    costList2 = []
    cost1 = 0;
    cost2 = 0;

    successorList=[]
   
    while ucsQueue.isEmpty() == False:
        
        currentState  = ucsQueue.pop()
        visited.append(currentState)
        
        if not problem.isGoalState(currentState):
            successorList = problem.getSuccessors(currentState)
            for nextState,action,cost in successorList:
                
                    if nextState not in visited:
                        actionList.append((currentState,nextState,action,cost))
                        
                        costFromStart = 0;
                        goalState = nextState
                
                        while startState != goalState:
                            for action in reversed(actionList):
                                if goalState  == action[1]:
                                    costFromStart += action[3]
                                    goalState = action[0]

                        if nextState not in queueItems:
                            ucsQueue.push(nextState, costFromStart)
                            queueItems.append(nextState)
                       
        else:

            goalState = currentState
            while startState != goalState:
                for action in actionList:
                    if goalState == action[1]:
                        pathList1.append(action[2])
                        costList1.append(action[3])
                        goalState = action[0]
                        

            goalState = currentState
            while startState != goalState:
                for action in reversed(actionList):
                    if goalState == action[1]:
                        pathList2.append(action[2])
                        costList2.append(action[3])
                        goalState = action[0]
                        
            break
    
    cost1 = sum(int(i) for i in costList1)
    cost2 = sum(int(i) for i in costList2)
    
    pathList1.reverse()
    pathList2.reverse()
    if cost1 > cost2:
        return pathList2
    else:
        return pathList1
    
        

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearet
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    visited = []
    startState = problem.getStartState()
    ucsQueue = util.PriorityQueue()
    visited.append(startState)
    ucsQueue.push(startState, nullHeuristic(startState,problem))
    goalState=(0, 0)
    actionList = []
    queueItems = []
    pathList1 = []
    pathList2 = []
    costList1 = []
    costList2 = []
    dList = []
    directionList = []
    cost1 = 0;
    cost2 = 0;
    
    aDic = {str(tuple(startState)):0}
    bDic = {str(tuple(startState)):0}
    successorList = []
   
    while ucsQueue.isEmpty() == False:
        
        currentState  = ucsQueue.pop()
        
        if not problem.isGoalState(currentState):
            successorList = problem.getSuccessors(currentState)
            for nextState,action,cost in successorList:
                if(str(tuple(nextState))) in aDic:
                    temp = 0
                    hCost = heuristic(nextState, problem)
                    temp = bDic[str(tuple(currentState))]+ cost + hCost
                    if aDic[str(tuple(nextState))] >  temp:
                        for d in directionList:
                            if d[1] == nextState:
                                directionList.remove(d)
                        visited.remove(nextState)
                        
                            
                if nextState not in visited:
                    
                    costFromStart = 0;
                    costFromStart = bDic[str(tuple(currentState))]
                    
                    bDic[str(tuple(nextState))] = bDic[str(tuple(currentState))] + cost
                    hCost = heuristic(nextState, problem)

                    totalCost = costFromStart + hCost + cost
                    aDic[str(tuple(nextState))] = totalCost
                    
                    directionList.append((currentState,nextState, action,totalCost))
                    visited.append(nextState)

                    ucsQueue.push(nextState,totalCost)
                    
                    
                    
                     
                     
                                                           
        else:
           
            
            goalState = currentState
         
            while startState != goalState:
                for d in directionList:
                    if goalState == d[1]:
                        pathList1.append(d[2])
                        costList1.append(d[3])
                        goalState = d[0]
                        
            goalState = currentState
            while startState != goalState:
                for d in reversed(directionList):
                    if goalState == d[1]:
                        pathList2.append(d[2])
                        costList2.append(d[3])
                        goalState = d[0]
            
            break
    
    cost1 = sum(int(i) for i in costList1)
    cost2 = sum(int(i) for i in costList2)
        
    pathList1.reverse()
    pathList2.reverse()
    if cost1 > cost2:
        return pathList2
    else:
        return pathList1
    
    
    

    

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


