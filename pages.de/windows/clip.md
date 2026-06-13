# clip

> Kopieren von Inhalten der Befehlsausgabe in die Windows Zwischenablage.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/clip>.

- Kopiere die Ausgabe eines Befehls in die Windows Zwischenablage:

`{{dir}} | clip`

- Kopiere den Inhalt einer Datei in die Windows Zwischenablage:

`clip < {{pfad/zu/datei.txt}}`

- Kopiere Text mit einem nachfolgenden Zeilenumbruch in die Windows Zwischenablage:

`echo {{irgendein text}} | clip`

- Kopiere Text ohne nachfolgenden Zeilenumbruch in die Windows Zwischenablage:

`echo | set /p="irgendein text" | clip`
