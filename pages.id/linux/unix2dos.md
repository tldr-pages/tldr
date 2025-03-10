# unix2dos

> Ubah format pengakhiran baris teks pada suatu berkas teks (plaintext) dari format Unix menuju DOS.
> Program ini menggantikan simbol LF menjadi CRLF.
> Lihat juga: `unix2mac`, `dos2unix`, dan `mac2unix`.
> Informasi lebih lanjut: <https://manned.org/unix2dos>.

- Ganti format pengakhiran baris teks dan simpan perubahan pada berkas yang sama:

`unix2dos {{jalan/menuju/berkas}}`

- Ganti format namun simpan perubahan sebagai berkas baru:

`unix2dos {{[-n|--newfile]}} {{jalan/menuju/berkas}} {{jalan/menuju/berkas_baru}}`

- Tampilkan informasi suatu berkas teks:

`unix2dos {{[-i|--info]}} {{jalan/menuju/berkas}}`

- Tetap jaga/tambahkan/hapus simbol Byte Order Mark (BOM) saat mengubah isi berkas:

`unix2dos --{{keep-bom|add-bom|remove-bom}} {{jalan/menuju/berkas}}`
