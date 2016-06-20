# expand

> Convert tabs to spaces.

- Convert tabs in each FILE to spaces, writing to standard output:

`expand {{FILE}}`

- Convert tabs to spaces, reading from standard input:

`expand`

- Do not convert tabs after non blanks:

`expand -i {{FILE}}`

- Have tabs NUMBER characters apart, not 8:

`expand -t={{NUMBER}} {{FILE}}`

- Use comma separated LIST of explicit tab positions:

`expand -t={{LIST}}`
