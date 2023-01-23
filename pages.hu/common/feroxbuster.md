# feroxbuster

> Egyszerű, gyors, rekurzív tartalomkereső eszköz, amely Rust nyelven íródott. Használható webszerverek rejtett elérési útvonalainak feltárására és más célokra. További információ: <https://epi052.github.io/feroxbuster-docs/docs/>.

- Konkrét könyvtárak és fájlok felfedezése, amelyek megfelelnek a szólistában a kiterjesztésekkel és 100 szálakkal, valamint egy véletlenszerű felhasználó-ügynökkel:

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --threads {{100}} --extensions "{{php,txt}}" --random-agent`

- Könyvtárak felsorolása rekurzió nélkül egy adott proxy-n keresztül:

`feroxbuster --url "{{https://example.com}}" --wordlist {{path/to/file}} --no-recursion --proxy "{{http://127.0.0.1:8080}}"`

- Linkek keresése weboldalakon:

`feroxbuster --url "{{https://example.com}}" --extract-links`

- Szűrés egy adott státuszkód és karakterek száma alapján:

`feroxbuster --url "{{https://example.com}}" --filter-status {{301}} --filter-size {{4092}}`
