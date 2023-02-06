# rdesktop

> Távoli asztali protokoll kliens. Az RDP protokollt használó távoli számítógéphez való csatlakozáshoz használható. További információ: <https://manned.org/rdesktop>.

- Csatlakozás a távoli számítógéphez (alapértelmezett port: 3389):

`rdesktop -u {{username}} -p {{password}} {{host:port}}`

- Egyszerű példák:

`rdesktop -u Administrator -p passwd123 192.168.1.111:3389`

- Csatlakozás egy távoli számítógéphez teljes képernyővel (a `Ctrl + Alt + Enter` megnyomásával létezik):

`rdesktop -u {{username}} -p {{password}} -f {{host:port}}`

- Használja a testreszabott felbontást (használja az 'x' betűt a számok között):

`rdesktop -u {{username}} -p {{password}} -g 1366x768 {{host:port}}`

- Csatlakozás távoli számítógéphez tartományi felhasználóval:

`rdesktop -u {{username}} -p {{password}} -d {{domainname}} {{host:port}}`

- Használja a 16 bites színt (gyorsítás):

`rdesktop -u {{username}} -p {{password}} -a 16 {{host:port}}`
