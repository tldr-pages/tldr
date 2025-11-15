# setfiles

> Set SELinux file security contexts based on policy rules.
> Similar to `restorecon` but reads contexts from a file_contexts file.
> See also: `restorecon`, `semanage-fcontext`, `fixfiles`.
> More information: <https://manned.org/setfiles>.

- Set file contexts according to the default policy file:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}}`

- Set file contexts recursively and show changes:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}} {{[-v|--verbose]}}`

- Preview what would be changed without actually modifying contexts:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}} {{[-n|--nochange]}}`

- Set file contexts and verify them:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}} {{[-v|--verbose]}} {{[-F|--force]}}`

- Use a specific root path for context matching:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/new_directory}} {{[-r|--rootpath]}} {{path/to/old_directory}}`
