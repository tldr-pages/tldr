# yum

> Utilitar de gestionare a pachetelor pentru RHEL, Fedora și CentOS (pentru versiuni mai vechi).
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/yum.8.html>

- Instalați un pachet nou:

`yum install {{package}}`

- Instalați un nou pachet și să își asume da la toate întrebările (de asemenea, funcționează cu actualizare, mare pentru actualizări automate):

`yum -y install {{package}}`

- Găsiți pachetul care oferă o anumită comandă:

`yum provides {{command}}`

- Elimină un pachet:

`yum remove {{package}}`

- Afișează actualizările disponibile pentru pachetele instalate:

`yum check-update`

- Upgrade pachetele instalate la cele mai noi versiuni disponibile:

`yum upgrade`
