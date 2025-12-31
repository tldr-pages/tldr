# pnputil

> Manage the driver store and driver packages on Windows.
> Requires an elevated Command Prompt.
> More information: <https://learn.microsoft.com/windows-hardware/drivers/devtest/pnputil-command-syntax>.

- List all installed driver packages:

`pnputil /enum-drivers`

- Install a driver package from an INF file:

`pnputil /add-driver {{path\to\driver.inf}}`

- Add and install all INF files in a folder (including subdirectories):

`pnputil /add-driver {{path\to\folder\*.inf}} /subdirs`

- Delete a driver package using its published name:

`pnputil /delete-driver {{oemXX.inf}}`

- Install a driver package using its published name:

`pnputil /add-driver {{oemXX.inf}}`

- Export all driver packages to a folder:

`pnputil /export-driver * {{path\to\folder}}`

- List all devices:

`pnputil /enum-devices`
