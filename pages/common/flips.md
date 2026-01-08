# flips

> Create and apply IPS and BPS patches.
> More information: <https://github.com/Alcaro/Flips>.

- Run Flips interactively:

`flips`

- Apply a patch to a file:

`flips --apply {{path/to/patch.bps}} {{path/to/source_file}} {{path/to/output_file}}`

- Create a patch from two files:

`flips --create {{path/to/original_file}} {{path/to/modified_file}} {{path/to/output_patch.bps}}`
