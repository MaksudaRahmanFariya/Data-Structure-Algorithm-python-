def repaint_fence(n, a, m, orders):
    color_to_indices = {}
    seen = set()
    final_orders = []
    for c in reversed(orders):
        if c not in seen:
            final_orders.append(c)
            seen.add(c)
    final_orders.reverse()
    from collections import defaultdict
    positions = defaultdict(list)
    for i, color in enumerate(a):
        positions[color].append(i)
    for c in final_orders:
        if len(positions[c]) <= 1:
            continue
        l = positions[c][0]
        r = positions[c][-1]
        for i in range(l, r + 1):
            a[i] = c

        positions[c] = list(range(l, r + 1))
        return a