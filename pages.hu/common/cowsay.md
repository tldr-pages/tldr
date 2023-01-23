# cowsay

> ASCII-képek nyomtatása (alapértelmezés szerint egy tehén), amely mond vagy gondol valamit. További információ: <https://github.com/tnalpgge/rank-amateur-cowsay>.

- Egy ASCII tehén kiírása, amely azt mondja: "hello, world":

`cowsay "{{hello, world}}"`

- Egy ASCII tehén nyomtatása, amely a `stdin` szövegét mondja:

`echo "{{hello, world}}" | cowsay`

- Az összes elérhető művészeti típus felsorolása:

`cowsay -l`

- A megadott ASCII-képek nyomtatása, amelyek azt mondják, hogy "hello, world":

`cowsay -f {{art}} "{{hello, world}}"`

- Egy halott gondolkodó ASCII tehén nyomtatása:

`cowthink -d "{{I'm just a cow, not a great thinker...}}"`

- Egyedi szemű ASCII tehén nyomtatása, amely azt mondja: "hello, world":

`cowsay -e {{characters}} "{{hello, world}}"`
