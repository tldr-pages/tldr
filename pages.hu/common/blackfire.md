# blackfire

> Parancssori profilkészítő eszköz PHP-hez. További információ: <https://blackfire.io>.

- A Blackfire kliens inicializálása és konfigurálása:

`blackfire config`

- Indítsa el a Blackfire ügynököt:

`blackfire agent`

- A Blackfire-ügynök elindítása egy adott foglalaton:

`blackfire agent --socket="{{tcp://127.0.0.1:8307}}"`

- A profilkészítő futtatása egy adott programon:

`blackfire run {{php path/to/file.php}}`

- A profilozó futtatása és 10 minta összegyűjtése:

`blackfire --samples={{10}} run {{php path/to/file.php}}`

- A profilozó futtatása és az eredmények JSON-ként történő kiadása:

`blackfire --json run {{php path/to/file.php}}`

- Profilozófájl feltöltése a Blackfire webszolgáltatásba:

`blackfire upload {{path/to/file}}`

- A profilok állapotának megtekintése a Blackfire webszolgáltatáson:

`blackfire status`
