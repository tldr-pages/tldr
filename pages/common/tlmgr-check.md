# tlmgr check

> Check the consistency of a TeX Live installation.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Check the consistency of the whole TeX Live installation:

`tlmgr check all`

- Check the consistency of the whole TeX Live information in verbose mode:

`tlmgr check all -v`

- Check for missing dependencies:

`tlmgr check depends`

- Check if all TeX Live executables are present:

`tlmgr check executes`

- Check if all files listed in the local TLPDB are present:

`tlmgr check files`

- Check for duplicate filenames in the runfiles sections:

`tlmgr check runfiles`
