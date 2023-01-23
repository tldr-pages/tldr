# make

> Task runner a Makefile-ban leírt célprogramokhoz. Leginkább a forráskódból származó futtatható program fordításának vezérlésére használják. További információ: <https://www.gnu.org/software/make/manual/make.html>.

- Meghívja a Makefile-ban megadott első célpontot (általában az "all" nevű):

`make`

- Egy adott célpont meghívása:

`make {{target}}`

- Egy adott célpont meghívása, egyszerre 4 feladat párhuzamos végrehajtása:

`make -j{{4}} {{target}}`

- Egy adott Makefile használata:

`make --file {{path/to/file}}`

- A make egy másik könyvtárból történő futtatása:

`make --directory {{path/to/directory}}`

- Kényszeríti a célprogram elkészítését, még akkor is, ha a forrásfájlok változatlanok:

`make --always-make {{target}}`

- A Makefile-ban definiált változó felülírása:

`make {{target}} {{variable}}={{new_value}}`

- A Makefile-ban a környezet által meghatározott változók felülírása:

`make --environment-overrides {{target}}`
