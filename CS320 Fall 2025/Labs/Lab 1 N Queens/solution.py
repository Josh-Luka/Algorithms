def nQueensAll(N):

    if N < 4:
        raise ValueError()

    def safe(B, R, C):

        for i in range(C):
            if B[R][i] == 1:
                return False
        for i, j in zip(range(R, -1, -1), range(C, -1, -1)):
            if B[i][j] == 1:
                return False
        for i, j in zip(range(R, N, 1), range(C, -1, -1)):
            if B[i][j] == 1:
                return False
        return True

    def solve(BS, CS):

        if CS >= N:
            sol = []
            for i in range(N):
                subtup = ()
                for j in range(N):
                    if BS[i][j] == 1:
                        subtup = (i, j)
                        sol.append(subtup)
            ans.append(sol)
            return True
        res = False
        for i in range(N):
            if safe(BS, i, CS):
                BS[i][CS] = 1
                res = solve(BS, CS + 1) or res
                BS[i][CS] = 0
        return res
    ans = []
    Bo = [[0 for _ in range(N)] for _ in range(N)]
    solve(Bo, 0)
    return ans
