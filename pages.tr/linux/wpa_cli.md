# wpa_cli

> Kablosuz LAN arayüzleri ekleyin ve yapılandırın.
> Daha fazla bilgi için: <https://manned.org/wpa_cli>.

- Kullanılabilir ağları tara:

`sudo wpa_cli scan`

- Tarama sonuçlarını göster:

`sudo wpa_cli scan_results`

- Ağ ekle:

`sudo wpa_cli {{[add_n|add_network]}} {{numara}}`

- Bir ağın SSID değerini ayarla:

`sudo wpa_cli {{[set_n|set_network]}} {{numara}} ssid "{{SSID}}"`

- Ağı etkinleştir:

`sudo wpa_cli {{[en|enable_network]}} {{numara}}`

- Yapılandırmayı kaydet:

`sudo wpa_cli {{[sa|save_config]}}`
