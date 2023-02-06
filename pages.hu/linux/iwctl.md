# iwctl

> Parancssori eszköz az iwd hálózati supplicant vezérlésére. További információ: <https://iwd.wiki.kernel.org/gettingstarted>.

- Indítsa el az interaktív üzemmódot, ebben az üzemmódban közvetlenül, automatikus kiegészítéssel adhatja meg a parancsokat:

`iwctl`

- Hívja fel az általános súgót:

`iwctl --help`

- A Wi-Fi állomások megjelenítése:

`iwctl station list`

- Kezdje el a hálózatok keresését egy állomással:

`iwctl station {{station}} scan`

- Az állomás által megtalált hálózatok megjelenítése:

`iwctl station {{station}} get-networks`

- Csatlakozás egy hálózathoz egy állomással, ha hitelesítő adatokra van szükség, akkor azokat a rendszer kéri:

`iwctl station {{station}} connect {{network_name}}`
