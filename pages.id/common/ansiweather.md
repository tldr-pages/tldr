# ansiweather

> Tampilkan kondisi cuaca saat ini ke dalam terminal.
> Informasi lebih lanjut: <https://github.com/fcambus/ansiweather>.

- Tampilkan ramalan cuaca ([f]orecast) selama tujuh hari ke depan bagi suatu [l]okasi, dengan satuan [u]nit ukur metrik:

`ansiweather -u metric -f 7 -l {{Rzeszow,PL}}`

- Tampilkan ramalan cuaca ([F]orecast) selama lima hari ke depan bagi lokasi saat ini, dengan tampilan [s]imbol serta informasi waktu matahari terbit dan terbenam ([d]aylight):

`ansiweather -F -s true -d true`

- Tampilkan informasi kecepatan angin ([w]ind) dan kelembapan udara ([h]umidity) bagi waktu dan lokasi saat ini:

`ansiweather -w true -h true`
