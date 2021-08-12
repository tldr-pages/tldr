# e2fsck

> Verificați un sistem de fișiere Linux ext2/ext3/ext4. În momentul executării comenzii, sistemul de fișiere trebuie demontat.
> Mai multe informaţii: <https://manned.org/e2fsck>

- Verificați sistemul de fișiere, raportând orice blocuri deteriorate:

`e2fsck {{/dev/sdXN}}`

- Verificați sistemul de fișiere și reparați automat blocurile deteriorate:

`e2fsck -p {{/dev/sdXN}}`

- Verificați sistemul de fișiere în modul doar citire:

`e2fsck -c {{/dev/sdXN}}`
