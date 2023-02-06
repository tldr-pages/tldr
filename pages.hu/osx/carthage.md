# carthage

> Függőségkezelő eszköz Cocoa alkalmazásokhoz. További információ: <https://github.com/Carthage/Carthage>.

- Töltse le a Cartfile-ban említett összes függőség legújabb verzióját, és építse be őket:

`carthage update`

- Frissítse a függőségeket, de csak iOS-re építsen:

`carthage update --platform ios`

- Frissítse a függőségeket, de egyiket se építse be:

`carthage update --no-build`

- Töltse le és építse újra a függőségek aktuális verzióját (frissítés nélkül):

`carthage bootstrap`

- Egy adott függőség újraépítése:

`carthage build {{dependency}}`
