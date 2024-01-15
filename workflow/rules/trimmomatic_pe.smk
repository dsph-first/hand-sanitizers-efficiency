rule trimmomatic_pe:
    input:
        get_input_files
    output:
        generate_output_files
    log:
        os.path.join(config['log_path'], "/{sample}.log")
    params:
        # list of trimmers (see manual)
        trimmer=config["trimming_rule"]["list_trimmers"],
        # optional parameters
        extra="",
        compression_level="-9"
    threads:
        config["trimmomatic_pe_rule"]["threads"]
    resources:
        mem_mb=config["trimmomatic_pe_rule"]["mem_mb"]
    wrapper:
        "v3.3.3/bio/trimmomatic/pe"