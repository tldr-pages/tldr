# yes

> Bir şeyi tekrar tekrar yazdır.
> Bu komut genelde yükleme işlemleri sırasında onay için yes yazmak için kullanılır (apt-get gibi).
> Daha fazla bilgi: <https://www.gnu.org/software/coreutils/yes>.

- Tekrar tekrar "mesaj" yazdır:

`yes {{mesaj}}`

- Tekrar tekrar "y" yazdır:

`yes`

- `apt-get` komutu tarafından sorulan her şeyi kabul et:

`yes | sudo apt-get install {{program}}`
