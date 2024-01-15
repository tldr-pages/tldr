# duplicity

> Crea archivi incrementali, compressi, cifrati con controllo di versione.
> Può caricare i backup su una varietà di servizi backend.
> Maggiori informazioni: <http://duplicity.nongnu.org>.

- Esegui il backup di una directory via FTPS su una macchina remota, cifrandolo con una password:

`FTP_PASSWORD={{password_login_ftp}} PASSPHRASE={{password_cifratura}} duplicity {{percorso/della/directory_sorgente}} {{ftps://utente@hostname/percorso/della/directory_target/}}`

- Esegui il backup di una directory in un server Amazon S3, facendo un backup completo ogni mese:

`duplicity --full-if-older-than {{1M}} s3://{{nome_bucket[/prefisso]}}`

- Elimina le versioni più vecchie di un anno da un backup salvato in un server WebDAV:

`FTP_PASSWORD={{password_login_webdav}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://utente@hostname[:porta]/directory}}`

- Elenca i backup disponibili:

`duplicity collection-status "file://{{percorso/assoluto/della/directory/di/backup}}"`

- Elenca i file in un backup salvato su una macchina remota, via SSH:

`duplicity list-current-files --time {{YYYY-MM-DD}} scp://{{utente@hostname}}/{{percorso/della/directory/backup}}`

- Ripristina una sotto-directory da un backup locale cifrato con GnuPG in una posizione precisa:

`PASSPHRASE={{password_chiave_gpg}} duplicity restore --encrypt-key {{id_chiave_gpg}} --path-to-restore {{percorso/relativo/sotto_directory}} file://{{percorso/assoluto/della/directory/di/backup}} {{percorso/della/directory/dove/ripristinare}}`
