import matplotlib.pyplot as plt

def generate_skew_plot(skew_matrix: list[int], skew_type: str="GC"):
    """
    Generates the skew plot of the given skew matrix.
    """
    plt.plot(skew_matrix)
    plt.xlabel("{} Skew Matrix".format(skew_type))
    plt.show()