# duplicity

> Inkrementális, tömörített, titkosított és verziószámozott biztonsági mentéseket készít. A biztonsági mentéseket számos háttértár-szolgáltatásba is fel tudja tölteni. További információ: <http://duplicity.nongnu.org>.

- Egy könyvtár biztonsági mentése FTPS-en keresztül egy távoli gépre, jelszóval titkosítva:

`FTP_PASSWORD={{ftp_login_password}} PASSPHRASE={{encryption_password}} duplicity {{path/to/source/directory}} {{ftps://user@hostname/target/directory/path/}}`

- Biztonsági mentés egy könyvtárról az Amazon S3-ra, havonta egy teljes biztonsági mentés készítése:

`duplicity --full-if-older-than {{1M}} --use-new-style s3://{{bucket_name[/prefix]}}`

- Törölje az 1 évnél régebbi verziókat egy WebDAV-megosztón tárolt biztonsági mentésből:

`FTP_PASSWORD={{webdav_login_password}} duplicity remove-older-than {{1Y}} --force {{webdav[s]://user@hostname[:port]/some_dir}}`

- A rendelkezésre álló biztonsági mentések listázása:

`duplicity collection-status "file://{{absolute/path/to/backup/directory}}"`

- Egy távoli gépen tárolt biztonsági mentés fájljainak listázása ssh-n keresztül:

`duplicity list-current-files --time {{YYYY-MM-DD}} scp://{{user@hostname}}/path/to/backup/dir`

- Egy alkönyvtár visszaállítása egy GnuPG-vel titkosított helyi biztonsági másolatból egy adott helyre:

`PASSPHRASE={{gpg_key_password}} duplicity restore --encrypt-key {{gpg_key_id}} --file-to-restore {{relative/path/restoredirectory}} file://{{absolute/path/to/backup/directory}} {{path/to/directory/to/restore/to}}`
