# pacreport

> Generate a report of installed packages, including unneeded dependencies, missing files, and cache sizes.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pacreport.pod>.

- Generate a summary of installed packages:

`pacreport`

- List unowned files:

`pacreport --unowned-files`

- List missing package files:

`pacreport --missing-files`

- Search for unmerged backup files (i.e. `.pacnew`, `.pacsave`) in `/etc`:

`pacreport --backups`

- Display packages in a specific group that are not currently installed:

`pacreport --group {{group_name}}`
