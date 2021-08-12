# genfstab

> Arch Linux script de instalare pentru a genera ieșire potrivită pentru adăugarea la un fișier fstab.
> Mai multe informaţii: <https://man.archlinux.org/man/extra/arch-install-scripts/genfstab.8>

- Afișează o ieșire compatibilă fstab bazată pe o etichetă de volum:

`genfstab -L {{path/to/mount_point}}`

- Afișează o ieșire compatibilă fstab bazată pe un volum UUID:

`genfstab -U {{path/to/mount_point}}`

- Un mod obișnuit de a genera un fișier fstab, necesită permisiuni de root:

`genfstab -U {{/mnt}} >> {{/mnt/etc/fstab}}`

- Adăugați un volum într-un fișier fstab pentru a-l monta automat:

`genfstab -U {{path/to/mount_point}} | sudo tee -a /etc/fstab`
