# ctrlaltdel

> Utilitate pentru a controla ce se întâmplă când CTRL+ALT+DEL este apăsat.

- Obțineți setarea curentă:

`ctrlaltdel`

- Setați CTRL+ALT+DEL pentru a reporni imediat, fără nici o pregătire:

`sudo ctrlaltdel hard`

- Setați CTRL+ALT+DEL pentru a reporni „normal”, oferind proceselor o șansă de a ieși mai întâi (trimiteți SIGINT la PID1):

`sudo ctrlaltdel soft`
