# wl-copy

> Wayland vágólapkezelő eszköz. Lásd még: `wl-paste`. További információ: <https://github.com/bugaevc/wl-clipboard>.

- Másolja a szöveget a vágólapra:

`wl-copy "{{text}}"`

- A parancs (`ls`) kimenete a vágólapra:

`{{ls}} | wl-copy`

- Másolás csak egy beillesztésre, majd törlés:

`wl-copy --paste-once "{{text}}"`

- A vágólap törlése:

`wl-copy --clear`
