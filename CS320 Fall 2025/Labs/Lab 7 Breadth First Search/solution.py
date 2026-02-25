from collections import deque


def bfs(g, s):

    if g is None or s is None:
        raise ValueError("Invalid graph or vertex")

    if s.name not in g._vertices:
        return []

    vis = set()
    q = deque([(s, 0)])
    lv = {}
    vis.add(s)

    while q:
        v, d = q.popleft()
        lv.setdefault(d, []).append(v)
        for nbr in g.adjacent(v):
            if nbr not in vis:
                vis.add(nbr)
                q.append((nbr, d + 1))

    return [tuple(lv[i]) for i in sorted(lv.keys())]
