# figlet

> Generați bannere ASCII din intrarea utilizatorului.
> Véase también `showfigfonts`.
> Mai multe informaţii: <http://www.figlet.org/figlet-man.html>

- Generează prin introducerea directă a textului:

`figlet {{input_text}}`

- Utilizați un fișier de font personalizat:

`figlet {{input_text}} -f {{path/to/font_file.flf}}`

- Utilizați un font din directorul de fonturi implicit (extensia poate fi omisă):

`figlet {{input_text}} -f {{font_filename}}`

- ieșire comandă țeavă prin figlet:

`{{command}} | figlet`
