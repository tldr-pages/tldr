# iwinfo

> Recupera información sobre interfaces inalámbricas en OpenWrt.
> Más información: <https://openwrt.org/docs/guide-developer/ubus/iwinfo>.

- Lista todas las interfaces inalámbricas disponibles:

`iwinfo`

- Muestra información detallada sobre una interfaz inalámbrica específica:

`iwinfo {{interfaz}} info`

- Busca redes inalámbricas cercanas visibles para la interfaz:

`iwinfo {{interface}} scan`

- Lista dispositivos conectados:

`iwinfo {{interface}} assoclist`

- Lista canales soportados por la interfaz:

`iwinfo {{interface}} freqlist`

- Lista niveles de potencia de transmisión disponibles para la interfaz:

`iwinfo {{interface}} txpowerlist`
