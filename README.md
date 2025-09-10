# Tower of Hanoi Solver

This Python script calculates and prints the solution to the classic Tower of Hanoi problem for any number of disks.

## How It Works

The script uses a recursive algorithm to determine the sequence of moves required to transfer all disks from the source rod to the target rod, following the rules of the Tower of Hanoi puzzle.

## Usage

1. Save the script as `tower_of_hanoi.py`.
2. Run it with Python:

    ```bash
    python tower_of_hanoi.py
    ```

3. Enter the desired number of disks when prompted.
4. The script will print each move in order, followed by the total number of moves.

## Example Output

```
Enter number of disks: 3
Move 1: A -> C
Move 2: A -> B
Move 3: C -> B
Move 4: A -> C
Move 5: B -> A
Move 6: B -> C
Move 7: A -> C
Total moves: 7
```

## License

MIT
