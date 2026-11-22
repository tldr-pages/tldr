# scp

> Güvenli kopyalama.
> SSH üzerinden Secure Copy Protocol kullanarak ana makineler arasında dosya kopyala.
> Daha fazla bilgi için: <https://man.openbsd.org/scp>.

- Yerel bir dosyayı uzak bir ana makineye kopyala:

`scp {{yol/yerel_dosya}} {{uzak_ana_makine}}:{{yol/uzak_dosya}}`

- Uzak ana makineye bağlanırken belirli bir port kullan:

`scp -P {{port}} {{yol/yerel_dosya}} {{uzak_ana_makine}}:{{yol/uzak_dosya}}`

- Uzak bir ana makinedeki dosyayı yerel bir dizine kopyala:

`scp {{uzak_ana_makine}}:{{yol/uzak_dosya}} {{yol/yerel_dizin}}`

- Uzak bir ana makinedeki bir dizinin içeriğini yerel bir dizine yinelemeli olarak kopyala:

`scp -r {{uzak_ana_makine}}:{{yol/uzak_dizin}} {{yol/yerel_dizin}}`

- İki uzak ana makine arasında dosyayı yerel ana makine üzerinden aktararak kopyala:

`scp -3 {{ana_makine1}}:{{yol/uzak_dosya}} {{ana_makine2}}:{{yol/uzak_dizin}}`

- Uzak ana makineye bağlanırken belirli bir kullanıcı adı kullan:

`scp {{yol/yerel_dosya}} {{uzak_kullanıcı_adı}}@{{uzak_ana_makine}}:{{yol/uzak_dizin}}`

- Uzak ana makineyle kimlik doğrulaması için belirli bir SSH özel anahtarı kullan:

`scp -i {{~/.ssh/özel_anahtar}} {{yol/yerel_dosya}} {{uzak_ana_makine}}:{{yol/uzak_dosya}}`

- Uzak ana makineye bağlanırken belirli bir proxy kullan:

`scp -J {{proxy_kullanıcı_adı}}@{{proxy_ana_makine}} {{yol/yerel_dosya}} {{uzak_ana_makine}}:{{yol/uzak_dosya}}`
