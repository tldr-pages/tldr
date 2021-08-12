# modprobe

> Adăugați sau eliminați module din nucleul Linux.

- Prefă-te că încarci un modul în kernel, dar nu o face de fapt:

`sudo modprobe --dry-run {{module_name}}`

- Încărcați un modul în kernel:

`sudo modprobe {{module_name}}`

- Scoateți un modul din kernel:

`sudo modprobe --remove {{module_name}}`

- Eliminați un modul și cele care depind de el din kernel:

`sudo modprobe --remove-dependencies {{module_name}}`

- Afișează dependențele modulului kernel:

`sudo modprobe --show-depends {{module_name}}`
