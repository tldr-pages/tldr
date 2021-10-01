# node

> Server-seitige JavaScript Plattform (Node.js).
> Weitere Informationen: <https://nodejs.org>.

- Führe eine JavaScript Datei aus:

`node {{pfad/zu/datei}}`

- Starte eine REPL (Interaktive Shell):

`node`

- Evaluiere als Argument übergebenen JavaScript Code:

`node -e "{{code}}"`

- Evaluierung und Ausgabe des Ergebnisses. Nützlich, um die Versionen der Abhängigkeiten von Node zu sehen:

`node -p "{{process.versions}}"`

- Aktiviere Inspector und pausiere die Ausführung bis sich ein Debugger verbindet sobald der Quellcode vollständig geparsed ist:

`node --no-lazy --inspect-brk {{pfad/zu/datei}}`
