# cvfsck

> Check and repair an Xsan file system volume.
> Part of the Xsan file system utilities on macOS.
> More information: <https://www.manpagez.com/man/1/cvfsck/>.

- Check an Xsan volume for metadata corruption (read-only mode):

`sudo cvfsck {{/Volumes/XsanVolume}}`

- Repair a corrupted Xsan volume (make modifications to fix problems):

`sudo cvfsck -w {{/Volumes/XsanVolume}}`

- Log problems to the system log (used mainly during automatic startup checks):

`sudo cvfsck -l {{/Volumes/XsanVolume}}`

- Report free-space fragmentation on an Xsan volume:

`sudo cvfsck -f {{/Volumes/XsanVolume}}`
