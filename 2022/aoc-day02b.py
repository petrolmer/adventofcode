score = 0
with open('aoc-day02a-input.txt') as f:
    for line in f:
        l = line.strip()
        (them, me) = l.split()
        if me == 'X': # Lose
            if them == 'A': # Rock
                score += 3
            elif them == 'B': # Paper
                score += 1
            else: # Scissors
                score += 2
        elif me == 'Y': # Draw
            score += 3
            if them == 'A': # Rock
                score += 1
            elif them == 'B': # Paper
                score += 2
            else: # Scissors
                score += 3
        else: # Win
            score += 6
            if them == 'A': # Rock
                score += 2
            elif them == 'B': # Paper
                score += 3
            else: # Scissors
                score += 1
print(score)