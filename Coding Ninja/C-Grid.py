
n, m, z, k = map(int, input().split())
direction_del = {'L': (0, -1),'R': (0, 1),'U': (-1, 0), 'D': (1, 0)}
rev_dir = {'L': 'R','R': 'L','U': 'D', 'D': 'U'}
#n, m, z, k = map(int, input().split())

grid = [list(input().strip()) for _ in range(n)]
robots = []
for _ in range(z):
    r, c, d = input().split()
    r = int(r) - 1
    c = int(c) - 1
    robots.append([r, c, d])
for idx in range(z):
    r, c, d = robots[idx]
    for _ in range(k):
        dr, dc = direction_del[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '.':
            r, c = nr, nc
        else:
            d = rev_dir[d]
    robots[idx] = (r + 1, c + 1, d)
for r, c, d in robots:
    print(r,c,d)