# apt autoremove

> Remove packages that were automatically installed to satisfy dependencies and are no longer needed.
> More information: <https://manned.org/apt.8>.

- Remove all packages that were automatically installed and are no longer needed:

`sudo apt autoremove`

- Remove unused packages and delete their configuration files:

`sudo apt autoremove --purge`

- Remove a specific package and its unused dependencies:

`sudo apt autoremove {{package}}`

- Simulate removing packages without making actual changes:

`apt autoremove {{[-s|--simulate|--dry-run]}}`

- Automatically answer yes to all prompts during package removal:

`sudo apt autoremove {{[-y|--yes]}}`
