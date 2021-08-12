# btrfs filesystem

> Gestionați sistemele de fișiere Btrfs.
> Mai multe informaţii: <https://btrfs.wiki.kernel.org/index.php/Manpage/btrfs-filesystem>

- Afișează utilizarea sistemului de fișiere (opțional rulat ca root pentru a afișa informații detaliate):

`btrfs filesystem usage {{path/to/btrfs_mount}}`

- Arată utilizarea de către dispozitive individuale:

`sudo btrfs filesystem show {{path/to/btrfs_mount}}`

- Defragmentarea unui singur fișier pe un sistem de fișiere btrfs (evitați în timp ce se execută un agent de eliminare a duplicatelor):

`sudo btrfs filesystem defragment -v {{path/to/file}}`

- Defragmentarea unui director recursiv (nu traversează limitele subvolumului):

`sudo btrfs filesystem defragment -v -r {{path/to/directory}}`

- Forțați sincronizarea blocurilor de date nescrise pe disc (e):

`sudo btrfs filesystem sync {{path/to/btrfs_mount}}`

- Rezumați utilizarea discului pentru fișierele dintr-un director recursiv:

`sudo btrfs filesystem du --summarize {{path/to/directory}}`
