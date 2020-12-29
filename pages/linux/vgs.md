# vgs

> Display information about LVM volume groups.
> More information: <https://man7.org/linux/man-pages/man8/vgs.8.html>.

- Display information about volume groups:

`vgs`

- Display all volume groups:

`vgs -a`

- Change default display to show more details:

`vgs -v`

- Display only specific fields:

`vgs -o {{field_name_1}},{{field_name_2}}`

- Append field to default display:

`vgs -o +{{field_name}}`

- Suppress heading line:

`vgs --noheadings`

- Use separator to separate fields:

`vgs --separator =`
