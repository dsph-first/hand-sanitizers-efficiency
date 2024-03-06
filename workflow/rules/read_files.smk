import glob
import os


number_of_folder = 1000
number_of_files = 10000

def get_fastq_files():
    fastq_files = []
    for i in range(1, 3):
        folder_path = f"folder/folder_{i}"
        for fastq_file in glob.glob(f"{folder_path}/*.fastq"):
            folder_name = os.path.basename(folder_path)
            file_name = os.path.basename(fastq_file).replace('.fastq', '')
            fastq_files.append((folder_name, file_name))
    return fastq_files

rule read_files:
    input:
        expand("processed/folder_{folder_id}/{file}.processed.fastq", folder_id=range(1, Number_of_folder+1), file=[f"barcode{i}" for i in range(1, number_of_files+1)])


rule process_fastq:
    input:
        "example_folder/{folder}/{file}.fastq"
    output:
        "processed/{folder}/{file}.processed.fastq"
    shell:
        """
        mkdir -p $(dirname {output})
        echo "Now processing {input}" > {output}
        """