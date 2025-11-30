# pivot_root

> Change the root filesystem to a new directory and move the current root to another location.
> Commonly used during system initialization (e.g., in initramfs) to switch from a temporary root to the real root filesystem.
> More information: <https://manned.org/pivot_root>.

- Move the current root to `/old_root` and make `/new_root` the new root:

`sudo pivot_root /new_root /new_root/old_root`

- Display help:

`sudo pivot_root --help`
