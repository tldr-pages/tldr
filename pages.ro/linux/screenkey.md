# screenkey

> Un instrument de ecran pentru a afișa tastele apăsate.
> Mai multe informaţii: <https://www.thregr.org/~wavexx/software/screenkey/>

- Tastele de afișare care sunt în prezent în curs de apăsare pe ecran:

`screenkey`

- Tastele de afișare și butoanele mouse-ului care sunt în prezent în curs de apăsare pe ecran:

`screenkey --mouse`

- Lansați meniul de setări al tastei de ecran:

`screenkey --show-settings`

- Lansarea tastei de ecran într-o anumită poziție:

`screenkey --position {{top|center|bottom|fixed}}`

- Modificați formatul modificatorilor cheie afișați pe ecran:

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- Modificați aspectul tastei de ecran:

`screenkey --bg-color "{{#a1b2c3}}" --font {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- Trageți și selectați o fereastră de pe ecran pentru a afișa cheia de ecran:

`screenkey --position fixed --geometry {{$(slop -n -f '%g')}}`
