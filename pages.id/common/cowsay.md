# cowsay

> Buat dan tampilkan seni teks ASCII (ASCII art) yang menampilkan objek (secara bawaan berupa seekor sapi) yang sedang berkata atau berpikir tentang sesuatu.
> Informasi lebih lanjut: <https://manned.org/cowsay>.

- Tampilkan suatu seni ASCII yang menunjukkan seekor sapi berkata "halo, dunia":

`cowsay "{{halo, dunia}}"`

- Tampilkan seni ASCII sapi dengan pesan dari `stdin`:

`echo "{{halo, dunia}}" | cowsay`

- Tampilkan seluruh variasi seni ASCII yang tersedia:

`cowsay -l`

- Tampilkan pesan "halo, dunia" dengan variasi seni tertentu:

`cowsay -f {{variasi}} "{{halo, dunia}}"`

- Tampilkan seni ASCII seekor sapi yang tewas dan berpikir:

`cowthink -d "{{Saya hanya seekor sapi, bukan pemikir hebat...}}"`

- Tampilkan pesan "halo, dunia" sebagai seni ASCII sapi dengan karakter yang ditentukan sebagai mata sang sapi:

`cowsay -e {{karakter_mata}} "{{halo, dunia}}"`
