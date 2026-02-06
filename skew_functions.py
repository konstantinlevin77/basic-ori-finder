
def generate_skew_matrix(genome: str, skew_type: str="GC") -> list[int]:
    """
    Generates the skew matrix.
    
    Args:
        genome: genome sequence
        skew_type: defaults to GC, AT is also possible.
    
    Returns:
        a list representing the skew matrix
    """
    skew_matrix = [0]
    n = len(genome)

    increasing = ""
    decreasing = ""

    if skew_type == "AT":
        increasing = "A"
        decreasing = "T"
    elif skew_type == "GC":
        increasing = "G"
        decreasing = "C"
    else:
        raise Exception("Skew type unidentified. Available skew types: GC (default), AT")


    for base in genome:
        if base == increasing:
            skew_matrix.append(skew_matrix[-1] + 1)
        elif base == decreasing:
            skew_matrix.append(skew_matrix[-1] - 1)
        else:
            skew_matrix.append(skew_matrix[-1])
    
    return skew_matrix

def approximate_ori_window(skew_matrix: list[int]) -> tuple[int,int]:
    
    n = len(skew_matrix) - 1
    min_val = min(skew_matrix)
    first_occurence = 0
    # There might be a handful of the same min value 
    # but this function takes the first occurence into account
    for i in range(len(skew_matrix)):
        if skew_matrix[i] == min_val:
            first_occurence = i
            break
    
    """
    Experimentally confirmed, most bacteria genome have a oriC sequence around 250 to 500 base pairs
    For a computational approach I choose a wider window to begin with.
    """
    WINDOW_WIDTH = 1500
    return ((first_occurence - WINDOW_WIDTH//2) % n , (first_occurence + WINDOW_WIDTH//2) % n)


def get_window_sequence(genome: str, start: int, end: int) -> str:
    """
    Returns the sequence from the circular genome for the given start and end indices.
    """
    if start < end:
        return genome[start:end]
    else:
        seq = ""
        seq += genome[start:]
        seq += genome[:end]
        return seq
    

