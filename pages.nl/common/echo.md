# echo

> Toont gegeven argumenten.
> Zie ook: `printf`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Toon een tekstbericht. Let op: aanhalingstekens zijn optioneel:

`echo "{{Hallo Wereld}}"`

- Toon een bericht met omgevingsvariabelen:

`echo "{{Mijn pad is $PATH}}"`

- Toon een bericht zonder de afsluitende nieuwe regel:

`echo -n "{{Hallo Wereld}}"`

- Voeg een bericht aan een bestand toe:

`echo "{{Hallo Wereld}}" >> {{bestand.txt}}`

- Schakel interpretatie van backslash-escapes (speciale tekens) in:

`echo -e "{{kolom 1\tkolom 2}}"`

- Toon de afsluitstatus van de laatst uitgevoerde opdracht (Let op: in Windows Command Prompt en PowerShell zijn de equivalente opdrachten respectievelijk `echo %errorlevel%` en `$lastexitcode`):

`echo $?`

- Geef tekst door aan een ander programma via `stdin`:

`echo "{{Hallo Wereld}}" | {{programma}}`
