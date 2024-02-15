rule kraken2_analysis:
    input:
        config["trimmed_samples"]"{sample}_trimmed.fastq"
    output:
        report="./report/quantification/{sample}_kraken.report"
    params:
        db=config["kraken_db"]  # Path to Kraken database from config file
    log:
        "logs/kraken2/{sample}_kraken.log"
    shell:
        """
        kraken2 --db {params.db} --output {output.report} --report {output.report} {input} &> {log}
        """

rule bracken_analysis:
    input:
        "quantification/{sample}_kraken.report"
    output:
        "quantification/{sample}_bracken.report"
    params:
        db=config["bracken_db"],  # Path to Bracken database from config file
        kmer_length=config["bracken_kmer_length"]  # K-mer length used for Bracken
    log:
        "logs/bracken/{sample}_bracken.log"
    shell:
        """
        bracken -d {params.db} -i {input} -o {output} -k {params.kmer_length} &> {log}
        """