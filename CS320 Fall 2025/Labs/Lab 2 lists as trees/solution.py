
# returns leftmost child of position n

def _iOILeft(n, t):
    i = prev = n
    while (i < len(t)) and (t[i] is not None):
        prev = i
        i = (i * 2) + 1
    return prev if (prev != n) else None
# returns next inorder node to position n
# core idea is to move right one position
# there are three cases
# parent -> leftmost of right child
# left child -> parent
# right child -> leftmost of grandparent’s right


def _iOINext(n, t):

    r = (n * 2) + 2  # right
    if (r < len(t)) and (t[r] is not None):
        # parent with right child
        # move to leftmost child of right (or right
        # if no child)
        if (n := _iOILeft(r, t)) is not None:
            return n
        return r
    elif n % 2:
        # left leaf or left parent with no
        # right child, go to parent
        n = (n - 1) // 2  # left child -> parent
        return n
    else:
        # at this point, right leaf with
        # no right children. So node’s
        # parent’s subtree is completed.
        # so next is first ancestor
        # above parent who is parent
        # of a left node
        p = (n - 2) // 2  # parent
        leftp = p % 2
        gp = (p - 1) // 2  # grandparent
        while gp and (not leftp):
            leftp = gp % 2
            gp = (gp - 1) // 2
        if leftp:
            return gp
    return -1
# this is a generator routine that
# returns successive elements in the
# inorder traversal


def _iOI(t):

    # find leftmost child = start node
    if (inorder := _iOILeft(0, t)) is None:
        inorder = 0
    while inorder >= 0:
        yield t[inorder]
        inorder = _iOINext(inorder, t)
# Inorder traversal that is iterative and does
# not use a stack (similar to a Morris
# traversal)


def inOrderIter(t):

    if not len(t):
        return []
    return list(_iOI(t))


def findMinIndex(x, t):

    while True:
        left = 2 * x + 1
        if left >= len(t) or t[left] is None:
            return x
        x = left


def deleteAt(x, t):

    le = 2 * x + 1
    ri = 2 * x + 2

    hasL = le < len(t) and t[le] is not None
    hasR = ri < len(t) and t[ri] is not None

    if not hasL and not hasR:
        t[x] = None
    elif hasL and not hasR:
        t[x] = t[le]
        deleteAt(le, t)
    elif not hasL and hasR:
        t[x] = t[ri]
        deleteAt(ri, t)
    else:
        suc = findMinIndex(ri, t)
        t[x] = t[suc]
        deleteAt(suc, t)


def findKey(k, t):

    if k is None:
        raise ValueError("null key")
    if t is None:
        raise ValueError("no tree")

    try:

        x = 0
        while x < len(t) and t[x] is not None:
            if t[x] is None:
                raise LookupError("not in tree")
            if t[x] == k:
                return x
            elif k < t[x]:
                x = 2 * x + 1
            else:
                x = 2 * x + 2
        raise LookupError("not in tree")

    except TypeError as z:
        raise Exception("tree error") from z


def addKey(k, t):

    if k is None:
        raise ValueError("null key")
    if t is None:
        raise ValueError("no tree")

    try:

        x = 0
        while True:

            while x >= len(t):
                t.extend([None]*max(1, len(t)))
            if t[x] is None:
                t[x] = k
                break
            elif k == t[x]:
                return t
            elif k < t[x]:
                x = 2 * x + 1
            else:
                x = 2 * x + 2

    except TypeError as z:
        raise Exception("tree error") from z

    while t and t[-1] is None:
        t.pop()

    return t


def deleteKey(k, t):

    if k is None:
        raise ValueError("null key")
    if t is None:
        raise ValueError("no tree")

    try:
        index = findKey(k, t)
        deleteAt(index, t)
    except LookupError:
        raise LookupError("not in tree")
    except TypeError as z:
        raise Exception("tree error") from z

    while t and t[-1] is None:
        t.pop()

    return t

# insert unit tests here


if __name__ == "__main__":
    t1 = [4, 2, 6, 1, 3, 5, 7]
    t2 = [4, 2, 6, 1, None, 5, 7]
    t3 = [1, None, 2, None, None, None, 4]
    t4 = [4, 2, None, 1]
    print(f"inOrderIter{t1}␣is␣{inOrderIter(t1)}")
    print(f"inOrderIter{t2}␣is␣{inOrderIter(t2)}")
    print(f"inOrderRecurse({t3})␣is␣{inOrderIter(t3)}")
    print(f"inOrderRecurse({t4})␣is␣{inOrderIter(t3)}")
