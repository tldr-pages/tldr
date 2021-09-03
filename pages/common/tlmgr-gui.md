# tlmgr gui

> Start the graphical user interface of `tlmgr`.
> `tlmgr gui` depends on the package `perl-tk`, which has to be installed manually.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Start the GUI of `tlmgr`:

`sudo tlmgr gui`

- Start the GUI specifying the background color:

`sudo tlmgr gui -background "{{#f39bc3}}"`

- Start the GUI specifying the foreground color:

`sudo tlmgr gui -foreground "{{#0ef3bd}}"`

- Start the GUI specifying the font and font size:

`sudo tlmgr gui -font "{{helvetica 18}}"`

- Start the GUI setting a specific geometry:

`sudo tlmgr gui -geometry {{width}}x{{height}}-{{xpos}}+{{ypos}}`

- Start the GUI passing an arbitrary X resource string:

`sudo tlmgr gui -xrm {{xresource}}`
