# Style guide

Diese Seite listet alle Regeln für `tldr`-Seiten auf.

## Layout

Eine Standard-`tldr`-Seite sollte dem folgenden Format entsprechen:

```md
# befehl

> Kurze Beschreibung.
> Möglichst nur eine Zeile; wenn nötig, sind zwei akzeptabel.
> Weitere Informationen: <https://example.com>.

- Beispielbeschreibung:

`befehl -opt1 -opt2 -arg1 {{arg_wert}}`

- Beispielbeschreibung:

`befehl -opt1 -opt2`
```

Es gibt einen Linter, der das obige Format prüft.
Er wird automatisch bei jeder Pull Request ausgeführt,
er kann aber auch manuell installiert werden, um neue Seiten schon vorher zu überprüfen:

```sh
npm install --global tldr-lint
tldr-lint {{seite.md}}
```

Für andere Optionen von `tldr-lint`, wie zum Beispiel das Linten eines ganzen Verzeichnisses:
[`tldr tldr-lint`](https://github.com/tldr-pages/tldr/blob/main/pages/common/tldr-lint.md). Alternativ, kann man auch den Alias `tldrl` verwenden.

Viele Clients unterstützen die `--render` Flag zum Anzeigen einer Seite:

```sh
tldr --render {{seite.md}}
```

## Token-Syntax

Eingaben der Nutzer\*innen sollten die `{{Token}}`-Syntax benutzen,
damit `tldr`-Clients sie hervorheben können.

Die folgenden Regeln sollten für Tokens beachtet werden:

1. Kurze und deskriptive Tokens,
   z. B. `{{source_file}}` oder `{{wallet.txt}}`.
2. Benutze `snake_case` <!--TODO: german wikipedia article for snake_case--> für Tokens, die aus mehreren Wörtern bestehen.
3. Benutze `{{filename}}` statt `{{file_name}}`.
4. Benutze für Pfade von Dateien oder Verzeichnissen das Format `{{path/to/<Platzhalter>}}`.
   Beispielsweise `ln -s {{path/to/file}} {{path/to/symlink}}`.
   Benutze für Platzhalter, die ein Pfad zu einer Datei oder einem Verzeichnis sein können `{{path/to/file_or_directory}}`
5. Folge der `{{path/to/<Platzhalter>}}`-Konvention für alle Pfad-bezogenen Befehle, außer wenn der
   Ort der Datei implizit ist.
6. Wenn ein Befehl eine bestimmte Dateiendung erwartet, benutze sie.
   Beispiel: `unrar x {{compressed.rar}}`.
   Für eine generelle Dateiendung, benutze `{{.ext}}`, aber **nur**, wenn eine Endung wirklich nötig ist.
   Beispielsweise, in find.md's Beispiel "Find files by extension" (`find {{root_path}} -name '{{*.ext}}'`)
   erklärt `{{*.ext}}` den Befehl ohne unnötig spezifisch zu sein;
   Aber in einem Befehl wie `wc -l {{file}}`, genügt `{{file}}` (ohne Endung).
7. Wenn das Beispiel mit einem konkreten Wert klarer ist, nutze einen Beispielwert.
   Benutze beispielsweise `iostat {{2}}` statt `iostat {{interval_in_secs}}`.
8. Wenn ein Befehl irreversible Änderungen am Dateisystem oder Geräten vornimmt, schreibe jedes Beispiel so, dass es nicht blind copy-pastet werden kann.
   Schreibe beispielsweise `ddrescue --force --no-scrape {{/dev/sdX}} {{/dev/sdY}}` statt  `ddrescue --force --no-scrape /dev/sda /dev/sdb`und benutze den `{{/dev/sdXY}}`-Platzhalter statt `/dev/sda1` für *blockgeräte*.

Generell sollten Tokens es so intuitiv wie möglich machen,
herauszufinden, wie der Befehl funktioniert und sie mit Werten auszufüllen.

Technische Begriffe in der Beschreibung sollten die `Backtick`-Syntax (\`) benutzen.
Benutze Backticks für Folgendes:

1. Pfade, wie `package.json`, `/etc/package.json`.
2. Dateiendungen, wie `.dll`.
3. Befehle, wie `ls`.

## Serial Comma

Benutze für eine Liste von 3 oder mehr Elementen ein [serial comma](https://en.wikipedia.org/wiki/Serial_comma), um Mehrdeutigkeiten zu verhindern.

> Delete the Git branches, tags and remotes.

Das obige Beispiel nutzt kein serial comma und ist somit mehrdeutig:

- Lösche die Git Branches namens `tags` und `remotes`.
- Lösche die Git Branches und die Git Tags und die Git Remotes.

Dies kann durch ein Komma vor "and" oder "or" gelöst werden.

> Delete the Git branches, tags, and remotes.
