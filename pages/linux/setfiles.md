# setfiles

> Set SELinux file security contexts based on policy rules.
> Similar to `restorecon` but reads contexts from a file_contexts file.
> See also: `restorecon`, `semanage-fcontext`, `fixfiles`.
> More information: <https://manned.org/setfiles>.

- Set file contexts according to the default policy file:

`sudo setfiles /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}}`

- Set file contexts recursively and show changes:

`sudo setfiles {{[-v|--verbose]}} /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}}`

- Preview what would be changed without actually modifying contexts:

`sudo setfiles {{[-n|--nochange]}} /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}}`

- Set file contexts and verify them:

`sudo setfiles {{[-v|--verbose]}} {{[-F|--force]}} /etc/selinux/targeted/contexts/files/file_contexts {{path/to/directory}}`

- Use a specific root path for context matching:

`sudo setfiles {{[-r|--rootpath]}} {{/old/path}} /etc/selinux/targeted/contexts/files/file_contexts {{/new/path}}`
