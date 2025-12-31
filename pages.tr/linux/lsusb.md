# lsusb

> USB girişleri ve girişlere bağlı olan cihazlar hakkında bilgi görüntüleyin.
> Daha fazla bilgi için: <https://manned.org/lsusb>.

- Mevcut tüm USB aygıtlarını listeleyin:

`lsusb`

- USB aygıtlarını ağaç hiyerarşisi görünümünde listeleyin:

`lsusb {{[-t|--tree]}}`

- USB aygıtları hakkında ayrıntılı bilgileri görüntüleyin:

`lsusb {{[-v|--verbose]}}`

- Bir USB aygıtı hakkında ayrıntılı bilgileri görüntüleyin:

`lsusb {{[-v|--verbose]}} -s {{giriş}}:{{cihaz numarası}}`

- Sadece belirli satıcı ve cihaz ID'sine sahip aygıtları listeleyin:

`lsusb -d {{satıcı}}:{{cihaz}}`
