# sic

> Client IRC simplu.
> O parte din uneltele fără suge.
> Mai multe informaţii: <https://tools.suckless.org/sic/>

- Conectează-te la gazda implicită (irc.ofct.net) cu porecla setată în variabila de mediu `$USER':

`sic`

- Conectează-te la o anumită gazdă, folosind o poreclă dată:

`sic -h {{host}} -n {{nickname}}`

- Conectați-vă la o anumită gazdă, folosind o poreclă și o parolă dată:

`sic -h {{host}} -n {{nickname}} -k {{password}}`

- Alătură-te unui canal:

`:j #{{channel}}<Enter>`

- Trimite un mesaj către un canal sau utilizator:

`:m #{{channel|user}}<Enter>`

- Setați canalul implicit sau utilizatorul:

`:s #{{channel|user}}<Enter>`
