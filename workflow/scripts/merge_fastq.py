#!/usr/bin/env python3
from os import system, walk
import os.path
from sys import argv, exit

# Function to get the file structure
def get_file_structure(path):
    passed_barcodes = []
    for root, dir, _ in walk(path):
        if root.endswith("/pass"):
            for barcode in dir:
                if barcode.startswith("barcode"):
                    barcode_path = os.path.join(root, barcode)
                    passed_barcodes.append(barcode_path)
    return passed_barcodes

# Function to check the existance of the output directory
def check_output_directory(output_folder):
    if os.path.isdir(output_folder):
        pass
    else:
        exit("[ERROR] - No output folder specified...")

# Function to concatenate files
def concat_files(barcodes, output_folder):
    check_output_directory(output_folder)
    for barcode_path in barcodes:
        barcode = barcode_path.split('/')[-1]
        # Concatenation command
        CONCAT_COMMAND = f"cat {barcode_path}/*.fastq > {output_folder}/{barcode}.fastq"
        print("running the following command:")
        print(CONCAT_COMMAND)
        system(CONCAT_COMMAND)
    return

# Main function
def main(args):
    files_path = args[0]
    output_folder = args[1]
    output_folder = os.path.join(files_path, output_folder)
    files_per_barcode = get_file_structure(files_path)
    concat_files(files_per_barcode, output_folder)

# If the script is run directly (not imported)
if __name__ == "__main__":
    if len(argv) > 0:
        args = argv[1:]
        main(args)
    else:
        exitcode = """Usage: merge_fastq.py [directory of nanopore fastq reads] [output directory to write to]"""
        exit(exitcode)