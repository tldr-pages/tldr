# robocopy

> Copia robusta di file e directory.
> Per impostazione predefinita, i file saranno copiati solo se la sorgente e la destinazione hanno timestamp o dimensioni dei file diversi.
> Maggiori informazioni: <https://learn.microsoft.com/it-it/windows-server/administration/windows-commands/robocopy>

- Copia tutti i file `.jpg` e `.bmp` da una cartella ad un'altra:

`robocopy {{percorso\della\directory_sorgente}} {{percorso\della\directory_destinazione}} {{*.jpg}} {{*.bmp}}`

- Copia tutti i file e le sottodirectory, includento anche quelle vuote:

`robocopy {{percorso\della\directory_sorgente}} {{percorso\della\directory_destinazione}} /E`

- Mirror/Sincronizza una directory, eliminando tutto ciò che non è nella sorgente e includendo tutti gli attributi e le autorizzazioni:

`robocopy {{percorso\della\directory_sorgente}} {{percorso\della\directory_destinazione}} /MIR /COPYALL`

- Copia tutti i file e le sottodirectory, escludendo i file di origine più vecchi rispetto ai file di destinazione:

`robocopy {{percorso\della\directory_sorgente}} {{percorso\della\directory_destinazione}} /E /XO`

- Elencare tutti i file di dimensioni maggiori o uguali a 50 MB anziché copiarli:

`robocopy {{percorso\della\directory_sorgente}} {{percorso\della\directory_destinazione}} /MIN:{{52428800}} /L`

- Consentire la ripresa se la connessione di rete viene interrotta e limitare i tentativi di ripetizione a 5 e il tempo di attesa a 15 secondi:

`robocopy {{percorso\della\directory_sorgente}} {{percorso\della\directory_destinazione}} /Z /R:5 /W:15`

- Mostra l'aiuto dettagliato:

`robocopy /?`
