#!/Users/kassidywall/anaconda3/bin/python
import sys
import json


def jaccard(set_A, set_B):
    intersection = len(set_A.intersection(set_B))
    union = len(set_A.union(set_B))
    return intersection / union if union != 0 else 0.0

for line in sys.stdin:
    line = line.strip()
    if line:
        data = json.loads(line)
        
        set_A = set(data['A_counts'].keys())
        set_B = set(data['B_counts'].keys())

        similarity = jaccard(set_A, set_B)
        del data['A_counts']
        del data['B_counts']
        data['similarity'] = similarity
        print(json.dumps(data))














'''        except json.JSONDecodeError as e:
            print(f"decoding JSON: {e}", file=sys.stderr)
        except Exception as e:
            print(f"different error: {e}", file=sys.stderr)'''




'''for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            data = json.loads(line) 
            print(data) 
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}", file=sys.stderr)'''

'''def jaccard(A,B):
    return len(A.intersection(B)) / len(A.union(B))


#should do the similarity 
for line in sys.stdin:
    #print(line)
    pairing = json.loads(line)
    set_A = set(pairing['A'].split())
    set_B = set(pairing['B'].split())
    similarity = jaccard(set_A, set_B)
    pairing['similarity'] = similarity #jaccard(set(pairing['A']), set(pairing['A']))
    print(json.dumps(pairing))'''