# cowsay

> Imprime arte ASCII (por defecto una vaca) diciendo o pensando algo.
> Más información: <https://manned.org/cowsay>.

- Imprime una vaca ASCII diciendo "hola, mundo":

`cowsay "{{hola, mundo}}"`

- Imprime una vaca ASCII diciendo texto de `stdin`:

`echo "{{hola, mundo}}" | cowsay`

- Lista todos los tipos de arte disponibles:

`cowsay -l`

- Imprime el arte ASCII especificado diciendo "hola, mundo":

`cowsay -f {{arte}} "{{hola, mundo}}"`

- Imprime un pensamiento triste de una vaca ASCII:

`cowthink -d "{{Solo soy una vaca, no una gran pensadora...}}"`

- Imprime una vaca ASCII con ojos personalizados diciendo "hola, mundo":

`cowsay -e {{caracteres}} "{{hola, mundo}}"`
