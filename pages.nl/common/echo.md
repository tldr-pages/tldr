# echo

> Toont gegeven argumenten.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html>.

- Toon een tekstbericht. Let op: aanhalingstekens zijn optioneel:

`echo "{{Hallo Wereld}}"`

- Toon een bericht met omgevingsvariabelen:

`echo "{{Mijn pad is $PATH}}"`

- Toont een bericht zonder te volgen met een nieuwe regel:

`echo -n "{{Hallo Wereld}}"`

- Voeg een bericht aan een bestand toe:

`echo "{{Hallo Wereld}}" >> {{bestand.txt}}`

- Interpretatie van backslash-escapes (speciale tekens) inschakelen:

`echo -e "{{kolom 1\kolom 2}}"`

- Toon de afsluitstatus van de laatst uitgevoerde opdracht (Let op: in Windows Command Prompt en PowerShell zijn de equivalente opdrachten respectievelijk `echo %errorlevel%` en `$lastexitcode`):

`echo $?`
