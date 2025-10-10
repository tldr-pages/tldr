# cvfsck

> Check and repair an Xsan file system volume.
> Part of the Xsan file system utilities on macOS.
> Requires superuser privileges.
> More information: <https://www.manpagez.com/man/1/cvfsck/>.

- Check an Xsan volume for metadata corruption:
`sudo cvfsck {{/Volumes/XsanVolume}}`

- Repair a corrupted Xsan volume:
`sudo cvfsck -w {{/Volumes/XsanVolume}}`

- Display a list of all files and their metadata:
`sudo cvfsck -l {{/Volumes/XsanVolume}}`

- Print help for available options:
`cvfsck -h`
