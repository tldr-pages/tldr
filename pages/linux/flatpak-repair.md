# flatpak repair

> Repair a Flatpak installation by pruning invalid objects and reinstalling missing or corrupted files.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-repair>.

- Repair the system-wide Flatpak installation:

`sudo flatpak repair`

- Repair the per-user Flatpak installation:

`flatpak repair --user`

- Repair a custom Flatpak installation by name:

`flatpak repair --installation={{installation_name}}`

- List what would be repaired without making any changes:

`sudo flatpak repair --dry-run`

- Reinstall all refs instead of only those with missing or corrupted objects:

`sudo flatpak repair --reinstall-all`
