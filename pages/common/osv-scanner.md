# osv-scanner

> Scan various mediums for dependencies and matches them against the OSV database.
> More information: <https://osv.dev/about>.

- Scan a docker image:

`osv-scanner -D {{docker_image_name}}`

- Scan a package lockfile:

`osv-scanner -L {{path/to/lockfile}}`

- Scan an SBOM file:

`osv-scanner -S {{path/to/sbom_file}}`

- Scan multiple directories recursively:

`osv-scanner -r {{directory1 directory2 ...}}`

- Skip scanning git repositories:

`osv-scanner --skip-git {{-r|-D}} {{target}}`

- Output result in JSON format:

`osv-scanner --json {{-D|-L|-S|-r}} {{target}}`
