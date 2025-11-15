# nmcli radio

> Zobrazit stav rádiových přepínačů nebo je povolit/zakázat pomocí NetworkManageru.
> Více informací: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmcli.html#radio>.

- Zobrazit stav Wi-Fi:

`nmcli {{[r|radio]}} {{[w|wifi]}}`

- Zapnout nebo vypnout Wi-Fi:

`nmcli {{[r|radio]}} {{[w|wifi]}} {{on|off}}`

- Zobrazit stav WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}}`

- Zapnout nebo vypnout WWAN:

`nmcli {{[r|radio]}} {{[ww|wwan]}} {{on|off}}`

- Zobrazit stav obou přepínačů:

`nmcli {{[r|radio]}}`

- Zapnout nebo vypnout oba přepínače:

`nmcli {{[r|radio]}} {{[a|all]}} {{on|off}}`
