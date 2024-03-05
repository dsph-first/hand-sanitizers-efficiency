# Colony count data analysis - DSPH
Analysis and visualization of colony count data from the fingerprint experiment

## Methods
- make graph
    - nested bar graph

- statistical test
    - testing for normality : Anderson-Darling
    - statistics : two-sample t-test or Mann-Whitney U

## Data
Excel file containing colony count data from the fingerprint experiment. Count data can be found in microsoft teams "transmission and hand sanitizer". I manually changed the names in the excel file containing the count data.

## Files
- requirements.txt contains the requirements.
- `visualization_analysis.ipynb` is a jupyter notebook containing the code to be executed.
    also contains improvements/todo 
- the folder `old` contains previous versions and also code to create mock data.

## How to use
1. Clone the repository
2. Obtain the data file
3. Ensure required dependencies are installed
4. Change the naming in the excel file

    HS1-1 HS1-2 HS1-3
    HS1-C1 HS1-C2 HS1-C3

    structure: HS1 is the identifier for the handsanitizer (can also be HS2 or HS3)
    followed by '-1' which denotes the number of the experiment (triplicates)
    '-1' is hand sanitizer and '-C1' is the corresponding control.

5. Adapt the file path in the notebook
6. excecute 