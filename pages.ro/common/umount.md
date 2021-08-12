# umount

> Anulați legarea unui sistem de fișiere de la punctul său de montare, făcându-l să nu mai fie accesibil.
> Un sistem de fișiere nu poate fi demontat atunci când este ocupat.

- Demontați un sistem de fișiere, trecând calea către sursa din care este montat:

`umount {{path/to/device_file}}`

- Demontați un sistem de fișiere, trecând calea către ținta unde este montată:

`umount {{path/to/mounted_directory}}`

- Demontați toate sistemele de fișiere montate (cu excepția sistemului de fișiere `proc`):

`umount -a`
