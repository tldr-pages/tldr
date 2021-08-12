# uvcdynctrl

> Un instrument de linie de comandă libwebcam pentru a gestiona controalele dinamice în uvcvideo.

- Listează toate camerele disponibile:

`uvcdynctrl -l`

- Specificați dispozitivul de utilizat (implicit la `video0`):

`uvcdynctrl -d {{device_name}}`

- Lista controalelor disponibile:

`uvcdynctrl -c`

- Setați o nouă valoare de control (pentru valori negative, adăugați — înainte de {{-value}}}):

`uvcdynctrl -s {{control_name}} {{value}}`

- Obțineți valoarea curentă de control:

`uvcdynctrl -g {{control_name}}`

- Salvați starea controalelor curente într-un fișier:

`uvcdynctrl -W {{filename}}`

- Încărcați starea controalelor dintr-un fișier:

`uvcdynctrl -L {{filename}}`
