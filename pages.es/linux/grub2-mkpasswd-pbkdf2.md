# grub2-mkpasswd-pbkdf2

> Genera una contraseña hasheada para GRUB.
> Más información: <https://manned.org/grub2-mkpasswd-pbkdf2>.

- Crea un hash de contraseña para GRUB 2 usando PBKDF2 y lo imprime en `stdout`:

`sudo grub2-mkpasswd-pbkdf2 {{[-c|--iteration-count]}} {{numero_de_iteraciones_pbkdf2}} {{[-s|--salt]}} {{longitud_salt}}`
