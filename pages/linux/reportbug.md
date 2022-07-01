# reportbug

> Bug report tool of Debian distribution.
> More information: <https://manpages.debian.org/latest/reportbug/reportbug.html>.

- Generate a bug report about a specific package, then send it by e-mail:

`reportbug {{package}}`

- Report a bug that is not about a specific package (general problem, infrastructure, etc.):

`reportbug other`

- Write the bug report to a file instead of sending it by e-mail:

`reportbug -o {{filename}} {{package}}`
