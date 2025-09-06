# pvs

> Display information about physical volumes.
> See also: `lvm`.
> More information: <https://manned.org/pvs>.

- Display information about physical volumes:

`pvs`

- Display non-physical volumes:

`pvs {{[-a|--all]}}`

- Change default display to show more details:

`pvs {{[-v|--verbose]}}`

- Display only specific fields:

`pvs {{[-o|--options]}} {{field_name_1}},{{field_name_2}}`

- Append field to default display:

`pvs {{[-o|--options]}} +{{field_name}}`

- Suppress heading line:

`pvs --noheadings`

- Use separator to separate fields:

`pvs --separator {{special_character}}`
