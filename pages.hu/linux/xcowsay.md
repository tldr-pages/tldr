# xcowsay

> Egy aranyos tehén és egy üzenet megjelenítése a Linux asztalon. A tehén vagy egy meghatározott ideig, vagy a szöveg méretéből számított ideig jelenik meg. A tehénre kattintva azonnal elbocsátható. További információ: <https://www.doof.me.uk/xcowsay/>.

- Egy tehén megjelenítése, amely azt mondja, hogy "hello, world":

`xcowsay "{{hello, world}}"`

- Egy tehén megjelenítése egy másik parancs kimenetével:

`ls | xcowsay`

- Egy tehén megjelenítése a megadott X és Y koordinátákon:

`xcowsay --at={{X}},{{Y}}`

- Egy különböző méretű tehén megjelenítése:

`xcowsay --cow-size={{small|med|large}}`

- Gondolatbuborék megjelenítése beszédbuborék helyett:

`xcowsay --think`

- Másik kép megjelenítése az alapértelmezett tehén helyett:

`xcowsay --image={{path/to/file}}`
