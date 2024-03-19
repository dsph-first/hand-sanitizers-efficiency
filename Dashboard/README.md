# Dashboard:
This is the dashboard to showcase the efficasy of non alcoholic hand sanitizer through different experiments visualisations.

# Installation:
1. At first, clone this repository using this command:
`git clone https://github.com/eshita53/Programming-2-Course-Assignment-Submission](https://github.com/dsph-first/hand-sanitizers-efficiency/new/dashboard/Dashboard`
2. Then go to the folder which contains the repository contents. `cd dsph-first/hand-sanitizers-efficiency/new/dashboard/Dashboard`
3. The next step is to configure your environment. The conda package manager is used in this tutorial. Please ensure that conda or Miniconda are properly installed and configured on your system. 
4. Run the following command inside the folder to create the environment. 
`conda env create -f environment.yaml`
5. Use the following command to activate the environment: 
`conda activate dashboard`
6. Before running the program please ensure you are in the `dashboard` environment.

# DataSets:
This dashboard currently using the fingerpad printing experiments data which is in `xls` format. Make a `data` folder and download the `fingerprinting.xlsx` file from the team and put this file into the
`data` folder.

# Configuaration File:
The paths to the datasets are contained in a `config.yaml` file. Please make sure the dataset location matches the location in the YAML file before running the file. This dashboard currently using the fingerpad 
printing experiments data. This datasets is in `xls` format. Download the `fingerprinting.xlsx` file from the team and put this file into the `data` folder.

# Files:
Apart from the configuration files,there are other files which are required for the dashboard. These files are described below:
`app.py`: This files holds the initilization of dash app.
`index.py`: This contains the whole layout of dashboard. 
`navigation_bar.py`: This file contains the layout of navigation bar.
`data_process.py`: This file load the data and process it for further analyzation. 
`counting_colony.py`: This file shows the visualization for colony counting test. It's the layout for colony counting tab.
`disk_diffusion.py`:  This file shows the visualization for disk diffusion test.It's the layout for disk diffusion tab. 
`full_workingindex.py`: This is the full working file of index.py before adding others tab 
`rs_seq.py`: This file shows the visualization for16 rs dna sequencing.It's the layout for that tab.
`statistics_analysis.py`: This files do all the statistical analysis for dashboard.
`user_perceptions.py`: This file shows the visualization for user perceptions. It's the layout for user perceptions tab.

# Run :
Go to the `dashboard` environment and run `python3 index.py`. There will be a running dash app in the localhost.






