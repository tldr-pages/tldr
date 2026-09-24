# pm list

> List users, packages, permissions, instrumentation, permission groups, features, and libraries managed by the package manager.
> More information: <https://developer.android.com/tools/adb#pm>.

- List all installed packages:

`pm list packages`

- List either [s]ystem or [3]rd-party packages:

`pm list packages {{-s|-3}}`

- Print all users on the system:

`pm list users`

- Print all known permission groups:

`pm list permission-groups`

- Print all known permissions:

`pm list permissions`

- List all test packages:

`pm list instrumentation`

- Print all features of the system:

`pm list features`

- Print all the libraries supported by the current device:

`pm list libraries`
