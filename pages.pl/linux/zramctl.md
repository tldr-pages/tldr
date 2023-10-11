# zramctl

> Tworzenie i kontrola urządzeń zram.
> Użyj `mkfs` lub `mkswap` aby sformatować urządzenia zram na partycje.
> Więcej informacji: <https://manned.org/zramctl>.

- Sprawdzenie, czy zram jest włączony:

`lsmod | grep -i zram`

- Włączenie zram z dynamiczną liczbą urządzeń (użyj `zramctl` aby skonfigurować urządzenia dalej):

`sudo modprobe zram`

- Włączenie zram z dokładnie 2 urządzeniami:

`sudo modprobe zram num_devices={{2}}`

- Znalezienie i inicjalizacja następnego wolnego urządzenia zram jako 2 GB napęd wirtualny z użyciem kompresji LZ4:

`sudo zramctl --find --size {{2GB}} --algorithm {{lz4}}`

- Wyświetlenie aktualnie zainicjalizowanych urządzeń:

`zramctl`
