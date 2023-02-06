# infection

> Egy mutációs tesztelési keretrendszer PHP-hez. További információ: <https://infection.github.io>.

- A kód elemzése a konfigurációs fájl segítségével (vagy hozzon létre egyet, ha nem létezik):

`infection`

- Használjon meghatározott számú szálat:

`infection --threads {{number_of_threads}}`

- Adjon meg egy minimális mutációs eredménymutatót (MSI):

`infection --min-msi {{percentage}}`

- Adjon meg egy minimálisan lefedett kód MSI-t:

`infection --min-covered-msi {{percentage}}`

- Egy adott tesztelési keretrendszer használata (alapértelmezés szerint PHPUnit):

`infection --test-framework {{phpunit|phpspec}}`

- Csak a tesztek által lefedett kódsorok mutációja:

`infection --only-covered`

- Az alkalmazott mutációs kód megjelenítése:

`infection --show-mutations`

- A napló szóbeliségének megadása:

`infection --log-verbosity {{default|all|none}}`
