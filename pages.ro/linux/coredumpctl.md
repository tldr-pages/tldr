# coredumpctl

> Recuperați și procesați haldele și metadatele de bază salvate.
> Mai multe informaţii: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>

- Listează toate gropile de bază capturate:

`coredumpctl list`

- Lista de gropi de bază capturate pentru un program:

`coredumpctl list {{program}}`

- Afișează informații despre gropile de bază care se potrivesc unui program cu `PID`:

`coredumpctl info {{PID}}`

- Invoke depanator folosind ultima dump de bază a unui program:

`coredumpctl debug {{program}}`

- Extrageți ultima imagine de bază a unui program într-un fișier:

`coredumpctl --output={{path/to/file}} dump {{program}}`
