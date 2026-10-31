# fsck.fat

> Check and repair a FAT filesystem. The filesystem should be unmounted.
> More information: <https://manned.org/fsck.fat>.

- Check a filesystem and interactively repair any problems:

`sudo fsck.fat {{/dev/sdXY}}`

- Check a filesystem without changing anything ([n]o-op):

`sudo fsck.fat -n {{/dev/sdXY}}`

- [a]utomatically repair a filesystem:

`sudo fsck.fat -a {{/dev/sdXY}}`

- Check a filesystem and [l]ist path names of files being processed:

`sudo fsck.fat -nl {{/dev/sdXY}}`

- [a]utomatically repair a filesystem and [t]est for bad clusters:

`sudo fsck.fat -at {{/dev/sdXY}}`
