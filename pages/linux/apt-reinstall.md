# apt reinstall

> Reinstall packages for Debian-based distributions.
> More information: <https://manned.org/apt.8>.

- Reinstall one or more packages:

`sudo apt reinstall {{package1 package2 ...}}`

- Simulate reinstalling packages without making actual changes:

`apt reinstall {{[-s|--simulate]}} {{package}}`

- Automatically answer yes to all prompts during reinstallation:

`sudo apt reinstall {{[-y|--yes]}} {{package}}`

- Download package files without installing them:

`sudo apt reinstall {{[-d|--download-only]}} {{package}}`
