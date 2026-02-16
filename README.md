# Basic Ori Finder

## Problem Definition
In circular bacterial genomes, DNA replication begins at a specific location called the **origin of replication** ($oriC$). Identifying this region is a fundamental task in bioinformatics, as it helps us understand genome organization.

---

## Biological Background: The GC Skew
To locate $oriC$ computationally, this project follows a biological phenomenon known as **GC Skew**. 

### The Replication Asymmetry
DNA polymerase can only synthesize DNA in the $5' \to 3'$ direction. Because the two strands of the double helix are antiparallel, one strand (the **leading strand**) is synthesized continuously, while the other (the **lagging strand**) is synthesized in short bursts called **Okazaki fragments**.

While waiting for the replication fork to open, the lagging strand remains in a single-stranded state (ssDNA) for longer periods. This makes it significantly more vulnerable to mutations compared to the leading strand.

### The Deamination Process
The most critical mutation occurring in the ssDNA state is **deamination**:
* **Cytosine ($C$)** spontaneously loses an amino group and mutates into **Uracil ($U$)**.
* Since Uracil pairs with Adenine, DNA repair mechanisms often replace it with **Thymine ($T$)**.
* **The Result:** Over evolutionary time, the lagging strand sees a significant decrease in Cytosine and an increase in Thymine.

### Finding the Origin
Because of this asymmetric mutation rate, one side of the circular chromosome (from the origin to the terminus) becomes "G-rich," while the other becomes "C-rich." 

[Image of GC skew diagram in circular bacterial DNA]

* **The Switch Point:** The $oriC$ is typically found at the point where the $G-C$ difference **reverses its trend**. 
* **The Algorithm:** This project implements a sliding window algorithm to calculate the **cumulative skew** ($G - C$) across the genome. The $oriC$ is generally located at the **minimum** of this cumulative skew curve, where the lagging strand ends and the leading strand begins.

---