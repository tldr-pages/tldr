# bun audit

> Periksa potensi celah keamanan dalam kumpulan paket yang terpasang.
> Informasi lebih lanjut: <https://bun.com/docs/pm/cli/audit>.

- Lakukan audit atas seluruh proyek dengan berkas ketergantungan paket `bun.lock`:

`bun audit`

- Hanya tampilkan celah keamanan dengan tingkat keparahan setara atau lebih:

`bun audit --audit-level {{low|moderate|high|critical}}`

- Hanya audit kumpulan paket yang diperlukan untuk dijalankan dalam lingkungan laik produksi:

`bun audit --prod`

- Abaikan celah keamanan dengan kode CVE tertentu:

`bun audit --ignore {{CVE-XXXX-YYYY}}`

- Luarkan laporan audit dalam format JSON:

`bun audit --json`
