# scores.py  (MAIN) - calculates Sum and Average
import sys

# Default scores
default_scores = [50, 60, 70]

# If a single parameter is passed (scores as space-separated string)
if len(sys.argv) == 2:
    print("User provided scores:")
    text = sys.argv[1]
    scores = list(map(float, text.split()))
else:
    print("No parameter given — using default scores")
    scores = default_scores

total = sum(scores)
average = total / len(scores)

print("Scores  :", scores)
print("Sum     :", total)
print("Average :", average)
