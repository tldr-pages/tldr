# winetricks

> Manage Wine virtual Windows environments.
> More information: <https://wiki.winehq.org/Winetricks>.

- Start a graphical setup at the default wine location:

`winetricks`

- Specify a wine prefix to run winetricks in:

`WINEPREFIX={{/path/to/wine/prefix}} winetricks`

- Install a Windows DLL or a component to the default prefix:

`winetricks {{package}}`
