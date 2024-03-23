# osascript

> Jalankan AppleScript atau JavaScript for Automation (JXA) dari command-line.
> Informasi lebih lanjut: <https://keith.github.io/xcode-man-pages/osascript.1.html>.

- Menjalankan sebuah perintah AppleScript:

`osascript -e "{{say 'Halo dunia'}}"`

- Menjalankan beberapa perintah AppleScript:

`osascript -e "{{say 'Halo'}}" -e "{{say 'dunia'}}"`

- Mengeksekusi perintah dari file AppleScript yang telah terkompilasi (`*.scpt`), terbundel (`*.scptd`), atau secara plaintext (`*.applescript`):

`osascript {{jalan/menuju/apple.scpt}}`

- Mendapatkan ID pengenal (bundle identifier) dari sebuah aplikasi (dapat digunakan untuk perintah `open -b`):

`osascript -e 'id of app "{{Aplikasi}}"'`

- Menjalankan sebuah perintah JavaScript:

`osascript -l JavaScript -e "{{console.log('Halo dunia');}}"`

- Mengeksekusi perintah dari file JavaScript:

`osascript -l JavaScript {{jalan/menuju/javascript.js}}`
