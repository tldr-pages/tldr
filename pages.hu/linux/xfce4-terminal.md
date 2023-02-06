# xfce4-terminal

> Az XFCE4 terminál emulátor. További információ: <https://docs.xfce.org/apps/xfce4-terminal/start>.

- Nyisson meg egy új terminálablakot:

`xfce4-terminal`

- Állítsa be a kezdeti címet:

`xfce4-terminal --initial-title "{{initial_title}}"`

- Új lap megnyitása az aktuális terminálablakban:

`xfce4-terminal --tab`

- Parancs végrehajtása egy új terminálablakban:

`xfce4-terminal --command "{{command_with_args}}"`

- A terminál megtartása a végrehajtott parancs végrehajtásának befejezése után:

`xfce4-terminal --command "{{command_with_args}}" --hold`

- Több új lap megnyitása, mindegyikben egy parancs végrehajtása:

`xfce4-terminal --tab --command "{{command_a}}" --tab --command "{{command_b}}"`
