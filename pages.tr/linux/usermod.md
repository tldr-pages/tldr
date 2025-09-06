# usermod

> Bir kullanıcı hesabını düzenleyin
> Ayrıca bakınız: `users`, `useradd`, `userdel`.
> Daha fazla bilgi için: <https://manned.org/usermod>.

- Kullanıcı adını değiştirin:

`sudo usermod {{[-l|--login]}} {{yeni_kullanıcı_adı}} {{kullanıcı_adı}}`

- Kullanıcı ID'sini değiştirin:

`sudo usermod {{[-u|--uid]}} {{id}} {{kullanıcı_adı}}`

- Kullanıcı kabuğunu değiştirin:

`sudo usermod {{[-s|--shell]}} {{kabuk/yolu}} {{kullanıcı_adı}}`

- Kullanıcıyı ek gruplara ekleyin (boşluk olmamasına dikkat edin):

`sudo usermod {{[-aG|--append --groups]}} {{grup1,grup2,...}} {{kullanıcı_adı}}`

- Bir gruptan belirtilen kullanıcıyı kaldırın:

`sudo usermod {{[-rG --remove --groups]}} {{grup1,grup2,...}} {{kullanıcı_adı}}`

- Kullanıcı ev dizinini değiştirin:

`sudo usermod {{[-m|--move-home]}} {{[-d|--home]}} {{yeni_ev/dizin/yolu}} {{kullanıcı_adı}}`

- Hesabı kilitleyin:

`sudo usermod {{[-L|--lock]}} {{kullanıcı_adı}}`

- Hesabın kilidini açın:

`sudo usermod {{[-U|--unlock]}} {{kullanıcı_adı}}`
