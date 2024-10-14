#!/Users/kassidywall/anaconda3/bin/python
import sys
import itertools
import json



all_outlets = []
counts_dict = {}

#with open('news_articles/outlet_output1/part-00000') as f:
#    for line in f:
for line in sys.stdin:
    line = line.strip()
    if line:
        outlet, counts_str = line.split(':::')
        counts = json.loads(counts_str.replace("'", "\"")) 
        all_outlets.append((outlet, counts))  

for outlet_A, counts_A in all_outlets:
    for outlet_B, counts_B in all_outlets:
        if outlet_A >= outlet_B: 
            continue
        pairing = {
            'A': outlet_A,
            'A_counts': counts_A,
            'B': outlet_B,
            'B_counts': counts_B
        }
        print(json.dumps(pairing))











'''WORKING all_outlets = []

#with open('news_articles/outlet_output1/part-00000') as f:
with open('news_articles/outlet_output1/part-00000') as f:
    for line in f:
        line = line.strip()
        if line:
            all_outlets.append(line)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    line = line.replace("'", '"')
    outlet, counts_str = line.split(':::')
    try:
        counts = json.loads(counts_str)
    except json.JSONDecodeError:
        print(f"Error processing line: {line}")
        continue

    combs = itertools.combinations(all_outlets, 2)
    for comb in combs:
        pairing = {'A': outlet, 'A_counts': counts, 'B': comb[0], 'B_counts': comb[1]}
        print(json.dumps(pairing))'''





'''word_counts = {}
with open('news_articles/outlet_output1/part-00000') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            outlet, counts = line.split(':::')
            word_counts[outlet] = json.loads(counts)
        except (ValueError, json.JSONDecodeError) as e:
            sys.stderr.write(f"Error processing line: {line}\n")
            continue

outlet_names = list(word_counts.keys())
combs = itertools.combinations(outlet_names, 2)

for comb in combs:
    outlet_a, outlet_b = comb
    pairing = {
        'A': {outlet_a: word_counts[outlet_a]},
        'B': {outlet_b: word_counts[outlet_b]}
    }
    print(json.dumps(pairing))'''






'''all_articles = []
with open('news_articles/output1/part-00000') as f:
    #all_articles = f.read().split('\n')
    for line in f : 
        line = line.strip()
        if line:
            all_articles.append(line)


for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    combs = itertools.combinations(all_articles, 2)
    for comb in combs:
        if comb[0] != line or not comb[1] or comb[0] == '\t':
            continue
        pairing = {'A': comb[0], 'B': comb[1]}
        print(json.dumps(pairing))'''
    
'''for line in sys.stdin:
    line = line.strip()
    if line:
        all_articles.append(line)'''