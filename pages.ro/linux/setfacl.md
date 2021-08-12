# setfacl

> Setați liste de control al accesului la fișiere (ACL).

- Modificarea ACL a unui fișier pentru utilizator cu acces de citire și scriere:

`setfacl -m u:{{username}}:rw {{file}}`

- Modificați ACL implicit al unui fișier pentru toți utilizatorii:

`setfacl -d -m u::rw {{file}}`

- Elimină ACL a unui fișier pentru un utilizator:

`setfacl -x u:{{username}} {{file}}`

- Eliminați toate intrările ACL ale unui fișier:

`setfacl -b {{file}}`
