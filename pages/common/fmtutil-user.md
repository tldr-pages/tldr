# fmtutil-user

> Manage TeX formats and Metafont bases for the current user.
> More information: <https://manned.org/fmtutil-sys>.

- Recreate all user format files:

`fmtutil-user --all`

- Create all missing user format files:

`fmtutil-user --missing`

- Recreate a specific user format:

`fmtutil-user --byfmt {{format}}`

- Recreate all formats built with a specific engine:

`fmtutil-user --byengine {{engine}}`

- List all available format configurations:

`fmtutil-user --listcfg`
