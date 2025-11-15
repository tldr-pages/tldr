# vol.py

> Framework forensics usado para analizar volcados de memoria volátil (RAM).
> Con volatility3, los complementos ahora se basan en el sistema operativo. Los ejemplos a continuación usarán Windows.
> Más información: <https://volatility3.readthedocs.io/en/latest/index.html>.

- Obtiene información sobre un archivo de volcado de memoria:

`python3 vol.py {{[-f|--filename]}} {{ruta/al/archivo_de_volcado_de_memoria}} windows.info`

- Lista procesos activos:

`python3 vol.py {{[-f|--filename]}} {{ruta/al/archivo_de_volcado_de_memoria}} windows.pslist`

- Lista hashes de usuarios en el sistema:

`python3 vol.py {{[-f|--filename]}} {{ruta/al/archivo_de_volcado_de_memoria}} windows.hashdump`

- Lista conexiones de red activas:

`python3 vol.py {{[-f|--filename]}} {{ruta/al/archivo_de_volcado_de_memoria}} windows.netstat`

- Muestra la ayuda:

`python3 vol.py {{[-h|--help]}}`
