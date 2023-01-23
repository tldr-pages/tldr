# subfinder

> Egy aldomain felfedező eszköz, amely felfedezi a weboldalak érvényes aldomainjeit. Passzív keretrendszerként tervezték, hogy hasznos legyen a bug bountieshez és biztonságos legyen a penetrációs teszteléshez. További információ: <https://github.com/subfinder/subfinder>.

- Aldomainek keresése egy adott domainhez:

`subfinder -d {{example.com}}`

- Csak a talált aldomainek megjelenítése:

`subfinder --silent -d {{example.com}}`

- Brute-force támadással keressen aldomaineket:

`subfinder -d {{example.com}} -b`

- Vadkártyás aldomainek eltávolítása:

`subfinder -nW -d {{example.com}}`

- Megadott, vesszővel elválasztott listát használjon a feloldókból:

`subfinder -r {{8.8.8.8}},{{1.1.1.1}} -d {{example.com}}`
