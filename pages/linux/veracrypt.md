# veracrypt

> Free and open source disk encryption software.
> More information: <https://www.veracrypt.fr/code/VeraCrypt/plain/doc/html/Documentation.html>.

- Decrypt a volume using a password and mount it to a directory:

`veracrypt --password={{password}} {{path/to/volume}} {{path/to/mount_point}}`

- Dismount a volume on the directory it is mounted to:

`veracrypt --dismount {{path/to/mounted_point}}`
