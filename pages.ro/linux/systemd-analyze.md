# systemd-analyze

> Afișați detaliile de sincronizare despre procesul de încărcare a unităților (servicii, puncte de montare, dispozitive, prize).

- Lista de timp a fiecărei unități pentru a porni:

`systemd-analyze blame`

- Imprimați un copac al lanțului critic de timp de unități:

`systemd-analyze critical-chain`

- Creați un fișier SVG care arată când a început fiecare serviciu de sistem, evidențiind timpul petrecut la inițializare:

`systemd-analyze plot > {{path/to/file.svg}}`

- Trasați un grafic de dependență și convertiți-l într-un fișier SVG:

`systemd-analyze dot | dot -T{{svg}} > {{path/to/file.svg}}`
