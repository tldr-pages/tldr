# node

> Platform JavaScript sisi server (Node.js).
> Informasi lebih lanjut: <https://nodejs.org>.

- Jalankan berkas program JavaScript:

`node {{jalan/menuju/berkas}}`

- Jalankan sebuah REPL (shell interaktif):

`node`

- Jalankan berkas program dan jalankan ulang saat isi dari berkas tersebut terubah (membutuhkan Node.js versi 18.11+):

`node --watch {{jalan/menuju/file}}`

- Evaluasi kode JavaScript dengan memberikanya sebagai sebuah argument:

`node {{[-e|--eval]}} "{{kode}}"`

- Evaluasi kode dan cetak hasil, berguna untuk melihat versi dependesni node:

`node {{[-p|--print]}} "process.versions"`

- Aktifkan inspector, yang akan menjeda eksekusi sampai debugger terhubung segera setelah kode sumber sepenuhnya terparser:

`node --no-lazy --inspect-brk {{jalan/menuju/berkas}}`
