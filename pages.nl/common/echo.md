# echo

> Drukt gegeven argumenten af.
> Meer informatie: <https://www.gnu.org/software/coreutils/echo>.

- Druk een tekstbericht af. Let op: aanhalingstekens zijn optimaal:

`echo "{{Hallo Wereld}}"`

- Druk een bericht af met omgevingsvariabelen:

`echo "{{Mijn pad is $PATH}}"`

- Drukt een bericht af zonder te volgen met een nieuwe regel:

`echo -n "{{Hallo Wereld}}"`

- Voeg een bericht aan een bestand toe:

`echo "{{Hallo Wereld}}" >> {{bestand.txt}}`

- Interpretatie van backslash-escapes (speciale tekens) inschakelen:

`echo -e "{{kolom 1\kolom 2}}"`

- Druk de afsluitstatus van de laatst uitgevoerde opdracht af (Opmerking: in Windows Command Prompt en PowerShell zijn de equivalente opdrachten respectievelijk `echo %errorlevel%` en `$lastexitcode`):

`echo $?`
