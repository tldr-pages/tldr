# pnputil

> Manage the driver store and driver packages on Windows.
> Requires an elevated Command Prompt.
> More information: <https://learn.microsoft.com/windows-hardware/drivers/devtest/pnputil>

- List all the installed driver packages:

`pnputil /enum-drivers`

- Install the driver package from an INF file:

`pnputil /add-driver {{path\to\driver.inf}}`

- Add and install all the INF files in a folder:

`pnputil /add-driver {{path\to\folder\*.inf}} /subdirs`

- Delete the driver package using its published name:

`pnputil /delete-driver {{oemXX.inf}}`

- Install the driver package (using published name):

`pnputil /install-driver {{oemXX.inf}}`

- Export all the driver packages to a folder:

`pnputil /export-driver * {{path\to\folder}}`

- List all the devices:

`pnputil /enum-devices`
