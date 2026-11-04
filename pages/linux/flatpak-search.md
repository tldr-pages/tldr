# flatpak search

> Search for flatpak applications and runtimes in configured remotes.
> See also: `flatpak`, `flatpak install`, `flatpak remote-info`.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-search>.

- Search for an application or runtime:

`flatpak search "{{text}}"`

- Search only the remotes of the current user:

`flatpak search {{[-u|--user]}} "{{text}}"`

- Search only the default system-wide remotes:

`flatpak search --system "{{text}}"`

- Show specific columns for each result:

`flatpak search --columns {{name,application,version}} "{{text}}"`

- Show all available columns for each result:

`flatpak search --columns all "{{text}}"`
