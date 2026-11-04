# chown

> Dosyaların ve dizinlerin kullanıcı ve grup sahipliğini değiştir.
> Ayrıca bakınız: `chgrp`.
> Daha fazla bilgi için: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Bir dosyanın/dizinin sahibi olan kullanıcıyı değiştir:

`sudo chown {{kullanıcı}} {{dosya_veya_dizin/yolu}}`

- Bir dosyanın/dizinin sahibi olan kullanıcıyı ve grubu değiştir:

`sudo chown {{kullanıcı}}:{{grup}} {{dosya_veya_dizin/yolu}}`

- Sahip kullanıcıyı ve grubu, ikisi de `kullanıcı` adını taşıyacak şekilde değiştir:

`sudo chown {{kullanıcı}}: {{dosya_veya_dizin/yolu}}`

- Bir dosyanın grubunu, mevcut kullanıcının üyesi olduğu bir grupla değiştir:

`chown :{{grup}} {{dosya_veya_dizin/yolu}}`

- Bir dizinin ve içeriğinin sahibini özyinelemeli olarak değiştir:

`sudo chown {{[-R|--recursive]}} {{kullanıcı}} {{dizin/yolu}}`

- Bir sembolik bağlantının sahibini değiştir:

`sudo chown {{[-h|--no-dereference]}} {{kullanıcı}} {{sembolik_bağlantı/yolu}}`

- Bir dosyanın/dizinin sahibini bir referans dosyasıyla aynı olacak şekilde değiştir:

`sudo chown --reference {{referans_dosyası/yolu}} {{dosya_veya_dizin/yolu}}`
