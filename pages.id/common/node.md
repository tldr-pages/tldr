# node

> Platform JavaScript sisi server (Node.js).
> Informasi lebih lanjut: <https://nodejs.org>.

- Menjalankan berkas JavaScript:

`node {{alamat/ke/berkas}}`

- Memulai sebuah REPL (shell interaktif):

`node`

- Mengevaluasi kode JavaScript dengan memberikanya sebagai sebuah argument:

`node -e "{{kode}}"`

- Mengevaluasi dan mencetak hasil, berguna untuk melihat versi dependesni node:

`node -p "{{process.versions}}"`

- Mengaktifkan inspector, menjeda eksekusi sampai debugger terhubung segera setelah kode sumber sepenuhnya terparser:

`node --no-lazy --inspect-brk {{alamat/ke/berkas}}`
