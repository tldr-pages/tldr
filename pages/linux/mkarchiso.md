# mkarchiso

> Build Arch Linux ISO images from an archiso profile.
> More information: <https://manned.org/mkarchiso>.

- Build an ISO from the official `releng` profile:

`mkarchiso -v /usr/share/archiso/configs/releng`

- Build an ISO with custom working and output directories:

`mkarchiso -v -w {{path/to/work_directory}} -o {{path/to/output_directory}} {{path/to/profile_directory}}`

- Build an ISO and delete the working directory afterwards:

`mkarchiso -r -o {{path/to/output_directory}} {{path/to/profile_directory}}`

- Build a bootstrap tarball and netboot artifacts instead of an ISO:

`mkarchiso -m "{{bootstrap netboot}}" {{path/to/profile_directory}}`

- Set the volume label, publisher, and application name of the ISO:

`mkarchiso -L {{label}} -P "{{publisher}}" -A "{{application}}" {{path/to/profile_directory}}`

- Install additional packages into the image:

`mkarchiso -p "{{package1 package2 ...}}" {{path/to/profile_directory}}`

- Display help:

`mkarchiso -h`
