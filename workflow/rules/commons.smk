import fnmatch
import pandas as pd

# read sample sheet
samples = pd.read_csv(config["samples"], sep="\t").set_index(
    ["sample_name"], drop=False
)

# TODO
samples_length = 6

def get_fastq_input(inputdir):
    """
    FASTQ-files may end on 'fq', 'fastq' and have an
    additional suffix indicating a compression format
    """
    return [fname for fname in os.listdir(inputdir) if \
            fnmatch.fnmatch(fname, "*[\.fq|\.fastq]*")]


def generate_output_files(wildcards):
    output_files = []
    for i in range(1, samples_length):
        output_files.append(f"processed/{wildcards.sample}.{i}.processed")
    return output_files


def get_input_files(wildcards):
    file_paths = []
    for i in range(1, samples_length):
        path = f"results/{wildcards.sample}.{i}.fastq.gz"
        if os.path.exists(path):
            file_paths.append(path)
    return file_paths