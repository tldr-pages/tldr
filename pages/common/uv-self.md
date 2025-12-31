# uv self

> Manage the `uv` executable itself.
> More information: <https://docs.astral.sh/uv/reference/cli/#uv-self>.

- Update `uv` to the latest version:

`uv self update`

- Update `uv` to a specific version:

`uv self update {{0.4.0}}`

- Check for available `uv` updates without installing:

`uv self update --dry-run`

- Update `uv` with verbose output:

`uv self update {{[-v|--verbose]}}`

- Display the current `uv` version:

`uv self version`

- Display only the version number:

`uv self version --short`

- Display version information in JSON format:

`uv self version --output-format json`
