# wine

> Windows futtatható Unix-alapú rendszereken. További információ: <https://wiki.winehq.org/>.

- Egy adott program futtatása a `wine` környezetben:

`wine {{command}}`

- Egy adott program futtatása a háttérben:

`wine start {{command}}`

- MSI csomag telepítése/eltávolítása:

`wine msiexec /{{i|x}} {{path/to/package.msi}}`

- A `File Explorer`, `Notepad` vagy `WordPad` futtatása:

`wine {{explorer|notepad|write}}`

- A `Registry Editor`, `Control Panel` vagy `Task Manager` futtatása:

`wine {{regedit|control|taskmgr}}`

- A konfigurációs eszköz futtatása:

`wine winecfg`
