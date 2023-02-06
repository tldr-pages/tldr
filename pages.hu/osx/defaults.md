# defaults

> A macOS felhasználói konfigurációjának olvasása és írása alkalmazások számára. További információ: <https://ss64.com/osx/defaults.html>.

- Rendszerbeállítások olvasása egy alkalmazás beállításához:

`defaults read "{{application}}" "{{option}}"`

- Alapértelmezett értékek olvasása egy alkalmazási opcióhoz:

`defaults read -app "{{application}}" "{{option}}"`

- Kulcsszó keresése tartománynevekben, kulcsokban és értékekben:

`defaults find "{{keyword}}"`

- Egy alkalmazási opció alapértelmezett értékének írása:

`defaults write "{{application}}" "{{option}}" {{-type}} {{value}}`

- Mission Control animációk felgyorsítása:

`defaults write com.apple.Dock expose-animation-duration -float 0.1`

- Egy alkalmazás összes alapértelmezett értékének törlése:

`defaults delete "{{application}}"`
