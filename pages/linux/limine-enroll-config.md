# limine-enroll-config

> Embed or reset the BLAKE2B hash of `limine.conf` in the Limine EFI executable.
> Used to ensure the configuration file has not been tampered with when Secure Boot is enabled.
> More information: <https://codeberg.org/Limine/Limine/src/branch/trunk/USAGE.md#secure-boot>.

- Embed a config file's BLAKE2B hash into the Limine EFI executable:

`limine-enroll-config {{path/to/BOOTX64.EFI}} {{blake2b_hash}}`

- Remove the enrolled hash from the executable, disabling the config integrity check:

`limine-enroll-config --reset {{path/to/BOOTX64.EFI}}`

- Display help:

`limine-enroll-config --help`
