import random
from util import cost, best_path, valid_path


def ga_tsp(initial_pop, distances, generations):

    if initial_pop is None or distances is None or generations is None:
        raise ValueError("Invalid argument")
    if generations <= 0:
        raise ValueError("Invalid argument")

    pop = list(initial_pop)
    popSize = len(pop)
    numCities = len(pop[0])

    def tournament_select(k=5):
        cand = random.sample(pop, k)
        return best_path(cand, distances)

    def pmx(parent1, parent2):
        p1 = list(parent1)
        p2 = list(parent2)

        a, b = sorted(random.sample(range(numCities), 2))
        child = [None] * numCities

        child[a:b] = p1[a:b]

        for i in range(a, b):
            if p2[i] not in child:
                pos = i
                val = p2[i]
                while True:
                    pos = p2.index(p1[pos])
                    if child[pos] is None:
                        child[pos] = val
                        break

        for i in range(numCities):
            if child[i] is None:
                child[i] = p2[i]

        return tuple(child)

    def mutate(path, rate=0.08):
        p = list(path)
        if random.random() < rate:
            i, j = random.sample(range(numCities), 2)
            p[i], p[j] = p[j], p[i]
        return tuple(p)

    for _ in range(generations):

        eliteCount = max(1, popSize // 20)
        elites = sorted(pop, key=lambda x: cost(x, distances))[:eliteCount]
        newPop = elites.copy()

        while len(newPop) < popSize:
            p1 = tournament_select()
            p2 = tournament_select()
            c1 = mutate(pmx(p1, p2))
            c2 = mutate(pmx(p2, p1))

            if valid_path(c1):
                newPop.append(c1)
            if len(newPop) < popSize and valid_path(c2):
                newPop.append(c2)

        pop = newPop

    return best_path(pop, distances)
