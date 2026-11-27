# ansible

> Bilgisayar gruplarını SSH üzerinden uzaktan yönet (yeni gruplar/ana makineler eklemek için `/etc/ansible/hosts` dosyasını kullan).
> `galaxy` gibi bazı alt komutların kendi kullanım dokümantasyonu vardır.
> Daha fazla bilgi için: <https://docs.ansible.com/projects/ansible/latest/cli/ansible.html>.

- Bir gruba ait ana makineleri listele:

`ansible {{grup}} --list-hosts`

- Bir ana makine grubuna ping modülünü çağırarak ping at:

`ansible {{grup}} {{[-m|--module-name]}} ping`

- Bir ana makine grubu hakkındaki bilgileri (facts) setup modülünü çağırarak göster:

`ansible {{grup}} {{[-m|--module-name]}} setup`

- Bir ana makine grubunda command modülünü argümanlarla çağırarak komut çalıştır:

`ansible {{grup}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{komut}}'`

- Bir komutu yönetici yetkileriyle çalıştır:

`ansible {{grup}} {{[-b|--become]}} --ask-become-pass {{[-m|--module-name]}} command {{[-a|--args]}} '{{komut}}'`

- Bir komutu özel bir envanter dosyasıyla çalıştır:

`ansible {{grup}} {{[-i|--inventory]}} {{envanter_dosyası}} {{[-m|--module-name]}} command {{[-a|--args]}} '{{komut}}'`

- Bir envanterdeki grupları listele:

`ansible localhost {{[-m|--module-name]}} debug {{[-a|--args]}} '{{var=groups.keys()}}'`
