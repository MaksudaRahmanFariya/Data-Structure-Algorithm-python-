

# Example usage:
#n = 10
#


#simulate_blocks_world(n,commands)

def find_block(blocks, block_id):
    for i, stack in enumerate(blocks):
        if block_id in stack:
            return i, stack.index(block_id)
    return -1, -1

def return_blocks_above(blocks, stack_id, index):
    while len(blocks[stack_id]) > index + 1:
        top = blocks[stack_id].pop()
        blocks[top].append(top)

def move_onto(blocks, a, b):
    sa, ha = find_block(blocks, a)
    sb, hb = find_block(blocks, b)
    if sa == sb or a == b:
        return
    return_blocks_above(blocks, sa, ha)
    return_blocks_above(blocks, sb, hb)
    blocks[sa].pop()
    blocks[sb].append(a)

def move_over(blocks, a, b):
    sa, ha = find_block(blocks, a)
    sb, _ = find_block(blocks, b)
    if sa == sb or a == b:
        return
    return_blocks_above(blocks, sa, ha)
    blocks[sa].pop()
    blocks[sb].append(a)

def pile_onto(blocks, a, b):
    sa, ha = find_block(blocks, a)
    sb, hb = find_block(blocks, b)
    if sa == sb or a == b:
        return
    return_blocks_above(blocks, sb, hb)
    moving = blocks[sa][ha:]
    blocks[sa] = blocks[sa][:ha]
    blocks[sb].extend(moving)

def pile_over(blocks, a, b):
    sa, ha = find_block(blocks, a)
    sb, _ = find_block(blocks, b)
    if sa == sb or a == b:
        return
    moving = blocks[sa][ha:]
    blocks[sa] = blocks[sa][:ha]
    blocks[sb].extend(moving)

def main():
    n = int(input())
    blocks = [[i] for i in range(n)]

    while True:
        command = input().strip()
        if command == 'quit':
            break

        parts = command.split()
        action, a, mode, b = parts[0], int(parts[1]), parts[2], int(parts[3])

        if a == b:
            continue
        sa, _ = find_block(blocks, a)
        sb, _ = find_block(blocks, b)
        if sa == sb:
            continue

        if action == 'move' and mode == 'onto':
            move_onto(blocks, a, b)
        elif action == 'move' and mode == 'over':
            move_over(blocks, a, b)
        elif action == 'pile' and mode == 'onto':
            pile_onto(blocks, a, b)
        elif action == 'pile' and mode == 'over':
            pile_over(blocks, a, b)

    for i in range(n):
        print(f"{i}:", end='')
        if blocks[i]:
            print(' ' + ' '.join(map(str, blocks[i])))
        else:
            print()

if __name__ == "__main__":
    main()
