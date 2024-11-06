import heapq

N, M = map(int, input().split())
Graph = [[] for _ in range(N)]

for _ in range(M):
    a,b,c = map(int, input().split())
    a -= 1
    b -= 1
    Graph[a].append((b, c))
    Graph[b].append((a, c))

def dist_from(k: int):
    pque = []
    dist = [10 ** 9] * N
    dist[k] = 0
    heapq.heappush(pque, (0, k))
    while len(pque) > 0:
        now_cost, now = heapq.heappop(pque)
        if now_cost > dist[now]:
            continue
        for to, cost in Graph[now]:
            if now_cost + cost < dist[to]:
                dist[to] = now_cost + cost
                heapq.heappush(pque, (now_cost + cost, to))
    
    return dist

from_first = dist_from(0)
from_last = dist_from(N - 1)

for i in range(N):
    print(from_first[i] + from_last[i])