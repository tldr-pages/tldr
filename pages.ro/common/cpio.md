# cpio

> Copiază fișierele din arhive și din arhive.
> Suportă următoarele formate de arhivă: binar personalizat al cpio, ASCII vechi, noul ASCII, CRC, HPUX binar, HPUX vechi ASCII, vechi tar și POSIX.1 tar.
> Mai multe informaţii: <https://www.gnu.org/software/cpio>

- Luați o listă de nume de fișiere din intrarea standard și adăugați-le [o] nla o arhivă în format binar cpio:

`echo "{{file1}} {{file2}} {{file3}}" | cpio -o > {{archive.cpio}}`

- Copiați toate fișierele și directoarele într-un director și adăugați-le [o] nto o arhivă, în modul [v] erbose:

`find {{path/to/directory}} | cpio -ov > {{archive.cpio}}`

- P [i] ck toate fișierele dintr-o arhivă, generând [d] irectorii acolo unde este necesar, în modul [v] erbose:

`cpio -idv < {{archive.cpio}}`
