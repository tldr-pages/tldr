# grub-file

> Verifica se un file è di un tipo di immagine avviabile.
> Maggiori informazioni: <https://manned.org/grub-file>.

- Verifica se un file è un'immagine ARM EFI:

`grub-file --is-arm-efi {{path/to/file}}`

- Verifica se un file è un'immagine i386 EFI:

`grub-file --is-i386-efi {{path/to/file}}`

- Verifica se un file è un'immagine x86_64 EFI:

`grub-file --is-x86_64-efi {{path/to/file}}`

- Verifica se un file è un'immagine ARM (kernel Linux):

`grub-file --is-arm-linux {{path/to/file}}`

- Verifica se un file è un'immagine x86 (kernel Linux):

`grub-file --is-x86-linux {{path/to/file}}`

- Verifica se un file è un'immagine x86_64 XNU (kernel macOS):

`grub-file --is-x86_64-xnu {{path/to/file}}`
