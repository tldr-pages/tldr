# act

> GitHub Actions iş akışlarını Docker kullanarak yerel olarak çalıştır.
> Daha fazla bilgi için: <https://manned.org/act>.

- Kullanılabilir görevleri listele:

`act {{[-l|--list]}}`

- Varsayılan olayı çalıştır:

`act`

- Belirli bir olayı çalıştır:

`act {{event_turu}}`

- Belirli bir görevi çalıştır:

`act {{[-j|--job]}} {{gorev_id}}`

- Eylemleri gerçekten çalıştırma (yani bir deneme/kuru çalıştır):

`act {{[-n|--dryrun]}}`

- Ayrıntılı güncükleri göster:

`act {{[-v|--verbose]}}`

- Belirli bir iş akışını push olayıyla çalıştır:

`act push {{[-W|--workflows]}} {{path/to/workflow}}`
