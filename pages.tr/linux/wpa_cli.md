# wpa_cli

> Kablosuz LAN arayüzleri ekleyin ve yapılandırın.
> Daha fazla bilgi için: <https://manned.org/wpa_cli>.

- Kullanılabilir ağları tara:

`wpa_cli scan`

- Tarama sonuçlarını göster:

`wpa_cli scan_results`

- Ağ ekle:

`wpa_cli add_network {{numara}}`

- Bir ağın SSID değerini ayarla:

`wpa_cli set_network {{numara}} ssid "{{SSID}}"`

- Ağı etkinleştir:

`wpa_cli enable_network {{numara}}`

- Yapılandırmayı kaydet:

`wpa_cli save_config`
