# wayland-info

> Display information about a Wayland compositor and available protocols.
> More information: <https://gitlab.freedesktop.org/wayland/wayland-utils>.

- Display information about the current Wayland compositor and available protocols:

`wayland-info`

- Display information for interfaces matching a specific name:

`wayland-info --interface {{wl_output}}`

- Display information for interfaces containing a specific string:

`wayland-info -i {{xdg}}`

- Save the output to a file:

`wayland-info > {{path/to/file.txt}}`
