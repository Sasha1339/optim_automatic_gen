import random
from typing import List, Dict
import math

import filter
from connect import connect, shim
from shim_ideal import generate
from filter import filter_ter

start_individuals = 10
count_iterations = 5

crossing_probability = 0.7
mutation_probability = 0.2

crossing_individual_probability_limit = 0.7

step_K = 0.00001
step_T = 0.00001

class Pair():
    __K: float
    __T: float

    def __init__(self, K: float, T: float):
        self.__K = K
        self.__T = T

    def get_K(self):
        return self.__K

    def get_T(self):
        return self.__T

def random_value_K() -> float:
    return round(random.uniform(0, 0.0003), 6)

def random_value_T() -> float:
    return round(random.uniform(0, 0.01), 6)


def start(f_discret, f1, f2):
    individuals = generate_individuals()
    indiv: Dict[float, Pair] = {}
    sig1, sig2 = connect(f_discret, f1, f2)
    ideal = generate(f_discret, f1, f2, sig1, sig2)
    errors: Dict[float, Pair] = {}
    g_shim, x = shim(f_discret, sig1, sig2, 0, 0)
    for i in range(count_iterations):
        print("Итерация №"+str(i))
        if i != 0:
            indiv = mutation(indiv)
            individuals = crossing(indiv)
            if len(individuals) == 0:
                individuals = generate_individuals()
        errors = {}
        for j in range(len(individuals)):
            signal = filter_ter(x, g_shim, f_discret, individuals[j].get_K(), individuals[j].get_T(), 2)
            error = calculate_error(ideal, signal)
            errors[error] = individuals[j]
        indiv = calculate_probability(errors)
        min_error = sorted(errors.keys())[0]
        if min_error < 0.03:
            return errors[min_error]
    return errors[sorted(errors.keys())[0]]


def generate_individuals() -> List[Pair]:
    result =[]
    for i in range(start_individuals):
        K = random_value_K()
        T = random_value_T()
        result.append(Pair(K, T))
    return result

def calculate_error(ideal: List[float], signal: List[float]):
    error = 0
    for i in range(len(signal)):
        error += abs(ideal[i] - signal[i])
    return error / len(signal)

def calculate_probability(inputs: Dict[float, Pair]) -> Dict[float, Pair]:
    keys_max = sorted(inputs.keys(), reverse=True)[0]
    outputs: Dict[float, Pair] = {}
    for key, value in inputs.items():
        outputs[(keys_max - key) / keys_max] = value
    return outputs

def crossing(individuals: Dict[float, Pair]) -> List[Pair]:
    result = []
    for key, value in individuals.items():
        if key > crossing_individual_probability_limit and crossing_probability > random.random():
            two_parent: Pair = random.choice(list(individuals.values()))
            result.append(Pair(value.get_K(), two_parent.get_T()))
            result.append(value)
    return result

def mutation(individuals: Dict[float, Pair]) -> Dict[float, Pair]:
    choice = ['minus', 'plus']
    result: Dict[float, Pair] = {}
    for key, value in individuals.items():
        if mutation_probability > random.random():
            operation: Pair = random.choice(choice)
            if operation == 'minus':
                result[key] = Pair(value.get_K() - step_K, value.get_T() - step_T)
            else:
                result[key] = Pair(value.get_K() + step_K, value.get_T() + step_T)
        else:
            result[key] = value
    return result
