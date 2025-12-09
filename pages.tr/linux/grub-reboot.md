# grub-reboot

> GRUB için varsayılan önyükleme girişini ayarlayın, sadece sonraki önyükleme için.
> Daha fazla bilgi için: <https://manned.org/grub-reboot>.

- Bir sonraki önyükleme için önyükleme girişini bir giriş numarasına, isime veya bir tanımlayıcıya ayarlayın:

`sudo grub-reboot {{giriş_numarası}}`

- Bir sonraki önyükleme için alternatif önyükleme dizinin, önyükleme girişini bir giriş numarasına, isime veya bir tanımlayıcıya ayarlayın:

`sudo grub-reboot --boot-directory /{{önyükleme/dizini/yolu}} {{giriş_numarası}}`
