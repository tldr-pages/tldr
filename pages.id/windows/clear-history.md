# Clear-History

> Hapus kumpulan entri riwayat perintah dari PowerShell.
> Catatan: Perintah `clhy` dapat digunakan sebagai alias untuk `Clear-History`.
> Informasi lebih lanjut: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/clear-history>.

- Hapus seluruh riwayat perintah dari sesi PowerShell saat ini:

`Clear-History`

- Hapus riwayat berdasarkan nama perintah tertentu:

`Clear-History -CommandLine "{{perintah}}"`

- Hapus riwayat berdasarkan berbagai nama perintah:

`Clear-History -CommandLine {{"perintah1", "perintah2", ...}}`

- Hapus entri riwayat berdasarkan nomor induk (ID):

`Clear-History -Id {{nomor_induk}}`

- Hapus entri riwayat berdasarkan beberapa nomor induk:

`Clear-History -Id {{nomor_induk1, nomor_induk2, ...}}`

- Hapus riwayat berdasarkan rentang nomor induk:

`Clear-History -Id ({{nomor_induk_awal}}..{{nomor_induk_akhir}})`

- Tampilkan riwayat mana saja yang akan dihapus, tanpa melakukannya (dry-run):

`Clear-History -WhatIf`

- Tampilkan permintaan konfirmasi sebelum menghapus riwayat:

`Clear-History -Confirm`
