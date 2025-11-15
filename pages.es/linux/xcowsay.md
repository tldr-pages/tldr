# xcowsay

> Muestra una linda vaca y un mensaje en el escritorio de Linux.
> La vaca se muestra por una cantidad fija de tiempo, o una cantidad de tiempo calculado a partir del tamaño del texto. Haga clic en la vaca para despedirla inmediatamente.
> Más información: <https://manned.org/xcowsay>.

- Muestra una vaca diciendo "hola, mundo":

`xcowsay "{{hola, mundo}}"`

- Muestra una vaca con salida desde otro comando:

`ls | xcowsay`

- Muestra una vaca en las coordenadas X e Y especificadas:

`xcowsay --at={{X}},{{Y}}`

- Muestra una vaca de tamaño diferente:

`xcowsay --cow-size={{small|med|large}}`

- Muestra una burbuja de pensamiento en lugar de una burbuja de discurso:

`xcowsay --think`

- Muestra una imagen diferente en lugar de la vaca predeterminada:

`xcowsay --image={{ruta/al/archivo}}`
