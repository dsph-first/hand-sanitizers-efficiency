rule krona:
    input:
        "braken_reports",
    output:
        "report.html",
    shell:
        "krona {input} {output}"
