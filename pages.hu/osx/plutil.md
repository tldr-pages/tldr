# plutil

> Tulajdonságlista ("plist") fájlok megtekintése, konvertálása, hitelesítése vagy szerkesztése. További információ: <https://www.manpagez.com/man/1/plutil/>.

- Egy vagy több plist fájl tartalmának megjelenítése ember által olvasható formátumban:

`plutil -p {{file1.plist file2.plist ...}}`

- Egy vagy több plist-fájl XML-formátumba konvertálása, az eredeti fájlok helyben történő felülírásával:

`plutil -convert xml1 {{file1.plist file2.plist ...}}`

- Egy vagy több plist-fájl bináris formátumba konvertálása, az eredeti fájlok helyben történő felülírásával:

`plutil -convert binary1 {{file1.plist file2.plist ...}}`

- Egy plist fájl átalakítása más formátumba, új fájlba írva:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{path/to/file.plist}} -o {{path/to/new_file.plist}}`

- Egy plist fájl átalakítása más formátumba, a `stdout` címre írva:

`plutil -convert {{xml1|binary1|json|swift|objc}} {{path/to/file.plist}} -o -`
