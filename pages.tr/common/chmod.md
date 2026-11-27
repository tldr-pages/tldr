# chmod

> Bir dosyanın veya dizinin erişim izinlerini değiştir.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

- Dosyanın sahibi olan kullanıcıya dosyayı çalıştırma izni ver:

`chmod u+x {{yol/dosya}}`

- Kullanıcıya bir dosyayı/dizini okuma ve yazma izni ver:

`chmod u+rw {{yol/dosya_veya_dizin}}`

- Gruptan ve diğerlerinden çalıştırma iznini kaldır:

`chmod g-x,o-x {{yol/dosya}}`

- Tüm kullanıcılara okuma ve çalıştırma izni ver:

`chmod a+rx {{yol/dosya}}`

- Diğerlerine (dosya sahibinin grubunda olmayanlara) grupla aynı izinleri ver:

`chmod o=g {{yol/dosya}}`

- Diğerlerinin tüm izinlerini kaldır:

`chmod o= {{yol/dosya}}`

- İzinleri sekizlik gösterimle ayarla:

`chmod {{644}} {{yol/dosya}}`

- Dosyalar için tüm kullanıcılara özyinelemeli olarak okuma izni ver. Ayrıca en az bir çalıştırma izni olan dosyalara ve tüm alt dizinlere çalıştırma izni ver:

`chmod {{[-R|--recursive]}} a+rX {{yol/dizin}}`
