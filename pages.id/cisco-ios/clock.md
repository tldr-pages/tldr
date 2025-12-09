# clock

> Atur waktu sistem.
> Informasi lebih lanjut: <https://www.cisco.com/c/en/us/td/docs/ios/fundamentals/command/reference/cf_book/cf_c1.html#clock>.

- Atur waktu dalam mode eksekusi istimewa:

`clock set {{23}}:{{59}}:{{59}} {{31}} {{april}} {{2000}}`

- Lakukan proses negosiasi waktu otomatis sejauh ujung rantai jaringan, dengan active-clock sebagai sumber waktu bawaan:

`clock active prefer`

- Lakukan proses negosiasi waktu otomatis sejauh ujung rantai jaringan, dengan passive-clock sebagai sumber waktu bawaan:

`clock passive prefer`

- Tampilkan mode waktu saat ini sebagaimana dinegosiasikan oleh peranti tegar (firmware):

`clock show interfaces`
