score = 0
with open('aoc-day02a-input.txt') as f:
    for line in f:
        l = line.strip()
        (them, me) = l.split()
        if me == 'X': # Rock
            score += 1
            if them == 'A': # Rock
                score += 3
            elif them == 'C': # Scissors
                score += 6
        elif me == 'Y': # Paper
            score += 2
            if them == 'B': # Paper
                score += 3
            elif them == 'A': # Rock
                score += 6
        else: # Scissors
            score += 3
            if them == 'C': # Scissors
                score += 3
            elif them == 'B': # Paper
                score += 6
print(score)