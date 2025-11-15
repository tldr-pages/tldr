# vgs

> Display information about volume groups.
> See also: `lvm`.
> More information: <https://manned.org/vgs>.

- Display information about volume groups:

`sudo vgs`

- Display all volume groups:

`sudo vgs {{[-a|--all]}}`

- Change default display to show more details:

`sudo vgs {{[-v|--verbose]}}`

- Display only specific fields:

`sudo vgs {{[-o|--options]}} {{field_name_1}},{{field_name_2}}`

- Append field to default display:

`sudo vgs {{[-o|--options]}} +{{field_name}}`

- Suppress heading line:

`sudo vgs --noheadings`

- Use separator to separate fields:

`sudo vgs --separator =`
