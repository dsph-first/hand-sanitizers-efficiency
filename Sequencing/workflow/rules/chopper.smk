from os.path import join
"""Chopper rule
Filtering on quality and/or read length, and optional
trimming after passing filters. Reads from stdin,
writes to stdout. Optionally reads directly from an
uncompressed file specified on the command line.

Intended to be used:

- directly after fastq extraction
- prior to mapping
- in a stream between extraction and mapping

author:
    J. Gray

version:
    v0.01

tool_website:
    https://github.com/wdecoster/chopper

tool_publication:
    Wouter De Coster, Rosa Rademakers, NanoPack2:
    population-scale evaluation of long-read sequencing data,
    Bioinformatics, Volume 39, Issue 5, May 2023, btad311,
    https://doi.org/10.1093/bioinformatics/btad311

"""


rule chopper:
    input:
        "{sample}.fastq"
    params:
        # Overwriting default values using a lower phred-score 0 --> 10
        phred_score=9,
        # Overwriting default value of mininimum length from 500 --> 100
        minimum_length=100
    log:
        join(config["log_location"], "chopper_{sample}.log")
    output:
        join(config["output_location"], "{sample}_filt.fastq")
    threads:
        16
    conda:
        "../envs/chopper.yaml"
    message:
        "Executing chopper on: {input} using {threads} threads"
    shell:
        """chopper --threads {threads} \
        -q {params.phred_score} \
        -l {params.minimum_length} \
        {input} > {output}
        """
