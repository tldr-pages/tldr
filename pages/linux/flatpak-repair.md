# flatpak repair

> Check a Flatpak installation for problems and fix them.
> Note: Without root privileges, repairing the system installation only reports problems, as if `--dry-run` were used.
> See also: `flatpak`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-repair>.

- Repair the system-wide installation:

`sudo flatpak repair`

- Repair the current user installation:

`flatpak repair {{[-u|--user]}}`

- Only report problems without making any changes:

`flatpak repair --dry-run`

- Reinstall all applications and runtimes:

`sudo flatpak repair --reinstall-all`
