# lvs

> Display information about logical volumes.
> See also: `lvm`.
> More information: <https://manned.org/lvs>.

- Display information about logical volumes:

`lvs`

- Display all logical volumes:

`lvs -a`

- Change default display to show more details:

`lvs -v`

- Display only specific fields:

`lvs -o {{field_name_1}},{{field_name_2}}`

- Append field to default display:

`lvs -o +{{field_name}}`

- Suppress heading line:

`lvs --noheadings`

- Use a separator to separate fields:

`lvs --separator {{=}}`
