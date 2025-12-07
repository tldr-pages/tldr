# pivot_root

> Change the root filesystem to a new directory and move the current root to a subdirectory of the new root.
> Commonly used during system initialization (e.g., in initramfs) to switch from a temporary root to the real root filesystem.
> More information: <https://manned.org/pivot_root.8>.

- Make `/new_root` the new root (`/`) and move current root to a subdirectory of it:

`sudo pivot_root /new_root /new_root/old_root`

- Display help:

`sudo pivot_root --help`
