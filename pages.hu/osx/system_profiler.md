# system_profiler

> A rendszer hardver- és szoftverkonfigurációjának jelentése. További információ: <https://ss64.com/osx/system_profiler.html>.

- Teljes rendszerprofil-jelentést jelenít meg, amely a System Profiler.app alkalmazással nyitható meg:

`system_profiler -xml > MyReport.spx`

- Hardveres áttekintés megjelenítése (modell, CPU, memória, soros stb.):

`system_profiler SPHardwareDataType`

- A rendszer sorozatszámának kinyomtatása:

`system_profiler SPHardwareDataType|grep "Serial Number (system)" | awk '{ print $4 }'`
