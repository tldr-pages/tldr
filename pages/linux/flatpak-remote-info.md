# flatpak remote-info

> Show information about an application or runtime in a remote.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-remote-info>.

- Show information about a flatpak:

`flatpak remote-info {{remote_name}} {{com.example.app}}`

- Show a log of previous versions in a remote:

`flatpak remote-info --log {{remote_name}} {{com.example.app}}`

- Show information about the specific commit, rather than the latest version:

`flatpak remote-info --commit={{COMMIT}} {{remote_name}} {{com.example.app}}`
