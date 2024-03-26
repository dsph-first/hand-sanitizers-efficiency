configfile: "config/config.yaml"


project_root = config["project_path"]

with open(config["samples"], "r") as f_in:
    SAMPLES = [file.strip() for file in f_in]


rule all:
    input:
        expand(
            project_root + config["krona_reports"] + "/{samples}.html", samples=SAMPLES
        ),


# MICROBIAL 16S CLASSIFICATION
rule kraken2:
    input:
        project_root + config["concatted_files"] + "/{samples}.fastq",
    output:
        report=project_root + config["kraken_reports"] + "/{samples}.kreport",
    params:
        database=project_root + config["kraken_db"],
        classified_out="/dev/null",
        unclassified_out="/dev/null",
    conda:
        config["kraken_conda"]
    threads: 4
    shell:
        """kraken2 \
        --threads {threads} \
        --db {params.database} \
        --use-names \
        --classified-out {params.classified_out} \
        --unclassified-out {params.unclassified_out} \
        --report {output.report} \
        {input} 1> /dev/null
        """


rule bracken:
    input:
        rules.kraken2.output,
    output:
        project_root + config["bracken_reports"] + "/{samples}.breport",
    params:
        database=project_root + config["kraken_db"],
        readlength=1600,
    conda:
        config["kraken_conda"]
    shell:
        """bracken \
        -d {params.database} \
        -r {params.readlength} \
        -i {input} \
        -o {output} \
        """


## BRACKEN REPORT VISUALISATION
rule krona:
    input:
        rules.bracken.output,
    output:
        project_root + config["krona_reports"] + "/{samples}.html",
    conda:
        config["krona_conda"]
    shell:
        """ktImportTaxonomy \
        -o {output} \
        {input}
        """
