import urllib.request
import os
import time

import urllib.request
import os
import time

def fetch_fasta_from_ncbi(accession: str, save_dir:str = "genomes"):
    """
    Fetches the genome sequence from NCBI database, saves the genome sequence to
    genomes folder.
    
    accession: accession ID of the genome sequence
    save_dir: folder to save the genome sequence in .fasta format, defaults to genomes folder.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    file_path = os.path.join(save_dir, f"{accession}.fasta")
    
    # 1. Construct the REST API URL
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = f"?db=nuccore&id={accession}&rettype=fasta&retmode=text"
    url = base_url + params
    
    # 2. Download the file
    print(f"Fetching {accession} from NCBI...")
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Successfully saved to {file_path}")
        
        time.sleep(0.5) 
        
    except Exception as e:
        print(f"Error downloading {accession}: {e}")
    

def parse_fasta(accession: str, save_dir:str = "genomes") -> str:
    """
    Parses the .fasta file and returns the genome sequence as str.
    
    accession: accession ID of the genome sequence in NCBI database
    save_dir: where the .fasta file for the corresponding sequence saved, defaults to genomes
    """
    content = ""

    try:
        with open(save_dir+"/"+accession+".fasta","r") as f:
            content = f.read()
            content = content.split("\n")
            content = content[1:]
            content = "".join(content)
    except Exception as e:
        print("Parsing .fasta file failed:",e)

    return content

