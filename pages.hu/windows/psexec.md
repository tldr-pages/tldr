# psexec

> Egy parancssori folyamat végrehajtása egy távoli gépen. Ez egy fejlett parancs, és potenciálisan veszélyes lehet. További információ: <https://learn.microsoft.com/en-us/sysinternals/downloads/psexec>.

- Parancs végrehajtása a `cmd` segítségével egy távoli héjban:

`psexec \\{{remote_host}} cmd`

- Parancs végrehajtása egy távoli állomáson (előzetesen hitelesített):

`psexec \\{{remote_host}} -u {{user_name}} -p {{password}}`

- Egy parancs távoli végrehajtása és az eredmény kiadása egy fájlba:

`psexec \\{{remote_host}} cmd /c {{command}} -an ^>{{path/to/file.txt}}`

- Egy program végrehajtása a felhasználókkal való interakcióhoz:

`psexec \\{{remote_host}} -d -i {{program_name}}`

- A távoli állomás IP-konfigurációjának megjelenítése:

`psexec \\{{remote_host}} ipconfig /all`
