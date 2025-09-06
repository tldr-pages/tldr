# dnf module

> Paket modülerliğini yönetmek için kullanılır.
> Daha fazla bilgi için: <https://dnf.readthedocs.io/en/latest/command_ref.html#module-command>.

- Modülerlik genel görünümünü göster:

`dnf module list`

- Belirli bir programın modülerliğini göster:

`dnf module list {{paket_adi}}`

- Bir paketi etkinleştirilecek şekilde ayarla:

`sudo dnf module enable {{paket_adi}}:{{stream}}`

- Belirli bir sürümü etkinleştir ve kur:

`dnf module install {{paket_adi}}:{{stream}}`
