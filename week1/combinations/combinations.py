n,k = map(int, input().split())
def rec_C(n, k):
    if k > n:
        return 0
    elif k == 0:
        return 1
    else:
        return rec_C(n - 1, k) + rec_C(n - 1, k - 1)

print(rec_C(n, k))