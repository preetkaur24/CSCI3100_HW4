import sys

def round10(x: int) -> int:
    r = x % 10
    return x - r if r < 5 else x + (10 - r)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, d = data[0], data[1]
    a = data[2:2 + n]

    # Prefix sums for O(1) range sums
    pref = [0] * (n + 1)
    s = 0
    for i, v in enumerate(a, 1):
        s += v
        pref[i] = s

    INF = 10**18
    dp_prev = [INF] * (n + 1)
    dp_prev[0] = 0
    ans = INF

    # Use k groups where 1 <= k <= d+1 (d dividers give up to d+1 groups)
    for _ in range(d + 1):
        dp_cur = [INF] * (n + 1)
        for i in range(1, n + 1):
            best = INF
            pi = pref[i]
            # Last group is (j+1..i)
            for j in range(i):
                val = dp_prev[j] + round10(pi - pref[j])
                if val < best:
                    best = val
            dp_cur[i] = best
        ans = min(ans, dp_cur[n])
        dp_prev = dp_cur

    print(ans)

if __name__ == "__main__":
    main()