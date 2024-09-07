# secon

> Get the SELinux security context of a file, pid, current execution context, or a context specification.
> See also: `semanage`, `runcon`, `chcon`.
> More information: <https://manned.org/man/secon>.

- Get the security context of the current execution context:

`secon`

- Get the current security context of a process:

`secon --pid {{1}}`

- Get the current security context of a file, resolving all intermediate symlinks:

`secon --file {{path/to/file_or_directory}}`

- Get the current security context of a symlink itself (i.e. do not resolve):

`secon --link {{path/to/symlink}}`

- Parse and explain a context specification:

`secon {{system_u:system_r:container_t:s0:c899,c900}}`
