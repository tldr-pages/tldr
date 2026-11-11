# flatpak search

> Search for Flatpak applications and runtimes in configured remotes.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-search>.

- Search for an application or runtime:

`flatpak search "{{text}}"`

- Search only the remotes of the current user:

`flatpak search {{[-u|--user]}} "{{text}}"`

- Show specific columns for each result:

`flatpak search --columns {{name,application,version,...}} "{{text}}"`

