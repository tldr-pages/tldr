# restorecon

> Restore SELinux security context on files/directories according to persistent rules.
> See also: `semanage-fcontext`.
> More information: <https://manned.org/restorecon>.

- View the current security context of a file or directory:

`ls -dlZ {{path/to/file_or_directory}}`

- Restore the security context of a file or directory:

`restorecon {{path/to/file_or_directory}}`

- Restore the security context of a directory recursively, and show all changed labels:

`restorecon -R -v {{path/to/directory}}`

- Restore the security context of a directory recursively, using all available threads, and show progress:

`restorecon -R -T {{0}} -p {{path/to/directory}}`

- Preview the label changes that would happen without applying them:

`restorecon -R -n -v {{path/to/directory}}`
