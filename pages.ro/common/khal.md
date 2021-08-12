# khal

> Un calendar bazat pe text și o aplicație de programare pentru linia de comandă.
> Mai multe informaţii: <https://lostpackets.de/khal>

- Start Khal pe modul interactiv:

`ikhal`

- Tipăriți toate evenimentele programate în calendarul personal pentru următoarele șapte zile:

`khal list -a {{personal}} {{today}} {{7d}}`

- Imprimați toate evenimentele programate nu în calendarul personal pentru mâine la 10:00:

`khal at -d {{personal}} {{tomorrow}} {{10:00}}`

- Imprimați un calendar cu o listă de evenimente pentru următoarele trei luni:

`khal calendar`

- Adăugați un eveniment nou în calendarul personal:

`khal new -a {{personal}} {{2020-09-08}} {{18:00}} {{18:30}} "{{Dentist appointment}}"`
