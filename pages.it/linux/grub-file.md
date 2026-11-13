# grub-file

> Verifica se un file è di un tipo di immagine avviabile.
> Maggiori informazioni: <https://manned.org/grub-file>.

- Verifica se un file è un'immagine ARM EFI:

`grub-file --is-arm-efi {{percorso/del/file}}`

- Verifica se un file è un'immagine i386 EFI:

`grub-file --is-i386-efi {{percorso/del/file}}`

- Verifica se un file è un'immagine x86_64 EFI:

`grub-file --is-x86_64-efi {{percorso/del/file}}`

- Verifica se un file è un'immagine ARM (kernel Linux):

`grub-file --is-arm-linux {{percorso/del/file}}`

- Verifica se un file è un'immagine x86 (kernel Linux):

`grub-file --is-x86-linux {{percorso/del/file}}`

- Verifica se un file è un'immagine x86_64 XNU (kernel macOS):

`grub-file --is-x86_64-xnu {{percorso/del/file}}`
