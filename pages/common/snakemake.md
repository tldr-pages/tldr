# snakemake

> Tool for running computational pipelines. Mostly used for bioinformatics workflows.
> More information: <https://snakemake.readthedocs.io/en/stable/executing/cli.html#all-options>.

- [F]orce-run entire pipeline, using all [c]ores, [k]eeping going even if job fails:

`snakemake --forceall --keep-going --cores all`

- Do a dry-ru[n], explicitly setting working [d]irectory and targe rule(s) or file(s):

`snakemake --dry-run --directory {{path/to/working_directory}} {{target_rule ...} {{target_file ...}}`

- Configure workflow using profile, configfile(s) and/or config key-value pairs:

`snakemake --profile {{path/to/profile}} --configfile {{path/to/configfile ...}} --config {{key_1}}={{value_1}} ...`

- Specify what triggers a rule rerun, changes to modification time [mtime], parameter changes [params], [input] data, [software-env]ironment and/or [code]:

`snakemake --rerun-triggers {{mtime,params,input,software-env,code}}`

- Force run one or more [R]ules and downstream, rerunning incomplete jobs without erro[ri]ng:

`snakemake --forcerun {{start_rule_1 ...}} --rerun-incomplete`

- [p]rint exact shell commands run for each job, with verbose output and execution stats:

`snakemake --printshellcmds --verbose --stats {{path/for/output/file}}`
