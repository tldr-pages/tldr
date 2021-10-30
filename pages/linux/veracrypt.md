# veracrypt

> Free and open source disk encryption software.
> More information: <https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>.

- Create a new volume through a text user interface and use `/dev/urandom` as a source of random data:

`veracrypt --text --create --random-source={{/dev/urandom}}`

- Decrypt a volume interactively through a text user interface and mount it to a directory:

`veracrypt --text {{path/to/volume}} {{path/to/mount_point}}`

- Decrypt a partition using a keyfile and mount it to a directory:

`veracrypt --keyfiles={{path/to/keyfile}} {{/dev/sdXN}} {{path/to/mount_point}}`

- Dismount a volume on the directory it is mounted to:

`veracrypt --dismount {{path/to/mounted_point}}`
