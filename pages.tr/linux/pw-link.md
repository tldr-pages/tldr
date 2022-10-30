# pw-link

> PipeWire'daki portlar arası linkleri yönet.
> Daha fazla bilgi için: <https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Virtual-Devices>.

- Tüm ses çıktı ve girdi portlarını sırala:

`pw-link --output --input'`

- Çıktı ve girdi portları arasında bir bağlantı yarat:

`pw-link {{çıktı_port_ismi}} {{girdi_port_ismi}}`

- Disconnect two ports:

`pw-link --disconnect {{çıktı_port_ismi}} {{girdi_port_ismi}}`

- Yardım sayfası göster:

`pw-link -h`
