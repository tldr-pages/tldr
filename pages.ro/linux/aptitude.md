# aptitude

> Utilitar de gestionare a pachetelor Debian și Ubuntu.
> Mai multe informaţii: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>

- Sincronizați lista de pachete și versiuni disponibile. Aceasta ar trebui să fie rulată mai întâi, înainte de a rula următoarele comenzi de aptitude:

`aptitude update`

- Instalați un nou pachet și dependențele sale:

`aptitude install {{package}}`

- Caută un pachet:

`aptitude search {{package}}`

- Caută un pachet instalat (`? instalat` este un termen de cautare a aptitudinilor):

`aptitude search '?installed({{package}})'`

- Eliminați un pachet și toate pachetele în funcție de acesta:

`aptitude remove {{package}}`

- Upgrade pachetele instalate la cele mai noi versiuni disponibile:

`aptitude upgrade`

- Upgrade-ul pachetelor instalate (cum ar fi `aptitude upgrade'), inclusiv eliminarea pachetelor învechite și instalarea de pachete suplimentare pentru a satisface noile dependențe de pachete:

`aptitude full-upgrade`

- Puneţi în aşteptare un pachet instalat pentru a preveni actualizarea automată a acestuia:

`aptitude hold '?installed({{package}})'`
