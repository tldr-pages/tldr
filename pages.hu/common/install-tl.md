# install-tl

> TeX Live keresztplatformos telepítő. További információ: <https://tug.org/texlive/>.

- Indítsa el a szöveges telepítőt (Unix rendszereken alapértelmezett):

`install-tl -no-gui`

- Indítsa el a GUI telepítőt (alapértelmezett macOS és Windows rendszereken, Tcl/Tk szükséges):

`install-tl -gui`

- Telepítse a TeX Live-ot egy adott profilfájlban meghatározottak szerint:

`install-tl -profile {{path/to/texlive.profile}}`

- Indítsa el a telepítőt egy adott profilfájl beállításaival:

`install-tl -init-from-file {{path/to/texlive.profile}}`

- Indítsa el a telepítőt hordozható eszközre, például USB-pendrive-ra történő telepítéshez:

`install-tl -portable`

- Súgó megjelenítése a `install-tl` oldalon:

`install-tl -help`
