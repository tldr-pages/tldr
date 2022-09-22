# autoconf

> Generate configuration scripts to automatically configure software source code packages.
> More information: <https://www.gnu.org/software/autoconf>.

- Generate a configuration script from `configure.ac` (if present) or `configure.in` and save this script to `configure`:

`autoconf`

- Generate a configuration script from the specified template; output to stdout:

`autoconf {{template-file}}`

- Generate a configuration script from the specified template (even if the input file has not changed) and write the output to a file:

`autoconf --force --output={{outfile}} {{template-file}}`
