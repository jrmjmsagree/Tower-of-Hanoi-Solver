def tower_of_hanoi(n, source, target, auxiliary, moves=None):
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target))
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target, moves)
        moves.append((source, target))
        tower_of_hanoi(n - 1, auxiliary, target, source, moves)
    return moves

def print_moves(moves):
    for i, move in enumerate(moves, 1):
        print(f"Move {i}: {move[0]} -> {move[1]}")

if __name__ == "__main__":
    N = int(input("Enter number of disks: "))
    moves = tower_of_hanoi(N, 'A', 'C', 'B')
    print_moves(moves)
    print(f"Total moves: {len(moves)}")
