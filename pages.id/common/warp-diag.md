# warp-diag

> Alat diagnostik dan umpan balik bagi layanan Cloudflare WARP.
> Lihat juga: `warp-cli`.
> Informasi lebih lanjut: <https://developers.cloudflare.com/warp-client/>.

- Membuat sebuah file arsip (zip) berisi informasi konfigurasi sistem dan log debug terhadap koneksi WARP:

`warp-diag`

- Membuat sebuah file arsip diagnostik dengan membubuhkan stempel waktu ke dalam nama file:

`warp-diag --add-ts`

- Menyimpan file arsip diagnostik ke dalam direktori tertentu:

`warp-diag --output {{jalan/menuju/direktori}}`

- Memberikan saran kepada Cloudflare WARP secara interaktif:

`warp-diag feedback`
