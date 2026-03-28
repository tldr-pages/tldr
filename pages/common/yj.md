# yj

> Convert between YAML, TOML, JSON, and HCL, preserving map order.
> More information: <https://github.com/sclevine/yj>.

- Convert [y]AML to JSON (default) from `stdin` and write the result to `stdout`:

`yj  < {{file.yml}} -y`

- Convert [t]OML to [y]AML:

`yj < {{file.toml}} -ty`

- Convert [j]SON to [t]OML with [i]ndentation:

`yj < {{file.json}} -jti`

- Convert H[c]L to [j]SON:

`yj < {{file.hcl}} -cj`

- Convert [y]AML to H[c]L ignoring inf/[n]aN conversion:

`yj < {{file.yml}} -ycn`

- Display [v]ersion:

`yj -v`
