# reflector

> Arch script to fetch and sort mirrorlists.

- get all mirrors, sort for speed and save them

`sudo reflector --sort rate --save /etc/pacman.d/mirrorlist`

- only get the 10 recently sync'd German HTTPS mirrors sorted

`reflector --latest 10 --country Germany --protocol https --sort rate`
