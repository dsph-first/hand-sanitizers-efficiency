configfile: "config/config.yaml"


project_root = config["project_path"]

with open(config["samples"], "r") as f_in:
    SAMPLES = [file.strip() for file in f_in]


## MAIN FUNCTION
rule all:
    input:
        # Quality control of sequencing run
        project_root + config["pycoqc_output_directory"] + "/sequencing_QC.html",
        # file merging directory
        project_root + config["concatted_files"],


## READ QUALITY CONTROL
rule pycoQC:
    input:
        project_root + config["sequencing_summary"],
    output:
        project_root + config["pycoqc_output_directory"] + "/sequencing_QC.html",
    params:
        name=config["pycoqc_report_name"],
    conda:
        config["pycoqc_conda"]
    shell:
        """
        pycoQC \
        --summary_file {input} \
        --html_outfile {output} \
        --report_title {params.name}
        """


## FASTQ FILE MERGING
rule merge_fastq_files:
    input:
        project_root + config["raw_reads"],
    output:
        directory(project_root + config["concatted_files"]),
    shell:
        """
        python3 \
        scripts/merge_fastq.py \
        {input} {output}
        """
