# apt search

> Search for packages in repositories using APT package manager.
> More information: <https://manpages.ubuntu.com/manpages/jammy/man8/apt.8.html>.

- Search for packages by name:

`apt search {{package_name}}`

- Search for packages by name or description:

`apt search {{keyword}}`

- Search for packages with exact name match:

`apt search {{^package_name$}}`

- Search for packages and show only package names:

`apt search {{keyword}} --names-only`

- Search for packages in a specific section:

`apt search {{keyword}} | grep "{{section}}"`

- Search for packages and show detailed information:

`apt search {{keyword}} --full`

- Search for packages using regular expressions:

`apt search "{{pattern.*}}`

- Search for installed packages only:

`apt search {{keyword}} --installed`
