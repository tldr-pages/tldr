# veracrypt

> Free and open source disk encryption software.
> More information: <https://arcanecode.com/2021/06/21/veracrypt-on-the-command-line-for-ubuntu-linux/>.

- Create a new volume through a text user interface and use `/dev/urandom` as a source of random data:

`veracrypt {{[-t|--text]}} {{[-c|--create]}} --random-source={{/dev/urandom}}`

- Decrypt a volume interactively through a text user interface and mount it to a directory:

`veracrypt {{[-t|--text]}} {{path/to/volume}} {{path/to/mount_point}}`

- Decrypt a partition using a keyfile and mount it to a directory:

`veracrypt {{[-k|--keyfiles]}} {{path/to/keyfile}} {{/dev/sdXN}} {{path/to/mount_point}}`

- Dismount a volume on the directory it is mounted to:

`veracrypt {{[-d|--dismount]}} {{path/to/mounted_point}}`
