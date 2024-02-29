"""kraken2 rule
Classification tool for metagenomic analysis of 16s DNA
sequenicing runs. Database can be specified in the:
    config/config_sample.yaml

Intended to be used:

- post trimming
- classification of microbial families, species, strains

rule author:
    J. Gray

version:
    v0.01

tool_website:
    https://ccb.jhu.edu/software/kraken2/

tool_publication:
    Wood, D.E., Lu, J. & Langmead, 
    B. Improved metagenomic analysis with Kraken 2.
    Genome Biol 20, 257 (2019).
    https://doi.org/10.1186/s13059-019-1891-0

"""

rule kraken2:
    ## TODO inputs and outputs need to be specified
    input:
        "{sample.fastq}"
    output:
        classified="",
        unclassified="",
        report=""
    params:
        database=config["kraken_db"]
    conda: "../envs/kraken2.yaml"
    threads: 32
    shell:
        """kraken2 \
        --threads {threads} \
        --db {params.database} \
        --classified-out {output.classified} \
        --unclassified-out {output.unclassified} \
        --output {output.report} \
        {input}
        """