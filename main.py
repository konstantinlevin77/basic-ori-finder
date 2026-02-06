import fetch_parse_fasta
import skew_functions

# Fetches the .fasta file from NCBI database for the T. pallidum genome
fetch_parse_fasta.fetch_fasta_from_ncbi("NC_000919.1")

genome = fetch_parse_fasta.parse_fasta("NC_000919.1")

skew_matrix = skew_functions.generate_skew_matrix(genome)
ori_window = skew_functions.approximate_ori_window(skew_matrix=skew_matrix)

print("Possible oriC window for T. pallidum starts at index:{} and ends at index:{}".format(ori_window[0],ori_window[1]))
