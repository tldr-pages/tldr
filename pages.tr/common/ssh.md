# ssh

> Secure Shell, uzak sistemlere güvenli bağlantı kurmak için kullanılan bir protokoldür.
> Uzak sunucuda oturum açmak veya komut çalıştırmak için kullanılabilir.
> Daha fazla bilgi için: <https://man.openbsd.org/ssh>.

- Uzak bir sunucuya bağlan:

`ssh {{kullanici}}@{{uzak_sunucu}}`

- Belirli bir kimlik dosyası (özel anahtar) ile uzak sunucuya bağlan:

`ssh {{kullanici}}@{{uzak_sunucu}} -i {{anahtar/dosyasi/yolu}}`

- `10.0.0.1` IP adresli uzak sunucuya belirli bir port ile bağlan (Not: `10.0.0.1` kısaltılarak `10.1` yazılabilir):

`ssh {{kullanici}}@10.0.0.1 -p {{2222}}`

- Uzak sunucuda etkileşimli komut çalıştırmak için tty tahsisi ile bağlan:

`ssh {{kullanici}}@{{uzak_sunucu}} -t {{komut}} {{komut_argumanlari}}`

- SSH tünelleme: Dinamik port yönlendirme (`localhost:1080` üzerinde SOCKS proxy):

`ssh {{kullanici}}@{{uzak_sunucu}} -D {{1080}}`

- SSH tünelleme: Belirli bir portu yönlendir (`localhost:9999`'dan `example.org:80`'e), sahte tty tahsisini ve uzak komut çalıştırmayı devre dışı bırak:

`ssh {{kullanici}}@{{uzak_sunucu}} -L {{9999}}:{{example.org}}:{{80}} -N -T`

- SSH atlama: Bir atlama sunucusu üzerinden uzak sunucuya bağlan (birden fazla atlama virgülle ayrılabilir):

`ssh {{kullanici}}@{{uzak_sunucu}} -J {{kullanici}}@{{atlama_sunucusu}}`

- Takılmış bir oturumu kapat:

`<Enter><~><.>`
