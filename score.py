import sys

default_scores = [50, 60, 70]

if len(sys.argv) == 2 and sys.argv[1].strip() != "":
    print("User provided scores:")
    text = sys.argv[1]
    scores = list(map(float, text.split()))
else:
    print("No valid parameter given — using default scores")
    scores = default_scores

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("Scores  :", scores)
print("Sum     :", total)
print("Average :", average)
print("Maximum :", maximum)
print("Minimum :", minimum)
