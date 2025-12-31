# pathchk

> Check the validity and portability of pathnames.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/pathchk-invocation.html>.

- Check pathnames for validity in the current system:

`pathchk {{path1 path2 ...}}`

- Check pathnames for validity on a wider range of POSIX compliant systems:

`pathchk -p {{path1 path2 ...}}`

- Check pathnames for validity on all POSIX compliant systems:

`pathchk {{[-p -P|--portability]}} {{path1 path2 ...}}`

- Only check for empty pathnames or leading dashes (-):

`pathchk -P {{path1 path2 ...}}`
