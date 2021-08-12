# pkill

> Procesul de semnal după nume.
> Folosit în principal pentru oprirea proceselor.
> Mai multe informaţii: <https://www.man7.org/linux/man-pages/man1/pkill.1.html>

- Omoară toate procesele care se potrivesc:

`pkill -9 "{{process_name}}"`

- Ucide toate procesele care se potrivesc cu comanda lor completă în loc de numele procesului:

`pkill -9 --full "{{command_name}}"`

- Trimite semnal SIGUSR1 la procesele care se potrivesc:

`pkill -USR1 "{{process_name}}"`

- Omoară procesul principal `firefox` pentru a închide browserul:

`pkill --oldest "{{firefox}}"`
