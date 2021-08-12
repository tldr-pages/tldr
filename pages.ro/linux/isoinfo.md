# isoinfo

> Programe utilitare pentru dumping și verificarea imaginilor de disc ISO.

- Listează toate fișierele incluse într-o imagine ISO:

`isoinfo -f -i {{path/to/image.iso}}`

- E [x] trage un anumit fișier dintr-o imagine ISO și trimite-l afară stdout:

`isoinfo -i {{path/to/image.iso}} -x {{/PATH/TO/FILE/INSIDE/ISO.EXT}}`

- Afișează informații antet pentru o imagine de disc ISO:

`isoinfo -d -i {{path/to/image.iso}}`
