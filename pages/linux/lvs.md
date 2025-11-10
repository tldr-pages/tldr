# lvs

> Display information about logical volumes.
> See also: `lvm`.
> More information: <https://manned.org/lvs>.

- Display information about logical volumes:

`sudo lvs`

- Display all logical volumes:

`sudo lvs {{[-a|--all]}}`

- Change default display to show more details:

`sudo lvs {{[-v|--verbose]}}`

- Display only specific fields:

`sudo lvs {{[-o|--options]}} {{field_name_1}},{{field_name_2}}`

- Append field to default display:

`sudo lvs {{[-o|--options]}} +{{field_name}}`

- Suppress heading line:

`sudo lvs --noheadings`

- Use a separator to separate fields:

`sudo lvs --separator {{=}}`
