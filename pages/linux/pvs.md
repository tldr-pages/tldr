# pvs

> Display information about physical volumes.
> See also: `lvm`.
> More information: <https://manned.org/pvs>.

- Display information about physical volumes:

`sudo pvs`

- Display non-physical volumes:

`sudo pvs {{[-a|--all]}}`

- Change default display to show more details:

`sudo pvs {{[-v|--verbose]}}`

- Display only specific fields:

`sudo pvs {{[-o|--options]}} {{field_name_1,field_name_2,...}}`

- Append field to default display:

`sudo pvs {{[-o|--options]}} +{{field_name}}`

- Suppress heading line:

`sudo pvs --noheadings`

- Use separator to separate fields:

`sudo pvs --separator {{special_character}}`
