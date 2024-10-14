# takes a user checks it against all the other ones and spits out a user thats most similar 
#grabs all pairs of users and computes something and then jacarrd 
#!/Users/kassidywall/anaconda3/bin/python
import sys
import json
from collections import defaultdict

'''for line in sys.stdin:
    if line.strip():
        print(line)'''

outlet_word_counts = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    try:
        outlet, content = line.strip().split(':::')
    except ValueError as e:
        sys.stderr.write(f"Error processing line: {line.strip()} - {e}\n")
        continue

    words = content.split()

    for word in words:
        outlet_word_counts[outlet][word] += 1

for outlet, word_counts in outlet_word_counts.items():
    print(f"{outlet}:::{dict(word_counts)}")

