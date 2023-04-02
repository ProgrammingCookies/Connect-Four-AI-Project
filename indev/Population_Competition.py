from NN import *
from Gameboard import *
from Connect_Four import * 
import copy
import numpy as np
import random

def matchBetweenAI(modelA, modelB):
    board = initBoard()
    while(True):
        moveA = nnPrediction(understandableBoard(board,0),modelA)
        row = drop(board, moveA, 0)
        if fourConnectedCheck(board, row, moveA, 0):
            return 1
        moveB = nnPrediction(understandableBoard(board,1),modelB)
        row = drop(board, moveB, 1)
        if fourConnectedCheck(board, row, moveB, 1):
            return -1
        if tie(board):
            return 0

#Initialize Population
def initPopulation(populationSize):
    population = []
    for i in range(populationSize):
        # Randomly generate weights and biases for each network
        weights = np.random.randn(input_size, output_size)
        biases = np.random.randn(output_size)
        network = (weights, biases)
        population.append(network)
    return population

def competition(population, challengerIndex, scoreboard):
    #Going from challengerIndex to population because every element challenges everyone in front of it in the array.
    #This way challengerIndex have already fought everyone before it.
    localScores = int[len(population) - challengerIndex]
    for i in range(challengerIndex+1, len(population)):
        if(i != challengerIndex):
            resultA = matchBetweenAI(population[challengerIndex], population[i])
            resultB  = matchBetweenAI(population[i],population[challengerIndex])
            localScores[0] += resultA - resultB #This is the challengers score
            localScores[i - challengerIndex] -= resultA - resultB #The challengers score
    return localScores

#TODO Decide how many parents each new offspring will have
# Create offspring
def initOffspring(population, inputSize, outputSize, mutationRate, tourSize):
    offspring = []
    for i in range(len(population)):
        # Use crossover and mutation to create variation in the offspring, example tourSize
        parent1, parent2 = tournamentSelectionMultipleParents(population, 2, tourSize)
        child_weights = parent1[0] * 0.5 + parent2[0] * 0.5 + np.random.randn(inputSize, outputSize) * mutationRate
        child_biases = parent1[1] * 0.5 + parent2[1] * 0.5 + np.random.randn(outputSize) * mutationRate
        child_network = (child_weights, child_biases)
        offspring.append(child_network)
    return offspring


#Tournament selection to find parents, finding the highest performance one out of a subset to create some variance instead of just say, taking the top 5 performers. 
def tournamentSelection(population, tournament_size):
    # Select a random subset of the population
    tournament = random.sample(population, tournament_size)

    # Choose the individual with the highest fitness from the tournament
    winner = max(tournament, key=lambda x: x.fitness)

    return winner

#Find a specific number of parents with tournament selection.
def tournamentSelectionMultipleParents(population, numParents, tourSize):
    parents = []
    for i in range(numParents):
        parent = tournamentSelection(population, tourSize)
        parents.append(parent)
    return parents


