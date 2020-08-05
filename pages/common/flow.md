# flow

> A static type checker for javascript. 
> More information: <https://flow.org/en/>.

- Run flow check:

`flow`

- Check which files are being checked by flow:

`flow ls`

- Run type coverage check on all files in a directory:

`flow batch-coverage  --show-all --strip-root {{frontend_js_dir}}`

- Print out the line-by-line stats on type coverage:

`flow coverage --color {{file.jsx}}`

