# encfs

> Montează sau creează sisteme de fișiere virtuale criptate.
> Vezi și `fusermount`, care poate demonta sistemele de fișiere montate de această comandă.
> Mai multe informaţii: <https://github.com/vgough/encfs>

- Iniţializarea sau montarea unui sistem de fişiere criptat:

`encfs {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Inițializați un sistem de fișiere criptat cu setări standard:

`encfs --standard {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Rulați encfs în prim-plan în loc să reproducă un daemon:

`encfs -f {{/path/to/cipher_dir}} {{/path/to/mount_point}}`

- Montați un instantaneu criptat al unui director simplu:

`encfs --reverse {{path/to/plain_dir}} {{path/to/cipher_dir}}`
