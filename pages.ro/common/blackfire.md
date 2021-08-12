# blackfire

> Un instrument de profilare a liniei de comandă pentru PHP.
> Mai multe informaţii: <https://blackfire.io>

- Inițializarea și configurarea clientului Blackfire:

`blackfire config`

- Lansează agentul Blackfire:

`blackfire agent`

- Lansarea agentului Blackfire pe un anumit soclu:

`blackfire agent --socket="{{tcp://127.0.0.1:8307}}"`

- Rulați profilerul pe un anumit program:

`blackfire run {{php path/to/file.php}}`

- Rulați profilerul și colectați 10 eșantioane:

`blackfire --samples={{10}} run {{php path/to/file.php}}`

- Rulați profiler și rezultatele de ieșire ca JSON:

`blackfire --json run {{php path/to/file.php}}`

- Încărcați un fișier profiler în serviciul web Blackfire:

`blackfire upload {{path/to/file}}`

- Vizualizați starea profilurilor pe serviciul web Blackfire:

`blackfire status`
