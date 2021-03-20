# nms

> Un efecto chulo de desencriptación de output.
> Más información: <https://github.com/bartobri/no-more-secrets>.

- Desencriptar "Hola, Mundo!" tras presionar una tecla:

`echo "Hola, Mundo! | nms"`

- Desencriptar el output de `ls -la` automaticamente:

`ls -la | nms -a`

- Desencriptar el contenido de `mensage_secreto.txt` automaticamente, con output rojo:

`cat mensaje_secreto.txt | nms -a -f red`

- Limpiar la pantalla previo a desencriptar `git status` automaticamente:

`git status | nms -a -c`
