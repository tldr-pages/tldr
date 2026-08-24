# atom

> Editor di testo multipiattaforma e personalizzabile tramite plugin.
> I plugin sono gestiti da `apm`.
> Nota: Atom è stato dismesso e non è più mantenuto attivamente. Usa `zed` invece.
> Maggiori informazioni: <https://atom.io/>.

- Apri un file o directory:

`atom {{percorso/al/file_o_directory}}`

- Apri un file o directory in una nuova finestra:

`atom {{[-n|--new-window]}} {{percorso/al/file_o_directory}}`

- Apri un file o directory in una finestra esistente:

`atom {{[-a|--add]}} {{percorso/al/file_o_directory}}`

- Avvia Atom in modalità sicura (non carica pacchetti aggiuntivi):

`atom --safe`

- Impedisci ad Atom di andare in background mantenendolo collegato al terminale:

`atom {{[-f|--foreground]}}`

- Aspetta la chiusura della finestra Atom prima di ritornare (utile per editor Git commit):

`atom {{[-w|--wait]}}`
