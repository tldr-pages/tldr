# dig

> Alat pencari entri DNS.
> Lihat juga: `resolvectl`, `nslookup`, `host`.
> Informasi lebih lanjut: <https://manned.org/dig>.

- Cari kumpulan alamat IP yang dirujuk oleh suatu nama host (berdasarkan informasi rekor A):

`dig +short {{example.com}}`

- Dapatkan jawaban lebih rinci mengenai suatu domain (berdasarkan informasi rekor A):

`dig +noall +answer {{example.com}}`

- Cari informasi suatu domain menggunakan data jenis rekor DNS tertentu:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Tentukan alamat peladen pencari entri DNS alternatif dan gunakan DNS lewat TLS (DoT) secara opsional:

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{example.com}}`

- Lakukan pencarian alamat DNS terbalik terhadap suatu alamat IP (berdasarkan informasi rekor PTR):

`dig -x {{8.8.8.8}}`

- Cari daftar peladen nama otoritatif untuk zona DNS tertentu dan tampilkan informasi rekor SOA:

`dig +nssearch {{example.com}}`

- Lakukan pencarian secara iteratif dan tampilkan jejak penelusuran untuk menuntaskan pencarian suatu nama domain:

`dig +trace {{example.com}}`

- Lakukan pencarian menggunakan suatu peladen DNS dengan [p]ort non-standar dan protokol TCP:

`dig +tcp -p {{port}} @{{alamat_ip_peladen_dns}} {{example.com}}`
