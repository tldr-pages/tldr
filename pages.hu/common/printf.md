# printf

> Szöveg formázása és nyomtatása. További információ: <https://www.gnu.org/software/coreutils/printf>.

- Szöveges üzenet nyomtatása:

`printf "{{%s\n}}" "{{Hello world}}"`

- Egész szám nyomtatása félkövér kék színnel:

`printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}`

- Egy lebegőszám nyomtatása az Unicode Euro-jelével:

`printf "{{\u20AC %.2f\n}}" {{123.4}}`

- Környezeti változókkal összeállított szöveges üzenet nyomtatása:

`printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"`

- Formázott üzenet tárolása egy változóban (zsh-n nem működik):

`printf -v {{myvar}} {{"This is %s = %d\n" "a year" 2016}}`
