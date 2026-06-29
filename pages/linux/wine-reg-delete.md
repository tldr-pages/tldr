# wine reg delete

> Delete keys and values from the Wine registry.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Delete a registry key and all of its values:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}'`

- Delete a specific [v]alue under a key:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}}`

- Delete the default (unnamed) value of a key:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /ve`

- Delete all values under a key without removing the key itself:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /va`

- [f]orcefully delete without prompting for confirmation:

`wine reg delete '{{HKEY_CURRENT_USER\path\to\key}}' /f`

- Display help:

`wine reg delete /?`
