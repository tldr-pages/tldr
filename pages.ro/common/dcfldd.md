# dcfldd

> Versiune îmbunătățită de dd pentru criminaliști și securitate.
> Mai multe informaţii: <http://dcfldd.sourceforge.net/>

- Copiați un disc într-un fișier de imagine brută și hash imaginea utilizând SHA256:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash=sha256 hashlog={{file.hash}}`

- Copiați un disc într-un fișier de imagine brută, hashing fiecare bucată de 1 GB:

`dcfldd if=/dev/{{disk_device}} of={{file.img}} hash={{sha512|sha384|sha256|sha1|md5}} hashlog={{file.hash}} hashwindow={{1G}}`
