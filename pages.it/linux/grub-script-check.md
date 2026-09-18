# grub-script-check

> Il programma `grub-script-check` prende un file script GRUB e lo controlla per errori di sintassi.
> Può accettare un percorso come argomento non-opzione. Se non viene fornito, legge da `stdin`.
> Maggiori informazioni: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dscript_002dcheck>.

- Verifica un file script specifico per errori di sintassi:

`grub-script-check {{path/to/grub_config_file}}`

- Mostra ogni riga di input dopo averla letta:

`grub-script-check {{[-v|--verbose]}}`

- Mostra aiuto:

`grub-script-check --help`

- Mostra versione:

`grub-script-check --version`
