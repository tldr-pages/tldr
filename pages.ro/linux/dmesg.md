# dmesg

> Scrieți mesajele kernel la ieșirea standard.
> Mai multe informaţii: <https://manned.org/dmesg>

- Afișează mesajele kernel:

`dmesg`

- Afișează mesaje de eroare kernel:

`dmesg --level err`

- Afișați mesajele kernel și continuați să citiți altele noi, similare cu `tail -f` (disponibile în kernelurile 3.5.0 și mai noi):

`dmesg -w`

- Arată cât de multă memorie fizică este disponibilă pe acest sistem:

`dmesg | grep -i memory`

- Afișează mesaje kernel 1 pagină la un moment dat:

`dmesg | less`

- Afișați mesajele kernel cu un timestamp (disponibil în kernelurile 3.5.0 și mai noi):

`dmesg -T`

- Afișați mesajele de kernel în formă lizibilă de om (disponibile în kernelurile 3.5.0 și mai noi):

`dmesg -H`

- Ieșire Colorizare (disponibilă în nucleele 3.5.0 și mai noi):

`dmesg -L`
