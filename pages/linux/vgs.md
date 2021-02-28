# vgs

> Display information about volume groups.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes/index>.

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
