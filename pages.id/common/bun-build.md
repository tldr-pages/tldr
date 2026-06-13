# bun build

> Lakukan proses pengemasan berkas program JavaScript dan TypeScript dengan pengemas Bun yang cepat.
> Informasi lebih lanjut: <https://bun.com/docs/bundler>.

- Kemas suatu berkas titik masuk program menuju berkas luaran/output:

`bun build {{jalan/menuju/titik_masuk.ts}} --outfile {{jalan/menuju/luaran.js}}`

- Kemas beberapa berkas menuju suatu direktori luaran:

`bun build {{jalan/menuju/berkas1.ts jalan/menuju/berkas2.ts ...}} --outdir {{jalan/menuju/dist}}`

- Kemas pula peta kode sumber untuk memudahkan proses awakutu/debugging:

`bun build {{jalan/menuju/titik_masuk.ts}} --outfile {{jalan/menuju/luaran.js}} --sourcemap`

- Kemas dan perkecil berkas luaran untuk produksi:

`bun build {{jalan/menuju/titik_masuk.ts}} --outfile {{jalan/menuju/luaran.js}} --minify`

- Kemas dengan menujukan lingkungan eksekusi/runtime program:

`bun build {{jalan/menuju/titik_masuk.ts}} --outfile {{jalan/menuju/luaran.js}} --target {{browser|bun|node}}`

- Kemas ke dalam suatu berkas program executable:

`bun build {{jalan/menuju/titik_masuk.ts}} --compile --outfile {{jalan/menuju/executable}}`

- Terus awasi kode sumber dan kemas ulang bila terdapat perubahan:

`bun build {{jalan/menuju/titik_masuk.ts}} --outfile {{jalan/menuju/luaran.js}} --watch`

- Masukkan juga kode modul-modul eksternal yang dipakai dalam program:

`bun build {{jalan/menuju/titik_masuk.ts}} --outfile {{jalan/menuju/luaran.js}} {{[-e|--external]}} {{react react-dom}}`
