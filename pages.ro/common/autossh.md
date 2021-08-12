# autossh

> Rulați, monitorizați și reporniți conexiunile SSH.
> Reconectează automat pentru a menține tunelurile de redirecționare a portului în sus. Acceptă toate steagurile `ssh`.
> Mai multe informaţii: <https://www.harding.motd.ca/autossh>

- Începeți o sesiune SSH, repornirea atunci când un port de monitorizare nu reușește să returneze date:

`autossh -M {{monitor_port}} "{{ssh_command}}"`

- Redirecționați un port local către unul de la distanță, repornirea atunci când este necesar:

`autossh -M {{monitor_port}} -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Furculiță `autossh` în fundal înainte de a executa `ssh` și nu deschideți o carcasă de la distanță:

`autossh -f -M {{monitor_port}} -N "{{ssh_command}}"`

- Rulați în fundal, fără port de monitorizare, și în schimb trimite pachete SSH keep-live la fiecare 10 secunde pentru a detecta eșec:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" "{{ssh_command}}"`

- Rulați în fundal, fără port de monitorizare și fără coajă de la distanță, ieșind în cazul în care portul înainte eșuează:

`autossh -f -M 0 -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -o ExitOnForwardFailure=yes -L {{local_port}}:localhost:{{remote_port}} {{user}}@{{host}}`

- Rulați în fundal, logare `autossh` depanare ieșire și `ssh` verbose ieșire la fișiere:

`AUTOSSH_DEBUG=1 AUTOSSH_LOGFILE={{path/to/autossh_log_file.log}} autossh -f -M {{monitor_port}} -v -E {{path/to/ssh_log_file.log}} {{ssh_command}}`
