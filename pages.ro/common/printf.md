# printf

> Formatarea și imprimarea textului.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/printf>

- Imprimarea unui mesaj text:

`printf "{{%s\n}}" "{{Hello world}}"`

- Imprimați un număr întreg în albastru aldine:

`printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}`

- Imprimați un număr plutitor cu semnul Unicode Euro:

`printf "{{\u20AC %.2f\n}}" {{123.4}}`

- Imprimarea unui mesaj text compus cu variabile de mediu:

`printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"`

- Stocați un mesaj formatat într-o variabilă (nu funcționează pe zsh):

`printf -v {{myvar}} {{"This is %s = %d\n" "a year" 2016}}`
