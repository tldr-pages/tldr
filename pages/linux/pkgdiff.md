# pkgdiff

> Compare the file contents of two Slackware packages.
> More information: <https://slackware.nl/slackware/slackware64-current/source/a/pkgtools/manpages/pkgdiff.8>.

- Compare two packages and display differences:

`pkgdiff {{path/to/package1.txz}} {{path/to/package2.txz}}`

- Compare two packages with colorized output:

`pkgdiff -c {{path/to/package1.txz}} {{path/to/package2.txz}}`

- Compare two packages and output a simple unified diff:

`pkgdiff -a {{path/to/package1.txz}} {{path/to/package2.txz}}`
