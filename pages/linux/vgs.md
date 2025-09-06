# vgs

> Display information about volume groups.
> See also: `lvm`.
> More information: <https://manned.org/vgs>.

- Display information about volume groups:

`vgs`

- Display all volume groups:

`vgs {{[-a|--all]}}`

- Change default display to show more details:

`vgs {{[-v|--verbose]}}`

- Display only specific fields:

`vgs {{[-o|--options]}} {{field_name_1}},{{field_name_2}}`

- Append field to default display:

`vgs {{[-o|--options]}} +{{field_name}}`

- Suppress heading line:

`vgs --noheadings`

- Use separator to separate fields:

`vgs --separator =`
