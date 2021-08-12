# btrfs

> Un sistem de fișiere bazat pe principiul copy-on-write (COW) pentru Linux.
> Mai multe informaţii: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs>

- Creează subvolum:

`sudo btrfs subvolume create {{path/to/subvolume}}`

- Lista subvolumelor:

`sudo btrfs subvolume list {{path/to/mount_point}}`

- Afișează informațiile de utilizare a spațiului:

`sudo btrfs filesystem df {{path/to/mount_point}}`

- Activează cota:

`sudo btrfs quota enable {{path/to/subvolume}}`

- Arată cota:

`sudo btrfs qgroup show {{path/to/subvolume}}`
