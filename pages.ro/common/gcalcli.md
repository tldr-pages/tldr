# gcalcli

> instrument de linie de comandă pentru a interacționa cu Google Calendar.
> Solicită autorizarea API Google la prima lansare.
> Mai multe informaţii: <https://github.com/insanum/gcalcli>

- Listează evenimentele pentru toate calendarele tale în următoarele 7 zile:

`gcalcli agenda`

- Arată evenimente care încep de la sau între anumite date (de asemenea, ia date relative, de exemplu, „mâine”):

`gcalcli agenda {{mm/dd}} [{{mm/dd}}]`

- Lista evenimentelor dintr-un anumit calendar:

`gcalcli --calendar {{calendar_name}} agenda`

- Afișează un calendar ASCII de evenimente de săptămână:

`gcalcli calw`

- Afișează un calendar ASCII de evenimente pentru o lună:

`gcalcli calm`

- Adaugă rapid un eveniment în calendar:

`gcalcli --calendar {{calendar_name}} quick "{{mm/dd}} {{HH:MM}} {{event_name}}"`

- Adaugă un eveniment în calendar. Declanşează promptul interactiv:

`gcalcli --calendar "{{calendar_name}}" add`
