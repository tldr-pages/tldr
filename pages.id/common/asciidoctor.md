# asciidoctor

> Ubah isi berkas AsciiDoc ke dalam format berkas layak publikasi.
> Informasi lebih lanjut: <https://docs.asciidoctor.org/asciidoctor/latest/cli/man1/asciidoctor/>.

- Ubah suatu berkas `.adoc` ke dalam format HTML (format berkas luaran secara default):

`asciidoctor {{jalan/menuju/berkas.adoc}}`

- Ubah suatu berkas `.adoc` ke dalam format HTML dengan menggunakan suatu berkas definisi penggayaan (stylesheet) CSS:

`asciidoctor {{[-a|--attribute]}} stylesheet={{jalan/menuju/stylesheet.css}} {{jalan/menuju/berkas.adoc}}`

- Ubah suatu berkas `.adoc` menuju format HTML layak semat (embeddable), hanya bangunkan isi tag body HTML:

`asciidoctor {{[-e|--embedded]}} {{jalan/menuju/berkas.adoc}}`

- Ubah suatu berkas `.adoc` menuju PDF melalui pustaka pendukung `asciidoctor-pdf`:

`asciidoctor {{[-b|--backend]}} pdf {{[-r|--require]}} asciidoctor-pdf {{jalan/menuju/berkas.adoc}}`
