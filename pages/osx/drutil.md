# drutil

> Interact with DVD burners.
> More information: <https://keith.github.io/xcode-man-pages/drutil.1.html>.

- Eject a disk from the drive:

`drutil eject`

- Burn a directory as an ISO9660 filesystem onto a DVD. Don't verify and eject when complete:

`drutil burn -noverify -eject -iso9660`
