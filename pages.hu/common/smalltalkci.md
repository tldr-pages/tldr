# smalltalkci

> Smalltalk projektek tesztelésére szolgáló keretrendszer a GitHub Actions, Travis CI, AppVeyor, GitLab CI és mások segítségével. További információ: <https://github.com/hpi-swa/smalltalkCI>.

- Tesztek futtatása egy konfigurációs fájlhoz:

`smalltalkci {{path/to/.smalltalk.ston}}`

- Az aktuális könyvtárban található `.smalltalk.ston` konfigurációhoz tartozó tesztek futtatása:

`smalltalkci`

- Tesztek hibakeresése headful módban (VM ablak megjelenítése):

`smalltalkci --headful`

- Letölt és előkészít egy jól ismert smalltalk-képet a tesztekhez:

`smalltalkci --smalltalk {{Squeak64-Trunk}}`

- Egyéni Smalltalk-kép és VM megadása:

`smalltalkci --image {{path/to/Smalltalk.image}} --vm {{path/to/vm}}`

- A gyorsítótárak kitakarítása és a buildek törlése:

`smalltalkci --clean`
