# arduino-builder

> Bangun program dari kode sumber piranti lunak (sketsa) Arduino.
> PERINGATAN DEPREKASI: Alat ini sedang dihapus demi penggunaan perintah `arduino` yang baru.
> Informasi lebih lanjut: <https://github.com/arduino/arduino-builder>.

- Bangun program dari suatu berkas (sketsa) kode sumber piranti lunak:

`arduino-builder -compile {{jalan/menuju/sketsa.ino}}`

- Tentukan tingkat penampilan informasi awakutu (nilai bawaan: 5):

`arduino-builder -debug-level {{1..10}}`

- Tentukan direktori untuk menampung hasil pembangunan:

`arduino-builder -build-path {{jalan/menuju/direktori_hasil_pembangunan}}`

- Gunakan konfigurasi yang didefinisikan di dalam suatu berkas, daripada mendefinisikan parameter perintah seperti `-hardware` dan `-tools` berulang kali:

`arduino-builder -build-options-file {{jalan/menuju/build.options.json}}`

- Gunakan mode verbose, tampilkan proses pembangunan secara rinci:

`arduino-builder -verbose {{true}}`
