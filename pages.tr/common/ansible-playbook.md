# ansible-playbook

> Playbook'ta tanımlanan görevleri uzak makinelerde SSH üzerinden çalıştır.
> Daha fazla bilgi için: <https://docs.ansible.com/projects/ansible/latest/cli/ansible-playbook.html>.

- Playbook'taki görevleri çalıştır:

`ansible-playbook {{playbook}}`

- Playbook'taki görevleri özel bir ana makine envanteriyle çalıştır:

`ansible-playbook {{playbook}} {{[-i|--inventory]}} {{envanter_dosyası}}`

- Playbook'taki görevleri komut satırında tanımlanan ek değişkenlerle çalıştır:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "{{değişken1}}={{değer1}} {{değişken2}}={{değer2}}"`

- Playbook'taki görevleri bir JSON dosyasında tanımlanan ek değişkenlerle çalıştır:

`ansible-playbook {{playbook}} {{[-e|--extra-vars]}} "@{{değişkenler.json}}"`

- Playbook'ta yalnızca belirtilen etiketlere sahip görevleri çalıştır:

`ansible-playbook {{playbook}} {{[-t|--tags]}} {{etiket1,etiket2}}`

- Playbook'u belirli bir görevden başlayarak çalıştır:

`ansible-playbook {{playbook}} --start-at {{görev_adı}}`

- Playbook'taki görevleri hiçbir değişiklik yapmadan deneme amacıyla çalıştır:

`ansible-playbook {{playbook}} {{[-C|--check]}} {{[-D|--diff]}}`
