# yj

> Convert between YAML, TOML, JSON, and HCL, preserving map order.
> More information: <https://github.com/sclevine/yj>.

- Convert YAML to JSON (default) from `stdin` and write the result to `stdout`:

`yj -y < {{file.yml}}`

- Convert TOML to YAML:

`yj -ty < {{file.toml}}`

- Convert JSON to TOML with indentation:

`yj -jti < {{file.json}}`

- Convert HCL to JSON:

`yj -cj < {{file.hcl}}`

- Convert YAML to HCL ignoring inf/NaN conversion:

`yj -ycn < {{file.yml}}`

- Display version:

`yj -v`
