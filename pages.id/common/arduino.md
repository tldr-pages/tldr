# arduino

> Arduino Studio - Sebuah alat pengembangan piranti lunak (IDE) bagi platform Arduino.
> Informasi lebih lanjut: <https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc>.

- Bangun piranti lunak dari suatu berkas (sketsa) kode sumber:

`arduino --verify {{jalan/menuju/berkas.ino}}`

- Bangun dan pasang piranti lunak menuju perangkat Arduino:

`arduino --upload {{jalan/menuju/berkas.ino}}`

- Bangun dan pasang piranti lunak menuju suatu perangkat Arduino Nano dengan prosesor Atmega328p yang terhubung dalam port `/dev/ttyACM0`:

`arduino --board {{arduino:avr:nano:cpu=atmega328p}} --port {{/dev/ttyACM0}} --upload {{jalan/menuju/berkas.ino}}`

- Atur `nilai` untuk suatu jenis preferensi/konfigurasi berdasarkan `nama` atau kata kunci:

`arduino --pref {{nama}}={{nilai}}`

- Bangun piranti lunak, kemudian simpan menuju suatu direktori hasil pembangunan, dan gunakan kembali hasil-hasil sebelumnya di dalam direktori tersebut:

`arduino --pref build.path={{jalan/menuju/direktori_hasil_pembangunan}} --verify {{jalan/menuju/bekas.ino}}`

- Simpan segala perubahan pada preferensi/konfigurasi menuju berkas `preferences.txt`:

`arduino --save-prefs`

- Pasang piranti pendukung pengembangan untuk perangkat Arduino berbasis SAM (seperti Arduino Due):

`arduino --install-boards "{{arduino:sam}}"`

- Pasang pustaka piranti lunak (library) untuk Bridge dan Servo:

`arduino --install-library "{{Bridge:1.0.0,Servo:1.2.0}}"`
