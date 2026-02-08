# split

- Teile eine Datei, wobei jeder Split 10 Zeilen hat (außer dem letzten Split):

`split {{[-l|--lines]}} 10 {{pfad/zu/datei}}`

- Teile eine Datei in 5 Dateien. Die Datei wird geteilt, sodass jeder Split die gleiche Größe hat (außer dem letzten Split):

`split {{[-n|--number]}} 5 {{pfad/zu/datei}}`

- Teile eine Datei mit 512 Bytes in jedem Split (außer dem letzten Split; verwende 512k für Kilobytes und 512m für Megabytes):

`split {{[-b|--bytes]}} 512 {{pfad/zu/datei}}`

- Teile eine Datei mit höchstens 512 Bytes in jedem Split, ohne Zeilen zu brechen:

`split {{[-C|--line-bytes]}} 512 {{pfad/zu/datei}}`

- Teile in mehrere Dateien aus `stdin`:

`gzip {{[-cd|--stdout --decompress]}} {{pfad/zu/komprimierte_datei.gz}} | split {{[-l|--lines]}} {{1000}} - {{pfad/zu/ausgabe}}`
