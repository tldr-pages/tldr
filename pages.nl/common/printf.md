# printf

> Formatteer en toon tekst.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/printf-invocation.html>.

- Toon een tekstbericht:

`printf "{{%s\n}}" "{{Hallo wereld}}"`

- Toon een geheel getal in vetgedrukt blauw:

`printf "{{\e[1;34m%.3d\e[0m\n}}" {{42}}`

- Toon een drijvend-komma getal met het Unicode euroteken:

`printf "{{\u20AC %.2f\n}}" {{123.4}}`

- Toon een tekstbericht samengesteld met omgevingsvariabelen:

`printf "{{var1: %s\tvar2: %s\n}}" "{{$VAR1}}" "{{$VAR2}}"`

- Sla een geformatteerd bericht op in een variabele (werkt niet in Zsh):

`printf -v {{mijnvar}} {{"Dit is %s = %d\n" "een jaar" 2016}}`

- Toon een hexadecimaal, octaal en wetenschappelijk getal:

`printf "{{hex=%x octal=%o scientific=%e}}" 0x{{FF}} 0{{377}} {{100000}}`
