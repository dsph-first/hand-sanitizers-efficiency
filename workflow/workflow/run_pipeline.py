import snakemake

snakefile_1 = "qc_merging.smk"
snakefile_2 = "classify.smk"

# Call snakemake
snakemake.snakemake(snakefile_1, use_conda=True,
                    cores=2, workdir='.')

snakemake.snakemake(snakefile_2, use_conda=True,
                    cores=4, workdir='.')