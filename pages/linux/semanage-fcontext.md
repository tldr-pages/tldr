# semanage fcontext

> Manage persistent SELinux security context rules on files/directories.
> See also: `semanage`, `matchpathcon`, `secon`, `chcon`, `restorecon`.
> More information: <https://manned.org/semanage-fcontext>.

- List all file labelling rules:

`sudo semanage fcontext --list`

- List all user-defined file labelling rules without headings:

`sudo semanage fcontext --list --locallist --noheading`

- Add a user-defined rule that labels any path which matches a PCRE regex:

`sudo semanage fcontext --add --type {{samba_share_t}} {{'/mnt/share(/.*)?'}}`

- Delete a user-defined rule using its PCRE regex:

`sudo semanage fcontext --delete {{'/mnt/share(/.*)?'}}`

- Relabel a directory recursively by applying the new rules:

`restorecon -R -v {{path/to/directory}}`
