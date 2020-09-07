# extundelete

> Restore files from an unmounted partition.
> See also `date` for Unix time information and `umount` for unmounting partitions.
> More information: <http://extundelete.sourceforge.net/>.

- Restore all deleted files inside partion 1 on device b (`sdb1`):

`sudo extundelete {{/dev/sdb1}} --restore-all`

- Restore a file from a path relative to root (Do not start the path with `/`):

`sudo extundelete {{/dev/sdb1}} --restore-file {{path/to/file}}`

- Restore a directory from a path relative to root (Do not start the path with `/`):

`sudo extundelete {{/dev/sdb1}} --restore-directory {{path/to/directory}}`

- Restore all files deleted after January 1st, 2020 (in Unix time):

`sudo extundelete {{/dev/sdb1}} --restore-all --after {{1577840400}}`
