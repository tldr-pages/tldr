# tlmgr option

> TeX Live settings manager.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all TeX Live settings:

`tlmgr option showall`

- List all currently set Tex Live settings:

`tlmgr option show`

- Print all TeX Live settings in JSON format:

`tlmgr option showall --json`

- Show the value of a specific TeX Live setting:

`tlmgr option {{setting}}`

- Modify the value of a specific TeX Live setting:

`tlmgr option {{setting}} {{value}}`

- Set TeX Live to get future updates from the internet after installing from DVD:

`tlmgr option {{repository}} {{https://mirror.ctan.org/systems/texlive/tlnet}}`
