# mkswap

> Configurează o zonă de swap Linux pe un dispozitiv sau într-un fișier.

- Configurarea unei partiții date ca zonă de swap:

`sudo mkswap {{/dev/sdb7}}`

- Utilizați un fișier dat ca zonă de swap:

`sudo mkswap {{path/to/file}}`

- Verificați o partiție pentru blocuri necorespunzătoare înainte de a crea zona swap:

`sudo mkswap -c {{/dev/sdb7}}`

- Specificați o etichetă pentru fișier (pentru a permite „swapon” să folosească eticheta):

`sudo mkswap -L {{swap1}} {{path/to/file}}`
