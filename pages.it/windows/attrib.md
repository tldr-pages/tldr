# attrib

> Mostra o cambia gli attributi di file e cartelle.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/attrib>.

- Mostra tutti gli attributi dei file in una cartella:

`attrib`

- Mostra tutti gli attributi dei file in una cartella specifica:

`attrib {{percorso\della\cartella}}`

- Mostra tutti gli attributi dei file e delle cartelle nella cartella corrente:

`attrib /d`

- Mostra tutti gli attributi dei file in una cartella e le sue sotto-cartelle:

`attrib /s`

- Aggiungi l'attributo `[r]ead-only` o `[a]rchive` o `[s]ystem` o `[h]idden` o `not content [i]ndexed` a file o cartelle:

`attrib +{{r|a|s|h|i}} {{percorso\del\file_o_cartella1 percorso\del\file_o_cartella2 ...}}`

- Rimuovi un attributo specifico da un file o una cartella:

`attrib -{{r|a|s|h|i}} {{percorso\del\file_o_cartella1 percorso\del\file_o_cartella2 ...}}`
