import heapq
import sys
def prim_mst(n, adj):
    visited = [False] * (n + 1)
    min_heap = [(0, 1)]  # (weight, node), start from node 1
    total_weight = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return total_weight
input = sys.stdin.read
data = input().split()

n = int(data[0])
m = int(data[1])
adj = [[] for _ in range(n + 1)]

index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    adj[u].append((v, w))
    adj[v].append((u, w))
    index += 3

print(prim_mst(n, adj))


