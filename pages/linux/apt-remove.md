# apt remove

> Remove packages for Debian-based distributions.
> More information: <https://manned.org/apt.8>.

- Remove one or more packages:

`sudo apt remove {{package1 package2 ...}}`

- Remove one or more packages and their configuration files:

`sudo apt remove --purge {{package1 package2 ...}}`

- Remove packages and automatically remove unused dependencies:

`sudo apt remove --autoremove {{package1 package2 ...}}`

- Automatically answer yes to all prompts during package removal:

`sudo apt remove {{[-y|--yes]}} {{package}}`

- Simulate removing packages without making actual changes:

`apt remove {{[-s|--simulate]}} {{package}}`
