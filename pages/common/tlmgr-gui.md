# tlmgr gui

> Start a graphical user interface for `tlmgr`.
> `tlmgr gui` depends on the package `perl-tk`, which has to be installed manually.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Start a GUI for `tlmgr`:

`sudo tlmgr gui`

- Start a GUI specifying the background color:

`sudo tlmgr gui -background "{{#f39bc3}}"`

- Start a GUI specifying the foreground color:

`sudo tlmgr gui -foreground "{{#0ef3bd}}"`

- Start a GUI specifying the font and font size:

`sudo tlmgr gui -font "{{helvetica 18}}"`

- Start a GUI setting a specific geometry:

`sudo tlmgr gui -geometry {{width}}x{{height}}-{{xpos}}+{{ypos}}`

- Start a GUI passing an arbitrary X resource string:

`sudo tlmgr gui -xrm {{xresource}}`
