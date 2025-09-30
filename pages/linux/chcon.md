# chcon

> Change SELinux security context of a file or files/directories.
> See also: `secon`, `restorecon`, `semanage-fcontext`.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- View security context of a file:

`ls {{[-lZ|-l --context]}} {{path/to/file}}`

- Change the security context of a target file, using a reference file:

`chcon --reference {{reference_file}} {{target_file}}`

- Change the full SELinux security context of a file:

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{filename}}`

- Change only the user part of SELinux security context:

`chcon {{[-u|--user]}} {{user}} {{filename}}`

- Change only the role part of SELinux security context:

`chcon {{[-r|--role]}} {{role}} {{filename}}`

- Change only the type part of SELinux security context:

`chcon {{[-t|--type]}} {{type}} {{filename}}`

- Change only the range/level part of SELinux security context:

`chcon {{[-l|--range]}} {{range/level}} {{filename}}`
