# ag

> The Silver Searcher. Seperti `ack`, namun bertujuan untuk lebih cepat daripadanya.
> Informasi lebih lanjut: <https://github.com/ggreer/the_silver_searcher>.

- Cari file yang mengandung teks "foo", dan cetak baris teks yang cocok:

`ag {{foo}}`

- Cari file yang mengandung teks "foo" dalam direktori tertentu:

`ag {{foo}} {{jalan/menuju/direktori}}`

- Cari file yang mengandung teks "foo", namun hanya tampilkan daftar nama file saja:

`ag -l {{foo}}`

- Cari file yang mengandung teks "FOO" tanpa memerhatikan perbedaan huruf besar-kecil (case-[i]nsensitive), dan hanya cetak teks yang cocok (jangan cetak kata-kata lainnya meskipun dalam baris yang sama):

`ag -i -o {{FOO}}`

- Cari file yang memiliki nama "bar" dan mengandung teks "foo":

`ag {{foo}} -G {{bar}}`

- Cari file yang memiliki teks yang memenuhi kriteria ekspresi reguler:

`ag '{{^ba(r|z)$}}'`

- Cari file dengan nama yang memiliki teks "foo":

`ag -g {{foo}}`
