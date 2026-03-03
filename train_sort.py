n = int(input())
cars = [int(input()) for _ in range(n)]


def sol(cars: list[int]) -> int:
    if not cars:
        return 0
    inc = [1] * len(cars)
    dec = [1] * len(cars)
    for i in range(len(cars) - 1, -1, -1):
        for j in range(i + 1, len(cars)):
            if cars[i] < cars[j]:
                inc[i] = max(inc[i], 1 + inc[j])
            if cars[i] > cars[j]:
                dec[i] = max(dec[i], 1 + dec[j])
    ans = 0
    for i in range(0, len(cars)):
        if -1 + inc[i] + dec[i] > ans:
            ans = -1 + inc[i] + dec[i]
    return ans


print(sol(cars))
