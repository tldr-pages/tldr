# pvs

> Display information about LVM physical volumes.
> More information: <https://www.man7.org/linux/man-pages/man8/pvs.8.html>.

- Display information about physical volumes:

`pvs`

- Display non-physical volumes:

`pvs -a`

- Change default display to show more details:

`pvs -v`

- Display only specific fields:

`pvs -o {{field_name_1}},{{field_name_2}}`

- Append field to default display:

`pvs -o +{{field_name}}`

- Suppress heading line:

`pvs --noheadings`

- Use separator to separate fields:

`pvs --separator {{special_character}}`
