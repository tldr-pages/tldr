# xcopy

> Copia di file e directory.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/xcopy>.

- Copia il/i file nella destinazione specificata:

`xcopy {{percorso\del\file_o_directory}} {{percorso\della\destinazione}}`

- Elenca i file da copiare prima di copiarli verso la destinazione:

`xcopy {{percorso\del\file_o_directory}} {{percorso\della\destinazione}} /p`

- Copia solo la struttura della directory senza i file:

`xcopy {{percorso\del\file_o_directory}} {{percorso\della\destinazione}} /t`

- Copia le directory vuote:

`xcopy {{percorso\del\file_o_directory}} {{percorso\della\destinazione}} /e`

- Mantieni le politiche di accesso della sorgente (ACL) nella directory di destinazione:

`xcopy {{percorso\del\file_o_directory}} {{percorso\della\destinazione}} /o`

- Continua l'operazione dopo l'interruzione della connessione di rete:

`xcopy {{percorso\del\file_o_directory}} {{percorso\della\destinazione}} /z`

- Sovrascrivi automaticamente i file di destinazione già esistenti:

`xcopy {{percorso\del\file_o_directory}} {{percorso\della\destinazione}} /y`

- Mostra l'aiuto dettagliato:

`xcopy /?`
