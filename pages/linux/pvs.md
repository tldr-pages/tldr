# pvs

> Display information about physical volumes.
> One of the Logical Volume Manager (LVM) tools.
> More information: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes/>.

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
