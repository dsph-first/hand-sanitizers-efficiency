from snakemake.remote.NCBI import RemoteProvider as NCBIRemoteProvider
NCBI = NCBIRemoteProvider(email=confg["ncbi_user_address"])
import os


rule all:
    input:
        NCBI.remote("NC_045512.2.fasta", db="nuccore")
    run:
        outputName = os.path.basename("test.fasta")
        shell("mv {input} {outputName}")