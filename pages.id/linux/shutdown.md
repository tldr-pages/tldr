# shutdown

> Matikan dan nyalakan ulang sistem komputer.
> Informasi lebih lanjut: <https://manned.org/shutdown.8>.

- Matikan ([h]alt) sistem secara segera:

`shutdown -h now`

- Nyalakan ulang ([r]eboot) segera:

`shutdown -r now`

- Nyalakan ulang dalam 5 menit:

`shutdown -r +{{5}} &`

- Matikan sistem pada pukul 1 siang (menggunakan format 24 jam):

`shutdown -h 13:00`

- Batalkan proses mati atau penyalaan ulang yang telah dijadwalkan:

`shutdown -c`
