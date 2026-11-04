# grub-mkrelpath

> Convert a system path to a path relative to its filesystem root for GRUB.
> More information: <https://www.gnu.org/software/grub/manual/grub/html_node/Invoking-grub_002dmkrelpath.html>.

- Print the GRUB path of a file:

`grub-mkrelpath {{path/to/file}}`

- Print the GRUB path of a file on a separately mounted filesystem:

`grub-mkrelpath {{/mnt/partition/path/to/file}}`
