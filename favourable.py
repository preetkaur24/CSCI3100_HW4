import sys
sys.setrecursionlimit(10**7)

T = int(input())

for _ in range(T):
    S = int(input())
    
    book = {}
    memo = {}
    
    for _ in range(S):
        parts = input().split()
        page = int(parts[0])
        
        if parts[1] == "favourably":
            book[page] = ("end", 1)
        elif parts[1] == "catastrophically":
            book[page] = ("end", 0)
        else:
            a = int(parts[1])
            b = int(parts[2])
            c = int(parts[3])
            book[page] = ("choice", [a, b, c])
    
    def count_ways(page):
        if page in memo:
            return memo[page]
        
        node_type = book[page][0]
        
        if node_type == "end":
            result = book[page][1]
        else:
            result = 0
            for next_page in book[page][1]:
                result += count_ways(next_page)
        
        memo[page] = result
        return result
    
    print(count_ways(1))