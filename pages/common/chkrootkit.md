# chkrootkit

> Scan system for rootkits.
> More information: <https://manned.org/chkrootkit>.

- Enable [q]uiet mode and suppress normal test results:

`chkrootkit -q`

- Enable e[x]pert mode and produce additional outputs:

`chkrootkit -x`

- Enable [d]ebug mode to show all output:

`chkrootkit -d`

- Specify [e]xcluded files for some tests:

`chkrootkit -e "{{path/to/file}}"`

- Specify a directory as the [r]oot for testing (e.g. mounted `ext` drives):

`chkrootkit -r {{path/to/directory}}`

- Ignore [n]fs-mounted directories:

`chkrootkit -n`

- Invoke [T]ests and ignore specific filesystem types:

`chkrootkit -T {{filesystemtype}}`

- Generate [l]ist of available tests:

`chkrootkit -l`
