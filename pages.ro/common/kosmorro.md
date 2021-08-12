# kosmorro

> Calculați efemeridele și evenimentele pentru o dată dată dată, la o anumită poziție pe Pământ.
> Mai multe informaţii: <http://kosmorro.space>

- Obțineți efemeride pentru Paris, Franța:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}}`

- Obțineți efemeride pentru Paris, Franța, în zona de fus orar UTC+2:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --timezone={{2}}`

- Obțineți efemeride pentru Paris, Franța, pe 9 iunie 2020:

`kosmorro --latitude={{48.7996}} --longitude={{2.3511}} --date={{2020-06-09}}`

- Generează un PDF (notă: TexLive trebuie instalat):

`kosmorro --format={{pdf}} --output={{path/to/file.pdf}}`
