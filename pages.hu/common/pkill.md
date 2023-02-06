# pkill

> Folyamat jelzése név szerint. Leginkább folyamatok leállítására használják. További információ: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>.

- Minden olyan folyamat megállítása, amelyik megfelel:

`pkill "{{process_name}}"`

- Az összes olyan folyamat megállítása, amely megfelel a teljes parancsnak, nem csak a folyamat nevének:

`pkill -f "{{command_name}}"`

- Megfelelő folyamatok megölésének kikényszerítése (nem lehet blokkolni):

`pkill -9 "{{process_name}}"`

- SIGUSR1 jelet küld a megfelelő folyamatoknak:

`pkill -USR1 "{{process_name}}"`

- A `firefox` főfolyamat megölése a böngésző bezárásához:

`pkill --oldest "{{firefox}}"`
