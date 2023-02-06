# say

> Szöveget beszéddé alakít. További információ: <https://ss64.com/osx/say.html>.

- Mondjon hangosan egy mondatot:

`say "{{I like to ride my bike.}}"`

- Fájl hangos felolvasása:

`say --input-file={{filename.txt}}`

- Mondjon el egy mondatot egyéni hanggal és beszédsebességgel:

`say --voice={{voice}} --rate={{words_per_minute}} "{{I'm sorry Dave, I can't let you do that.}}"`

- A rendelkezésre álló hangok listája (a különböző hangok különböző nyelveken beszélnek):

`say --voice="?"`

- Mondjon valamit lengyelül:

`say --voice={{Zosia}} "{{Litwo, ojczyzno moja!}}"`

- Hangfájl létrehozása az elhangzott szövegből:

`say --output-file={{filename.aiff}} "{{Here's to the Crazy Ones.}}"`
