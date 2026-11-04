# egrep

> Vyhledat vzory v souborech pomocí rozšířených `regex` výrazů.
> Poznámka: Tento příkaz je aliasem pro `grep --extended-regexp`.
> Viz také: `regex`.
> Více informací: <https://manned.org/egrep>.

- Vyhledat jeden nebo více opakujících se znaků:

`egrep '{{a}}+' {{cesta/k/souboru}}`

- Vyhledat jeden nebo žádný výskyt znaku (nepovinný výskyt):

`egrep '{{a}}?' {{cesta/k/souboru}}`

- Vyhledat 10 výskytů určitého znaku:

`egrep '{{a}}{10}' {{cesta/k/souboru}}`

- Vyhledat 3 až 7 výskytů určitého znaku:

`egrep '{{a}}{3,7}' {{cesta/k/souboru}}`

- Vyhledat jednu z uvedených možností:

`egrep '{{kocka}}|{{pes}}|{{mys}}' {{cesta/k/souboru}}`

- Vyhledat jednu z uvedených možností v rámci vetšího vzoru:

`egrep 'c({{a}}|{{o}}|{{u}})p' {{cesta/k/souboru}}`

- Vyhledat skupinu znaků opakující se jednou nebo vícekrát:

`egrep '({{aeiou}})+' {{cesta/k/souboru}}`

- Vyhledat pomocí standardních tříd znaků (více info: <https://www.regular-expressions.info/posixbrackets.html>):

`egrep [[{{:alnum:|:alpha:|:space:|...}}]] {{cesta/k/souboru}}`
