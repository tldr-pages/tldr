# chmod

> Bir dosyanın veya dizinin erişim izinlerini değiştir.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html>.

- Dosyanın sahibi olan kullanıcıya dosyayı çalıştırma izni ver:

`chmod u+x {{dosya/yolu}}`

- Kullanıcıya bir dosyayı/dizini okuma ve yazma izni ver:

`chmod u+rw {{dosya_veya_dizin/yolu}}`

- Gruptan ve diğerlerinden çalıştırma iznini kaldır:

`chmod g-x,o-x {{dosya/yolu}}`

- Tüm kullanıcılara okuma ve çalıştırma izni ver:

`chmod a+rx {{dosya/yolu}}`

- Diğerlerine (dosya sahibinin grubunda olmayanlara) grupla aynı izinleri ver:

`chmod o=g {{dosya/yolu}}`

- Diğerlerinin tüm izinlerini kaldır:

`chmod o= {{dosya/yolu}}`

- İzinleri sekizlik gösterimle ayarla:

`chmod {{644}} {{dosya/yolu}}`

- Dosyalar için tüm kullanıcılara özyinelemeli olarak okuma izni ver. Ayrıca en az bir çalıştırma izni olan dosyalara ve tüm alt dizinlere çalıştırma izni ver:

`chmod {{[-R|--recursive]}} a+rX {{dizin/yolu}}`
