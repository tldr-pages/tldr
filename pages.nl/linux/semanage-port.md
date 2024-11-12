# semanage port

> Beheer persistente SELinux-poortdefinities.
> Zie ook: `semanage`.
> Meer informatie: <https://manned.org/semanage-port>.

- Toon alle poortlabelregels:

`sudo semanage port {{-l|--list}}`

- Toon alle door de gebruiker gedefinieerde poortlabelregels zonder koppen:

`sudo semanage port {{-l|--list}} {{-C|--locallist}} {{-n|--noheading}}`

- Voeg een door de gebruiker gedefinieerde regel toe die een label toekent aan een protocol-poortpaar:

`sudo semanage port {{-a|--add}} {{-t|--type}} {{ssh_port_t}} {{-p|--proto}} {{tcp}} {{22000}}`

- Verwijder een door de gebruiker gedefinieerde regel met behulp van zijn protocol-poortpaar:

`sudo semanage port {{-d|--delete}} {{-p|--proto}} {{udp}} {{11940}}`
