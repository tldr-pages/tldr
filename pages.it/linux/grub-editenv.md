# grub-editenv

> Modifica le variabili d'ambiente di GRUB.
> Maggiori informazioni: <https://www.gnu.org/software/grub/manual/grub/grub.html>.

- Imposta una voce di avvio predefinita (supponendo che la voce di avvio esista già):

`grub-editenv /boot/grub/grubenv set default={{Ubuntu}}`

- Mostra tutte le variabili d'ambiente di GRUB:

`grub-editenv /boot/grub/grubenv list`

- Reimposta la variabile `saved_entry` al valore predefinito:

`grub-editenv /boot/grub/grubenv unset saved_entry`
