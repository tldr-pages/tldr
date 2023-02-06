# ts

> Időbélyegzők hozzáadása minden sorhoz a standard bemenetről. További információ: <https://joeyh.name/code/moreutils/>.

- Időbélyegző hozzáadása minden sor elejére:

`{{some_command}} | ts`

- Időbélyegek hozzáadása mikroszekundumos pontossággal:

`{{some_command}} | ts "{{%b %d %H:%M:%.S}}"`

- \[i\]ncrementális időbélyegek hozzáadása mikroszekundumos pontossággal, nullától kezdve:

`{{some_command}} | ts -i "{{%H:%M:%.S}}"`

- A szöveges fájlban (pl. naplófájlban) meglévő időbélyegzők \[r\]elatív formátumba történő átalakítása:

`cat {{path/to/file}} | ts -r`
