import random
from typing import List, Dict
import math

import filter
from connect import connect, shim
from shim_ideal import generate
from filter import filter_ter

start_individuals = 300
count_iterations = 5000

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
    return round(random.uniform(0, 2), 5)

def random_value_T() -> float:
    return round(random.uniform(0, 2), 5)


def start(f_discret, f1, f2):
    individuals = generate_individuals()
    indiv: Dict[float, Pair] = {}
    sig1, sig2 = connect(f_discret, f1, f2)
    ideal = generate(f_discret, f1, f2, sig1, sig2)
    for i in range(count_iterations):
        if i != 0:
            indiv = mutation(indiv)
            individuals = crossing(indiv)
        errors: Dict[float, Pair] = {}
        for j in range(len(individuals)):
            error = calculate_error(ideal, shim(f_discret, sig1, sig2, individuals[i].get_K(), individuals[i].get_T()))
            errors[error] = individuals[i]
        indiv = calculate_probability(errors)
        min_error = sorted(errors.keys())[0]
        if min_error < 0.1:
            return errors[min_error]


def generate_individuals() -> List[Pair]:
    result = List[Pair]()
    for i in range(start_individuals):
        K = random_value_K()
        T = random_value_T()
        result.append(Pair(K, T))
    return result

def calculate_error(ideal: List[float], signal: List[float]) -> float:
    error = 0
    for i in range(len(signal)):
        error += (ideal[i] - signal[i])**2
    return math.sqrt(error / len(signal))

def calculate_probability(inputs: Dict[float, Pair]) -> Dict[float, Pair]:
    keys_max = sorted(inputs.keys(), reverse=True)[0]
    outputs: Dict[float, Pair] = {}
    for key, value in inputs.items():
        outputs[(keys_max - key) / keys_max] = value
    return outputs

def crossing(individuals: Dict[float, Pair]) -> List[Pair]:
    result = List[Pair]()
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
        if key > crossing_individual_probability_limit and mutation_probability > random.random():
            operation: Pair = random.choice(choice)
            if operation == 'minus':
                result[key] = Pair(value.get_K() - step_K, value.get_T() - step_T)
            else:
                result[key] = Pair(value.get_K() + step_K, value.get_T() + step_T)
        else:
            result[key] = value
    return result
