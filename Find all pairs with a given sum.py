def allPairs(self, A, B, N, M, X):
    lst = []
    A.sort()
    for i in range(N):
        for j in range(0, M):
            if A[i] + B[j] == X:
                lst.append([A[i], B[j]])

    return lst
