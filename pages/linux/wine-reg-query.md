# wine reg query

> Display keys, values, and data in the Wine registry.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Commands>.

- Display all values directly under a key:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}'`

- Display a specific [v]alue of a key:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}' /v {{value_name}}`

- Display the default (unnamed) value of a key:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}' /ve`

- Recursively display a key together with all its [s]ubkeys and values:

`wine reg query '{{HKEY_CURRENT_USER\path\to\key}}' /s`

- Display help:

`wine reg query /?`
