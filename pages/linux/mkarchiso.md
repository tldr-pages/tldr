# mkarchiso

> Build Arch Linux ISO images from an archiso profile.
> More information: <https://manned.org/mkarchiso>.

- Build an ISO from the official `releng` profile (copy it somewhere else first to customize it):

`sudo mkarchiso -v {{/usr/share/archiso/configs/releng}}`

- Build an ISO with custom working and output directories:

`sudo mkarchiso -v -w {{path/to/work_directory}} -o {{path/to/output_directory}} {{path/to/profile}}`

- Build an ISO and delete the working directory afterwards:

`sudo mkarchiso -r -o {{path/to/output_directory}} {{path/to/profile}}`

- Build a bootstrap tarball and netboot artifacts instead of an ISO:

`sudo mkarchiso -m "{{bootstrap netboot}}" {{path/to/profile}}`

- Set the volume label, publisher, and application name of the ISO:

`sudo mkarchiso -L {{label}} -P "{{publisher}}" -A "{{application}}" {{path/to/profile}}`

- Install additional packages into the image:

`sudo mkarchiso -p "{{package1 package2 ...}}" {{path/to/profile}}`

- Display help:

`mkarchiso -h`
