# iscc

> Fordító az Inno Setup telepítőkhöz. Az Inno Setup szkripteket Windows telepítőprogram futtatható állományává fordítja. További információ: <https://jrsoftware.org/isinfo.php>.

- Inno Setup szkriptek fordítása:

`iscc {{path/to/file.iss}}`

- Csendben fordít le egy Inno Setup telepítőprogramot:

`iscc /Q {{path/to/file.iss}}`

- Aláírt Inno Setup telepítőprogram fordítása:

`iscc /S={{name}}={{command}} {{path/to/file.iss}}`
