# yj

> Convert between YAML, TOML, JSON, and HCL, preserving map order.
> More information: <https://github.com/sclevine/yj>.

- Convert YAML to JSON (default) from `stdin` and write the result to `stdout`:

`yj  < {{file.yml}} -y`

- Convert TOML to YAML:

`yj < {{file.toml}} -ty`

- Convert JSON to TOML with indentation:

`yj < {{file.json}} -jti`

- Convert HCL to JSON:

`yj < {{file.hcl}} -cj`

- Convert YAML to HCL ignoring inf/NaN conversion:

`yj < {{file.yml}} -ycn`

- Display version:

`yj -v`
