# dmesg

> A kernel üzenetek kiírása a standard kimenetre. További információ: <https://manned.org/dmesg>.

- A kernel üzenetek megjelenítése:

`dmesg`

- A rendszermag hibaüzeneteinek megjelenítése:

`dmesg --level err`

- A kernel üzenetek megjelenítése és az újak folyamatos beolvasása, hasonlóan a `tail -f` (elérhető a 3.5.0 és újabb kernelekben):

`dmesg -w`

- Megmutatja, hogy mennyi fizikai memória áll rendelkezésre ezen a rendszeren:

`dmesg | grep -i memory`

- A rendszermag üzeneteinek megjelenítése egyszerre 1 oldalra:

`dmesg | less`

- Kernelüzenetek megjelenítése időbélyeggel (a 3.5.0 és újabb rendszermagokban elérhető):

`dmesg -T`

- A rendszermag üzenetek megjelenítése ember által olvasható formában (a 3.5.0 és újabb rendszermagokban érhető el):

`dmesg -H`

- A kimenet színezése (a 3.5.0 és újabb rendszermagokban elérhető):

`dmesg -L`
