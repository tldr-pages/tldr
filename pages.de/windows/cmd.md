# cmd

> Auch Windows-Eingabeaufforderung genannt, der Windows-Befehlsinterpreter.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Starten einer interaktiven Shell-Sitzung:

`cmd`

- Ausführen eines Befehls (Command):

`cmd /c {{echo Hallo Welt}}`

- Ausführen eines Skripts:

`cmd {{Pfad\zur\Datei.bat}}`

- Ausführen eines Befehls und anschließendes Aufrufen einer interaktiven Shell:

`cmd /k {{echo Hallo Welt}}`

- Starten einer interaktiven Shell-Sitzung, bei der `echo` in der Befehlsausgabe deaktiviert ist:

`cmd /q`

- Starten einer interaktiven Shell-Sitzung mit aktivierter oder deaktivierter verzögerter Erweiterung der Umgebungsvariablen:

`cmd /v:{{on|off}}`

- Starten einer interaktiven Shell-Sitzung mit aktivierten oder deaktivierten Befehleerweiterungen:

`cmd /e:{{on|off}}`

- Starten einer interaktiven Shell-Sitzung mit Unicode-Kodierung:

`cmd /u`
