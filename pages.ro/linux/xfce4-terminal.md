# xfce4-terminal

> Emulatorul terminalului XFCE4.
> Mai multe informaţii: <https://docs.xfce.org/apps/xfce4-terminal/start>

- Deschide o fereastră nouă de terminal:

`xfce4-terminal`

- Stabilește titlul inițial:

`xfce4-terminal --initial-title "{{initial_title}}"`

- Deschideți o filă nouă în fereastra curentă a terminalului:

`xfce4-terminal --tab`

- Execută o comandă într-o fereastră nouă de terminal:

`xfce4-terminal --command "{{command_with_args}}"`

- Păstrați terminalul în jurul valorii de după executarea comenzii executate:

`xfce4-terminal --command "{{command_with_args}}" --hold`

- Deschideți mai multe file noi, executând o comandă în fiecare:

`xfce4-terminal --tab --command "{{command_a}}" --tab --command "{{command_b}}"`
