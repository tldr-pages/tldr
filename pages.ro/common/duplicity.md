# duplicity

> Creează copii de rezervă incrementale, comprimate, criptate și versiuni.
> De asemenea, puteți încărca copiile de rezervă într-o varietate de servicii backend.
> Mai multe informaţii: <http://duplicity.nongnu.org>

- Copierea de rezervă a unui director prin FTPS pe o mașină de la distanță, criptarea cu o parolă:

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source/directory}} {{ftps://user@hostname/target/directory/path/}}`

- Copierea de rezervă a unui director pe Amazon S3, făcând o copie de rezervă completă în fiecare lună:

`duplicity --full-if-older-than {{1M}} --use-new-style s3://{{bucket_name[/prefix]}}`

- Ștergeți versiunile mai vechi de 1 an dintr-o copie de rezervă stocată pe o partajare WebDAV:

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_dir}}`

- Listați copiile de rezervă disponibile:

`duplicity collection-status "file://{{absolute/path/to/backup/directory}}"`

- Listați fișierele într-o copie de rezervă stocată pe o mașină de la distanță, prin intermediul ssh:

`duplicity list-current-files --time {{YYYY-MM-DD}} scp://{{user@hostname}}/path/to/backup/dir`

- Restaurați un subdirector dintr-o copie de rezervă locală criptată GNUPG într-o anumită locație:

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --file-to-restore {{relative/path/restoredirectory}} file://{{absolute/path/to/backup/directory}} {{path/to/directory/to/restore/to}}`
