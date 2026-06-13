# winetricks

> Manage Wine virtual Windows environments.
> More information: <https://gitlab.winehq.org/wine/wine/-/wikis/Winetricks>.

- Start a graphical setup at the default Wine location:

`winetricks`

- Specify a custom Wine directory to run Winetricks in:

`WINEPREFIX={{path/to/wine_directory}} winetricks`

- Install a Windows DLL or component to the default Wine directory:

`winetricks {{package}}`
