# cryfs

> Un sistem de fișiere criptografic pentru cloud.
> Mai multe informaţii: <https://www.cryfs.org/>

- Montează un sistem de fişiere criptat. Expertul de inițializare va fi pornit la prima execuție:

`cryfs {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Demontați un sistem de fișiere criptat:

`cryfs-unmount {{path/to/mount_point}}`

- Demontați automat după zece minute de inactivitate:

`cryfs --unmount-idle {{10}} {{path/to/cipher_dir}} {{path/to/mount_point}}`

- Afișează o listă de cifruri acceptate:

`cryfs --show-ciphers`
