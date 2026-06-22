# wine reg copy

> Copy a registry key to a new location within the Wine registry.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Copy a registry key to a new location:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}'`

- Recursively copy a key together with all its [s]ubkeys and values:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /s`

- [f]orcefully overwrite the destination without prompting for confirmation:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /f`

- Recursively and [f]orcefully copy a key, overwriting the destination:

`wine reg copy '{{HKEY_CURRENT_USER\path\to\source_key}}' '{{HKEY_CURRENT_USER\path\to\destination_key}}' /s /f`

- Display help:

`wine reg copy /?`
