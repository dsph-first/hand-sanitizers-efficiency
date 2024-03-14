"""Bracken rule
Post classification bayesian normalisation tool for kraken2 
output on analysis of 16s DNA
sequenicing runs. Database can be specified in the:
    config/config_sample.yaml

Intended to be used:

- classification normalisation of kraken2 reports

rule author:
    J. Gray

version:
    v0.01

tool_website:
    https://github.com/jenniferlu717/Bracken

tool_publication:
    Lu J, Breitwieser FP, Thielen P, Salzberg SL. (2017) 
    Bracken: estimating species abundance in metagenomics data. 
    PeerJ Computer Science 3:e104,
    doi:10.7717/peerj-cs.104 
"""

rule bracken:
    input:
        "{sample}.kreport"
    output:
        "{sample}.breport"
    params:
        database=config["kraken_db"],
        readlength=1600,
    conda: "kraken2"
    shell:
        """bracken \
        --db {params.database} \
        -r {params.readlength} \
        -i {input} \
        -o {output} \
        """
