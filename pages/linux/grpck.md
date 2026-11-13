# grpck

> Verify the integrity of the group files (`/etc/group` and `/etc/gshadow`).
> See also: `pwck`, `vigr`.
> More information: <https://manned.org/grpck>.

- Check the group files and interactively fix errors:

`sudo grpck`

- Check the group files without making any changes:

`sudo grpck {{[-r|--read-only]}}`

- Sort entries in the group files by group ID (modifies the files; cannot be combined with `--read-only`):

`sudo grpck {{[-s|--sort]}}`

- Check specific group and gshadow files:

`sudo grpck {{[-r|--read-only]}} {{path/to/group}} {{path/to/gshadow}}`
