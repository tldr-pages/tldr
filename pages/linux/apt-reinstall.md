# apt reinstall

> Reinstall packages in their current version.
> More information: <https://manned.org/apt.8>.

- Reinstall a package:

`sudo apt reinstall {{package}}`

- Reinstall one or more packages:

`sudo apt reinstall {{package1 package2 ...}}`

- Simulate reinstalling packages without making actual changes:

`apt reinstall {{[-s|--simulate|--dry-run]}} {{package}}`

- Automatically answer yes to all prompts during reinstallation:

`sudo apt reinstall {{[-y|--yes]}} {{package}}`

- Download package files without installing them:

`sudo apt reinstall {{[-d|--download-only]}} {{package}}`
