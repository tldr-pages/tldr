# chcon

> Change SELinux security context of a file or files/directories.
> More information: <https://www.gnu.org/software/coreutils/chcon>.

- View security context of a file:

`ls -lZ {{path/to/file}}`

- Change the security context of a target file, using a reference file:

`chcon --reference={{path/to/file}} {{path/to/file}}`

- Change the full SELinux security context of a file:

`chcon {{user}}:{{role}}:{{type}}:{{range/level}} {{path/to/file}}`

- Change only the user part of SELinux security context:

`chcon -u {{user}} {{path/to/file}}`

- Change only the role part of SELinux security context:

`chcon -r {{role}} {{path/to/file}}`

- Change only the type part of SELinux security context:

`chcon -t {{type}} {{path/to/file}}`

- Change only the range/level part of SELinux security context:

`chcon -l {{range/level}} {{path/to/file}}`
