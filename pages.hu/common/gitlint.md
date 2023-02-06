# gitlint

> A Git commit message linter ellenőrzi a commit üzenetek stílusát. További információ: <https://jorisroovers.com/gitlint/>.

- Ellenőrizze az utolsó commit üzenetet:

`gitlint`

- A commitok tartománya lint:

`gitlint --commits {{single_refspec_argument}}`

- Egy könyvtár vagy python modul elérési útja extra felhasználó által definiált szabályokkal:

`gitlint --extra-path {{path/to/directory}}`

- Egy adott CI munka elindítása:

`gitlint --target {{path/to/target_directory}}`

- Egy commit-msg-t tartalmazó fájl elérési útja:

`gitlint --msg-filename {{path/to/filename}}`

- Lépcsőzetes commit meta-info olvasása a helyi tárolóból:

`gitlint --staged`
