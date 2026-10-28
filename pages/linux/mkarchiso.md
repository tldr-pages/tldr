# mkarchiso

> Create Arch Linux ISO images, netboot artifacts, and bootstrap tarballs from a profile directory.
> More information: <https://man.archlinux.org/man/mkarchiso.1>.

- Build the ISO for the default `releng` profile:

`sudo mkarchiso /usr/share/archiso/configs/releng`

- Build from a specific profile directory:

`sudo mkarchiso {{path/to/profile_directory}}`

- Build into a specific output directory:

`sudo mkarchiso -o {{path/to/output_directory}} {{path/to/profile_directory}}`

- Build a specific type of artifact (bootstrap, iso, or netboot):

`sudo mkarchiso -m {{bootstrap|iso|netboot}} {{path/to/profile_directory}}`

- Set the ISO volume label:

`sudo mkarchiso -L {{label}} {{path/to/profile_directory}}`

- Use a specific `pacman` configuration file:

`sudo mkarchiso -C {{path/to/pacman.conf}} {{path/to/profile_directory}}`

- Delete the working directory when the build finishes:

`sudo mkarchiso -r {{path/to/profile_directory}}`

- Display help:

`mkarchiso -h`
