# deno

> Runtime aman untuk JavaScript dan TypeScript.
> Informasi lebih lanjut: <https://deno.land/>.

- Menjalankan berkas JavaScript atau TypeScript:

`deno {{alamat/ke/berkas.ts}}`

- Menjalankan REPL (shell interaktif):

`deno`

- Menjalankan berkas dengan memperbolehkan akses jaringan:

`deno --allow-net {{alamat/ke/berkas.ts}}`

- Menjalankan berkas dari URL:

`deno {{https://deno.land/std/examples/welcome.ts}}`

- Memasang skrip yang dapat dieksekusi dari URL:

`deno install --allow-net --allow-read {{file_server}} {{https://deno.land/std/http/file_server.ts}}`
