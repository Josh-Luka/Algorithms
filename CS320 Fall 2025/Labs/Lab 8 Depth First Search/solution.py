from collections import Counter
from edgegraph import GraphEL


def pld_graph(g: GraphEL) -> list:

    if g is None:
        raise ValueError("Bad graph")

    valCount = Counter(e.get_value() for e in g.edges())
    palin = set()

    def checkPal(values):

        n = len(values)
        for start in range(n):
            for end in range(start + 3, n + 1):
                seg = values[start:n]
                if seg == seg[::-1]:
                    palin.add(tuple(seg))

    def extendPath(currVer, usedEdges, pathVals):

        if len(pathVals) >= 2:
            lastVal = pathVals[-1]
            if valCount[lastVal] == 1:
                mid = (len(pathVals) - 1) // 2
                if len(pathVals) - 1 > mid:
                    return

        checkPal(pathVals)

        for e in g.incident(currVer):
            if e in usedEdges:
                continue

            nextVer = e.head() if e.tail() == currVer else e.tail()
            usedEdges.add(e)
            pathVals.append(e.get_value())
            extendPath(nextVer, usedEdges, pathVals)
            usedEdges.remove(e)
            pathVals.pop()

    for e in g.edges():
        v1, v2 = e.ends()
        val = e.get_value()

        extendPath(v2, {e}, [val])
        extendPath(v1, {e}, [val])

    return sorted(list(palin))
