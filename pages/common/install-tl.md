# install-tl

> TeX Live cross-platform installer.
> More information: <https://tug.org/texlive/>.

- Start the text-based installer (default on Unix systems):

`install-tl -no-gui`

- Start the GUI installer (default on macOS and Windows, requires Tcl/Tk):

`install-tl -gui`

- Install TeX Live as defined in a specific profile file:

`install-tl -profile {{path/to/texlive.profile}}`

- Start the installer with the settings from a specific profile file:

`install-tl -init-from-file {{path/to/texlive.profile}}`

- Start the installer for installation on a portable device, like a USB stick:

`install-tl -portable`

- Show help for `install-tl`:

`install-tl -help`
