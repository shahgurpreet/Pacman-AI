# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        heuristicValue = 0
        foodDistance = []
        inverseFoodDistance = 0


        for st in newScaredTimes:
            heuristicValue += st

        foodList = newFood.asList()
        for fl in foodList:
            foodDistance.append(manhattanDistance(newPos, fl))

        if foodDistance:
            minFoodDistance = min(foodDistance)
            inverseFoodDistance = 1.0/minFoodDistance

        ghostDistance = []
        for gd in newGhostStates:
            if gd.getPosition == newPos:
                if gd.scaredTimer == 0:
                    return -10000
                else:
                    return 10000
            else:
                ghostDistance.append(manhattanDistance(newPos, gd.getPosition()))
                
        
        minGhostDistance = min(ghostDistance)
            
        heuristicValue += (minGhostDistance) * ((inverseFoodDistance))
        heuristicValue += successorGameState.getScore()
        return heuristicValue
        
        

        "*** YOUR CODE HERE ***"
##        return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):

    
    def maxPlayer(self, state, depth, currentPlayer):

        bestValue = -99999
        bestAction = ''

        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        legalMoves = state.getLegalActions(currentPlayer)
        
        for lm in legalMoves:
            successor = state.generateSuccessor(currentPlayer, lm)
            value = self.minimax(successor, depth, currentPlayer+1)
            if bestValue < value:
                bestValue = value
                bestAction = lm

        if depth == 1:
            return bestAction
        else:
            return bestValue

    def minPlayer(self, state, depth, currentPlayer):

      bestValue = 99999
      bestAction = ''
      numOfAgents = state.getNumAgents()
      
      if state.isWin() or state.isLose():
        return self.evaluationFunction(state)

      legalMoves = state.getLegalActions(currentPlayer)
      
      for lm in legalMoves:
          successor = state.generateSuccessor(currentPlayer, lm)
          if currentPlayer == numOfAgents - 1:
              if depth == self.depth:
                  value = self.evaluationFunction(successor)
              else:
                  value = self.minimax(successor, depth+1, 0)
          else:
              value = self.minimax(successor, depth, currentPlayer+1)

          if bestValue > value:
              bestValue = value
              bestAction = lm
      return bestValue
    
    
    def minimax(self, state, depth, currentPlayer):
        if currentPlayer == 0:
            return (self.maxPlayer(state, depth, currentPlayer))
        else:
            return (self.minPlayer(state, depth, currentPlayer))


    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """

        state = gameState
        currentDepth = 1
        currentPlayer = 0
        bestAction = self.minimax(state, currentDepth, currentPlayer)
        return bestAction



          
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        state = gameState
        currentDepth = 1
        currentPlayer = 0
        alpha = -999999
        beta = 999999
        bestAction = self.alphabeta(state, currentDepth, currentPlayer, alpha, beta)
        return bestAction

    def alphabeta(self, state, depth, currentPlayer, alpha, beta):
        if currentPlayer == 0:
            return self.maxPlayer(state, depth, currentPlayer, alpha, beta)
        else:
            return self.minPlayer(state, depth, currentPlayer, alpha, beta)

    def maxPlayer(self, state, depth, currentPlayer, alpha, beta):

        bestValue = -99999
        bestAction = ''

        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        legalMoves = state.getLegalActions(currentPlayer)
        for lm in legalMoves:
            successor = state.generateSuccessor(currentPlayer, lm)
            value = self.alphabeta(successor, depth, currentPlayer+1, alpha, beta)

            if value > beta:
                return value

            if value > bestValue:
                bestValue = value
                bestAction = lm

            alpha = max(alpha, bestValue)

        if depth == 1:
            return bestAction
        else:
            return bestValue


    def minPlayer(self, state, depth, currentPlayer, alpha, beta):    

        bestValue = 99999
        bestAction = ''
        numOfAgents = state.getNumAgents()

        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        legalMoves = state.getLegalActions(currentPlayer)
        for lm in legalMoves:
            successor = state.generateSuccessor(currentPlayer, lm)
            if currentPlayer == numOfAgents - 1:
                if depth == self.depth:
                    value = self.evaluationFunction(successor)
                else:
                    value = self.maxPlayer(successor, depth+1, 0, alpha, beta)
            else:
                value = self.minPlayer(successor, depth, currentPlayer+1, alpha, beta)


            if value < alpha:
                return value

            if value < bestValue:
                bestValue = value
                bestAction = lm

            beta = min(beta, bestValue)
        return bestValue
        

        
        
                

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        state = gameState
        currentDepth = 1
        currentPlayer = 0
        bestAction = self.expectimax(state, currentDepth, currentPlayer)
        return bestAction

    def expectimax(self, state, depth, currentPlayer):
        if currentPlayer == 0:
            return (self.maxPlayer(state, depth, currentPlayer))
        else:
            return (self.minPlayer(state, depth, currentPlayer))

    def maxPlayer(self, state, depth, currentPlayer):

        bestValue = -99999
        bestAction = ''

        if state.isWin() or state.isLose():
            return self.evaluationFunction(state)

        legalMoves = state.getLegalActions(currentPlayer)
        
        for lm in legalMoves:
            successor = state.generateSuccessor(currentPlayer, lm)
            value = self.expectimax(successor, depth, currentPlayer+1)
            if bestValue < value:
                bestValue = value
                bestAction = lm

        if depth == 1:
            return bestAction
        else:
            return bestValue

    def minPlayer(self, state, depth, currentPlayer):

      bestValue = 0
      bestAction = ''
      numOfAgents = state.getNumAgents()
      
      if state.isWin() or state.isLose():
        return self.evaluationFunction(state)

      legalMoves = state.getLegalActions(currentPlayer)
      chance = 1.0/len(legalMoves)
      
      for lm in legalMoves:
          successor = state.generateSuccessor(currentPlayer, lm)
          if currentPlayer == numOfAgents - 1:
              if depth == self.depth:
                  value = self.evaluationFunction(successor)
              else:
                  value = self.expectimax(successor, depth+1, 0)
          else:
              value = self.expectimax(successor, depth, currentPlayer+1)

          bestValue += value * chance
      return bestValue
    

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"

    #returning a heuritsic which takes in the minimum of the food
    #and capsule and ghost positions

    newPos = currentGameState.getPacmanPosition()
    newFood = currentGameState.getFood()
    newGhostStates = currentGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    
    heuristicValue = 0
    foodDistance = []
    inverseFoodDistance = 0
    distanceCapsule = []
    minDistanceFromCapsule = 1
    
    capsule = currentGameState.getCapsules()
    for c in capsule:
        distanceCapsule.append(manhattanDistance(newPos, c))

    if distanceCapsule:
        minDistanceFromCapsule = 1.0/min(distanceCapsule)


    foodList = newFood.asList()
    for fl in foodList:
        foodDistance.append(manhattanDistance(newPos, fl))

    if foodDistance:
        minFoodDistance = min(foodDistance)
        inverseFoodDistance = 1.0/minFoodDistance

    ghostDistance = []
    for gd in newGhostStates:
        ghostDistance.append(manhattanDistance(newPos, gd.getPosition()))
            
    if ghostDistance:
        ghostDistance = min(ghostDistance)

    heuristic = ((ghostDistance)) * ((inverseFoodDistance)) * minDistanceFromCapsule
    heuristic += currentGameState.getScore()
    return heuristic

# Abbreviation
better = betterEvaluationFunction

