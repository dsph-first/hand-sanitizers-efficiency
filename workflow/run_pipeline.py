import snakemake

snakefile_1 = "./rules/qc_merging.smk"
snakefile_2 = "./rules/classify.smk"

# Call snakemake
snakemake.snakemake(snakefile_1, use_conda=True,
                    cores=2, workdir='.')

snakemake.snakemake(snakefile_2, use_conda=True,
                    cores=4, workdir='.')
