# dnf group

> Fedora tabanlı sistemlerde paketlerin sanal koleksiyonlarını yönetmek için kullanılır.
> Daha fazla bilgi için: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- DNF gruplarını listele, kurulu ve kurulmamış durumları tabloda göster:

`dnf {{[grp|group]}} list`

- DNF grup bilgilerini göster, depo ve isteğe bağlı paketler dahil:

`dnf {{[grp|group]}} info {{grup_adi}}`

- DNF grubunu kur:

`dnf {{[grp|group]}} install {{grup_adi}}`

- DNF grubunu kaldır:

`dnf {{[grp|group]}} remove {{grup_adi}}`

- DNF grubunu yükselt:

`dnf {{[grp|group]}} upgrade {{grup_adi}}`
