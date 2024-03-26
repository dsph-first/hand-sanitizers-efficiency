## Install

`conda install -n base -c conda-forge mamba`

`mamba create -c conda-forge -c bioconda -n sanitizer snakemake`

`conda activate sanitizer`

## Usage:

`snakemake --snakefile Snakefile --config folder="/path/to/fastq" min_len=50 qc=10 -c 16 --use-conda`

### Requirements:

#### Porechope

Remove adaptors

Link[https://github.com/rrwick/Porechop]

`pip install git+https://github.com/rrwick/Porechop.git`

### Nanofilt

Trimming based on quality and length

https://github.com/wdecoster/nanofilt

### Centrifuge:

https://github.com/infphilo/centrifuge

git clone https://github.com/infphilo/centrifuge cd centrifuge make sudo make install prefix=/usr/local

##### Download database for Centrifuge:

https://data.mendeley.com/datasets/tt5ntb4zyv/1

`wget https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/tt5ntb4zyv-1.zip unzip tt5ntb4zyv-1.zip`

Write the path to the database in the file `../config/config.yaml`
`centrifuge_db: "/path/to/NCBI_202207"`
