# nextflow

> Tool for running computational pipelines. Mostly used for bioinformatics workflows.
> Homepage: <https://www.nextflow.io>.

- Run a pipeline, use cached results from previous runs:

`nextflow run {{main.nf}} -resume`

- Run a specific release of a remote workflow from GitHub:

`nextflow run {{user/repo}} -revision {{release_tag}}`

- Run with a given work directory for intermediate files, save execution report:

`nextflow run {{workflow}} -work-dir {{/path/to/directory}} -with-report {{report.html}}`

- Show details of previous runs in current directory:

`nextflow log`

- Remove cache and intermediate files for a specific run:

`nextflow clean -force {{run_name}}`

- List all downloaded projects:

`nextflow list`

- Pull the latest version of a remote workflow from Bitbucket:

`nextflow pull {{user/repo}} -hub bitbucket`

- Update Nextflow:

`nextflow self-update`
