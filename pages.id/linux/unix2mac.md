# unix2mac

> Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format Unix menuju macOS.
> Program ini menggantikan simbol LF menjadi CR.
> Lihat juga: `unix2dos`, `dos2unix`, dan `mac2unix`.
> Informasi lebih lanjut: <https://manned.org/unix2mac>.

- Ganti format pengakhiran baris teks dan simpan perubahan pada berkas yang sama:

`unix2mac {{jalan/menuju/berkas}}`

- Ganti format namun simpan perubahan sebagai berkas baru:

`unix2mac {{[-n|--newfile]}} {{jalan/menuju/berkas}} {{jalan/menuju/berkas_baru}}`

- Tampilkan informasi suatu berkas teks:

`unix2mac {{[-i|--info]}} {{jalan/menuju/berkas}}`

- Tetap jaga/tambahkan/hapus simbol Byte Order Mark (BOM) saat mengubah isi berkas:

`unix2mac --{{keep-bom|add-bom|remove-bom}} {{jalan/menuju/berkas}}`
