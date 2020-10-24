# node

> Platform JavaScript sisi server (Node.js).
> Informasi lebih lanjut: <https://nodejs.org>.

- Menjalankan berkas JavaScript:

`node {{path/to/file}}`

- Memulai sebuah REPL (shell interaktif):

`node`

- Mengevaluasi kode JavaScript dengan memberikanya sebagai sebuah argument:

`node -e "{{code}}"`

- Mengevaluasi dan mencetak hasil, berguna untuk melihat versi dependesni node:

`node -p "{{process.versions}}"`

- Mengaktifkan inspector, menjeda eksekusi sampai debugger terhubung segera setelah kode sumber sepenuhnya terparser:

`node --no-lazy --inspect-brk {{path/to/file}}`
