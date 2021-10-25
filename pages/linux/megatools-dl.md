# megatools-dl

> Download files from `mega.nz`.
> Part of the `megatools` suite.
> More information: <https://megatools.megous.com/man/megatools-dl.html>.

- Download files from a `mega.nz` link into the current directory:

`megatools-dl {{https://mega.nz/...}}`

- Download files from a `mega.nz` link into a specific directory:

`megatools-dl --path {{path/to/directory}} {{https://mega.nz/...}}`

- Interactively choose which files to download:

`megatools-dl --choose-files {{https://mega.nz/...}}`

- Limit the download speed in KiB/s:

`megatools-dl --limit-speed {{speed}} {{https://mega.nz/...}}`
