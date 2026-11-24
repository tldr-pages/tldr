# apt purge

> Remove packages and their configuration files.
> Note: Does not remove user configurations stored in the home directory.
> More information: <https://manned.org/apt.8>.

- Remove a package and its configuration files:

`sudo apt purge {{package}}`

- Remove one or more packages and their configuration files:

`sudo apt purge {{package1 package2 ...}}`

- Remove a package along with its configuration files and unused dependencies:

`sudo apt purge --autoremove {{package}}`

- Simulate purging packages without making actual changes:

`apt purge {{[-s|--simulate]}} {{package}}`

- Automatically answer yes to all prompts during package removal:

`sudo apt purge {{[-y|--yes]}} {{package}}`
