# grub-mkrescue

> Crea un'immagine avviabile GRUB per CD/USB/floppy.
> Maggiori informazioni: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmkrescue>.

- Crea un ISO avviabile dalla directory corrente e lo salva come `grub.iso`:

`grub-mkrescue --output {{grub.iso}} .`

- Crea un ISO usando file GRUB da una directory personalizzata:

`grub-mkrescue --directory {{/usr/lib/grub/i386-pc}} --output {{grub.iso}} {{path/to/source}}`

- Usa la compressione per i file GRUB durante la creazione dell'immagine, impostando `no` disabilita la compressione:

`grub-mkrescue --compress {{no|xz|gz|lzo}} --output {{grub.iso}} {{path/to/source}}`

- Disabilita l'interfaccia a riga di comando GRUB nell'immagine generata:

`grub-mkrescue --disable-cli --output {{grub.iso}} {{path/to/source}}`

- Precarica moduli GRUB specifici nell'immagine:

`grub-mkrescue --modules "{{part_gpt iso9660}}" --output {{grub.iso}} {{path/to/source}}`

- Passa opzioni aggiuntive direttamente a `xorriso`:

`grub-mkrescue --output {{grub.iso}} -- {{-volid}} {{volume_name}} {{path/to/source}}`

- Mostra aiuto:

`grub-mkrescue {{[-?|--help]}}`

- Mostra versione:

`grub-mkrescue --version`
