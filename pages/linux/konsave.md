# konsave

> A CLI program that will let you save and apply your Linux customizations with just one command!
> More information: <https://github.com/Prayag2/konsave>.


- Save current configuration as a profile:

`konsave --save <profile name>`

- Apply a profile:

`konsave --apply <profile name>`

- Overwrite an already saved profile:

`konsave -s <profile name> --force`

- List all profiles:

`konsave --list`

- Remove a profile:

`konsave --remove <profile name>`

- Export a profile as a ".knsv":

`konsave --export-profile <profile name>`


- Import a ".knsv" file:

`konsave --import-profile <path to the file>`
