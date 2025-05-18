# reuse

> Tool for compliance with the REUSE recommendations.
> More information: <https://reuse.readthedocs.io/en/stable/man/index.html>.

- Lint for REUSE compliance for the current project (version control aware):

`reuse lint`

- Lint for REUSE compliance from the specified directory:

`reuse --root {{path/to/directory}} lint`

- Download a license by its SPDX identifier and place it in the LICENSES directory:

`reuse download {{spdx-identifier}}`

- Download all missing licenses detected in the project:

`reuse download --all`
