# matchpathcon

> Lookup the persistent SELinux security context setting of a path.
> See also: `semanage-fcontext`, `secon`, `chcon`, `restorecon`.
> More information: <https://manned.org/man/matchpathcon.8>.

- Lookup the persistent security context setting of an absolute path:

`matchpathcon {{/path/to/file}}`

- Restrict lookup to settings on a specific file type:

`matchpathcon -m {{file|dir|pipe|chr_file|blk_file|lnk_file|sock_file}} {{/path/to/file}}`

- [V]erify that the persistent and current security context of a path agree:

`matchpathcon -V {{/path/to/file}}`
