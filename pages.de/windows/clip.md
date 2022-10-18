# clip

> Weiterleiten von Inhalten der Befehlsausgabe in die Windows Zwischenablage.
> Weitere Informationen: <https://learn.microsoft.com/de-de/windows-server/administration/windows-commands/clip>.

- Weiterleiten der Verzeichnisauflistung in die Windows Zwischenablage:

`{{Verzeichnis}} | clip`

- Kopieren des Inhalts einer Datei in die Windows-Zwischenablage:

`clip < {{Pfad/zur/Datei.txt}}`

- Kopieren von Text mit einem nachfolgenden Zeilenumbruch in die Windows-Zwischenablage:

`echo {{irgendein Text}} | clip`

- Kopieren von Text ohne nachfolgenden Zeilenumbruch in die Windows-Zwischenablage:

`echo | set /p="irgendein Text" | clip`
