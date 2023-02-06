# figlet

> ASCII bannerek generálása a felhasználói bemenetből. Lásd még: `showfigfonts`. További információ: <http://www.figlet.org/figlet-man.html>.

- Generálás szöveg közvetlen bevitelével:

`figlet {{input_text}}`

- Egyéni betűtípusfájl használata:

`figlet {{input_text}} -f {{path/to/font_file.flf}}`

- Az alapértelmezett betűtípus könyvtárból származó betűtípus használata (a kiterjesztés elhagyható):

`figlet {{input_text}} -f {{font_filename}}`

- A parancsok kimenete a FIGleten keresztül:

`{{command}} | figlet`

- Elérhető FIGlet betűtípusok megjelenítése:

`showfigfonts {{optional_string_to_display}}`
