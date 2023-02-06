# osascript

> AppleScript vagy JavaScript for Automation (JXA) futtatása a parancssorból. További információ: <https://ss64.com/osx/osascript.html>.

- AppleScript parancs futtatása:

`osascript -e "{{say 'Hello world'}}"`

- Több AppleScript parancs futtatása:

`osascript -e "{{say 'Hello'}}" -e "{{say 'world'}}"`

- Kompilált (`*.scpt`), csomagolt (`*.scptd`) vagy egyszerű szöveges (`*.applescript`) AppleScript-fájl futtatása:

`osascript {{path/to/apple.scpt}}`

- Egy alkalmazás csomagazonosítójának lekérdezése (hasznos a `open -b`):

`osascript -e 'id of app "{{Application}}"'`

- JavaScript parancs futtatása:

`osascript -l JavaScript -e "{{console.log('Hello world');}}"`

- JavaScript fájl futtatása:

`osascript -l JavaScript {{path/to/script.js}}`
