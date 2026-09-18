# fmtutil

> Manage TeX formats and Metafont bases.
> More information: <https://manned.org/fmtutil-sys>.

- Recreate all format files:

`fmtutil --all`

- Create all missing format files:

`fmtutil --missing`

- List available format configurations:

`fmtutil --listcfg`

- Recreate formats built with a specific engine:

`fmtutil --byengine {{engine}}`

- Recreate a specific format:

`fmtutil --byfmt {{format}}`
