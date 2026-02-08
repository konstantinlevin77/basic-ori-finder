import fetch_parse_fasta
import skew_functions
import util_functions
import pattern_matching


#fetch_parse_fasta.fetch_fasta_from_ncbi("NC_000913.3")

genome = fetch_parse_fasta.parse_fasta("NC_000913.3")
print("Length of the genome: {}".format(len(genome)))
print("Generating skew matrix.")
skew_matrix = skew_functions.generate_skew_matrix(genome)
print("Approximationg ori window")
ori_window = skew_functions.approximate_ori_window(skew_matrix=skew_matrix)


print("Possible oriC window for E. coli starts at index:{} and ends at index:{}".format(ori_window[0],ori_window[1]))

print(pattern_matching.find_most_frequent_9mers(genome,ori_window))