# cpio

> Utilitaire d'archivage
> Supportes les format d'archivages [--format]: binaire, ASCII, crc, HPUX, tar, et POSIX.1 tar.
> Plus d'informations: <https://www.gnu.org/software/cpio>.

- Capture le contenue de la console et l'archive en format binaire [o]:

`echo "{{file1}} {{file2}} {{file3}}" | cpio -o > {{archive.cpio}}`

- Archive[o] tous fichiers specifier en argument avec [v]erbosité:

`find {{path/to/directory}} | cpio -ov > {{archive.cpio}}`

- Extrait tous les fichiers de l'archive[i], crée les repertoire[d], avec [v]erbosité:

`cpio -idv < {{archive.cpio}}`

- Extrait le contenue de l'archive et le duplique à partir du répertoire courant, même si le nom de fichier sont absolus:

`cpio -idv --no-absolute-filenames < {{archive.cpio}}`
