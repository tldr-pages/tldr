# deno

> Runtime aman untuk JavaScript, TypeScript, dan WebAssembly.
> Mencakup pengelolaan ketergantungan modul menggunakan `npm` atau `jsr`, serta perangkat pengolah program seperti penolok ukur, pemaket, dokumentasi program, dan penghitung cakupan pengujian. 
> Informasi lebih lanjut: <https://docs.deno.com/runtime/reference/cli/>.

- Jalankan sebuah shell interaktif REPL (Read-Eval-Print-Loop):

`deno`

- Buat suatu proyek dan ujikan proyek tersebut, yang bernama sample:

`deno init sample && cd sample && deno test`

- Jalankan suatu berkas program secara aman. Ia akan menanyakan (bila perlu) apakah program ini berhak mengakses jaringan, membaca berkas, dsb.:

`deno run {{jalan/menuju/berkas.ts}}`

- Jalankan berkas program dengan memberikan sebagaian atau seluruh hak-hak (hanya jika Anda percaya asal atau pengembang program tersebut) secara eksplisit:

`deno run {{--allow-env|--allow-net|--allow-write|--allow-all}} {{jsr:@deno/deployctl}}`

- Tampilkan dan jalankan tugas dari `deno.json` atau kumpulan skrip yang terdaftar pada `package.json`:

`deno task`

- Pasang modul ketergantungan yang terdaftar pada `deno.json` atau `package.json` (beserta berkas kunci versi modul / lock files):

`deno install`

- Periksa struktur tipe data, format penulisan naskah, dan perbaiki kesalahan secara otomatis (jika memungkinkan):

`deno check && deno fmt && deno lint --fix`

- Bangunkan suatu berkas menjadi suatu berkas program executable, termasuk modul-modul yang tergantung, dan program pejalan berkas program (runtime):

`deno compile {{path/to/file.ts}}`
