# firejail

> În siguranță, nisipurile procesează containerele utilizând capacitățile Linux încorporate.
> Mai multe informaţii: <https://manned.org/firejail>

- Integrați firejail cu mediul desktop:

`sudo firecfg`

- Deschide un Mozilla Firefox restricționat:

`firejail {{firefox}}`

- Porniți un server Apache restricționat pe o interfață și o adresă cunoscută:

`firejail --net={{eth0}} --ip={{192.168.1.244}} {{/etc/init.d/apache2}} {{start}}`

- Lista de cutii de nisip care rulează:

`firejail --list`

- Lista activității de rețea de la care rulează sandbox-uri:

`firejail --netstats`

- Închiderea unei cutii de nisip care rulează:

`firejail --shutdown={{7777}}`
