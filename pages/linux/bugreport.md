# bugreport

> File a bug report on Debian.
> More information: <https://manpages.debian.org/buster/reportbug/reportbug.1.en.html>.

- Generate a bug report about a specific package, then send it by e-mail:

`reportbug {{package}}`

- File a report about a package that does not exist yet (to request it, for example):

`reportbug wnpp`

- Report a bug that is not about a specific package (general problem, infrastructure, etc.):

`reportbug other`

- Write the bug report to a file instead of sending it by e-mail:

`reportbug -o {{filename}} {{package}}`
