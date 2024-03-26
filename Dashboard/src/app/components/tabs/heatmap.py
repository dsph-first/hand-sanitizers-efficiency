# Imports
import os
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

# Suppress useless warning
os.environ["XDG_SESSION_TYPE"] = "x11"

# Get sample names from file paths
reports = glob("/students/2023-2024/master/hand_sanitizer/bracken/reports/*.breport")
reports.sort()


def read_samples(reports):
    """
    Read sample data from reports and merge them into a combined DataFrame.

    Args:
        reports (list): List of file paths to reports.

    Returns:
        tuple: A tuple containing a list of individual sample DataFrames and a combined DataFrame.
    """
    # Read relevant columns from each report into a list of DataFrames
    reads = [pd.read_csv(f, sep="\t")[["name", "new_est_reads"]] for f in reports]

    # Create an empty DataFrame to merge the read DataFrames
    combined_reads = pd.DataFrame()

    # Merge DataFrames pairwise based on the 'name' column
    for i in range(len(reads) - 1):
        if combined_reads.empty:
            combined_reads = reads[i]
        else:
            combined_reads = combined_reads.merge(
                right=reads[i],
                how="outer",
                left_on="name",
                right_on="name",
                suffixes=(f"_{i-1}", f"_{i}"),
            )

    return reads, combined_reads


# Call read_samples function to read and merge the samples
reads, combined_reads = read_samples(reports)


def format_dataframe(reads, combined_reads):
    """
    Format the combined DataFrame.

    Args:
        reads (list): List of individual sample DataFrames.
        combined_reads (DataFrame): Combined DataFrame of samples.

    Returns:
        DataFrame: Formatted combined DataFrame.
    """
    # Define column names for the combined DataFrame
    col_names = ["name"] + [f"Barcode_{i}" for i in range(1, len(reads))]
    # Set column names
    combined_reads = combined_reads.set_axis(col_names, axis="columns")
    # Fill NaN values with 0
    combined_reads = combined_reads.fillna(0)
    # Set 'name' column as index
    combined_reads = combined_reads.set_index("name")
    return combined_reads


# Call format_dataframe function to format the DataFrame
combined_reads = format_dataframe(reads, combined_reads)


def create_heatmap(combined_reads):
    """
    Create and display a heatmap of the combined reads.

    Args:
        combined_reads (DataFrame): Combined DataFrame of samples.
    """
    # Set seaborn theme and font scale
    sns.set_theme(font_scale=0.5)
    # Create a clustered heatmap using log-transformed data
    sns.clustermap(np.log(combined_reads + 1e-6), cmap="viridis", figsize=(15, 10))
    # Show the heatmap
    plt.show()


# Call create_heatmap function to display the heatmap
create_heatmap(combined_reads)
