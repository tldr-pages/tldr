# certutil

> Strumento per gestire e configurare informazioni sul contenuto dei certificati.
> Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>.

- Esegue il dump delle informazioni di configurazione o del file:

`certutil {{nome_file}}`

- Codifica un file in esadecimale:

`certutil -encodehex {{percorso\al\file_di_input}} {{percorso\al\file_di_output}}`

- Codifica un file in Base64:

`certutil -encode {{percorso\al\file_di_input}} {{percorso\al\file_di_output}}`

- Decodifica un file codificato da Base64:

`certutil -decode {{percorso\al\file_di_input}} {{percorso\al\file_di_output}}`

- Genera e mostra l'hash crittografico di un file:

`certutil -hashfile {{percorso\al\file_di_input}} {{md2|md4|md5|sha1|sha256|sha384|sha512}}`

