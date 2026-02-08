import skew_functions
from collections import defaultdict
def find_reverse_complement(genome: str) -> str:
    
    compl_table = {"A":"T","C":"G","T":"A","G":"C"}
    rev_ = []
    for i in range(len(genome)):
        rev_.append(compl_table[genome[i]])
    return "".join(rev_)[::-1]


def find_all_9mers(genome: str,ori_window: tuple[int,int]) -> defaultdict[str,int]:
    # This function takes reverse complement into account

    genome =  skew_functions.get_window_sequence(genome,ori_window[0],ori_window[1])

    n = len(genome)
    reverse_complement = find_reverse_complement(genome)
    k = 9
    table = defaultdict(int)
    
    for i in range(n-k + 1):
        table[genome[i:i+9]] += 1
        table[reverse_complement[i:i+9]] += 1

    return table

def hamming_distance(a,b,k) -> bool:
    total = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            total += 1
    return total <= k


def find_most_frequent_9mers(genome: str,ori_window: tuple[int,int]) -> dict[str,int]:
    table = find_all_9mers(genome,ori_window)
    final_table = {}

    for key in table:
        final_table[key] = table[key]

    for key in table:
        for key2 in table:
            if key != key2:
                if hamming_distance(key,key2,1):
                    final_table[key] += table[key2]
                    final_table[key2] += table[key]
    
    if not final_table:
        return {}

    # 1. Sort the items by score in descending order
    # item[1] refers to the value (the score)
    sorted_patterns = sorted(final_table.items(), key=lambda item: item[1], reverse=True)

    # 2. Get the unique scores to find the "Top N" tiers
    # This ensures if there are ties, you see all patterns with that score
    unique_scores = sorted(list(set(final_table.values())), reverse=True)
    top_5_threshold_scores = unique_scores[:5] 

    # 3. Filter the results
    result_dict = {}
    for pattern, score in sorted_patterns:
        if score in top_5_threshold_scores:
            result_dict[pattern] = score
            
    return result_dict

    return result_dict


    
