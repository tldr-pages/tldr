# github-label-sync

> GitHub etiketlerini senkronize etmeye yarayan komut satırı arayüzü.
> Daha fazla bilgi için: <https://github.com/Financial-Times/github-label-sync>.

- Yerel bir `labels.json` dosyası kullanarak etiketleri senkronize et:

`github-label-sync --access-token {{token}} {{depo_ismi}}`

- Belirli bir etiketlenen JSON dosyası kullanarak etiketleri senkronize et:

`github-label-sync --access-token {{token}} --labels {{url|örnek/json_dosyası}} {{depo_ismi}}`

- Programı etiketleri gerçekten senkronize etmeden çalıştır:

`github-label-sync --access-token {{token}} --dry-run {{depo_ismi}}`

- `labels.json` içinde olmayan etiketleri sakla:

`github-label-sync --access-token {{token}} --allow-added-labels {{depo_ismi}}`

- `GITHUB_ACCESS_TOKEN` ortam değişkenini kullanarak senkronize et:

`github-label-sync {{depo_ismi}}`
