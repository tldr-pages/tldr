# kube-fzf

> Shell parancsok a Kubernetes Podok parancssori fuzzy kereséséhez. Lásd még: `kubectl` a kapcsolódó parancsokat. További információ: <https://github.com/thecasualcoder/kube-fzf>.

- Pod részletek lekérdezése (az aktuális névtérből):

`findpod`

- Get pod details (az összes névtérből):

`findpod -a`

- Egy pod leírása:

`describepod`

- Tail pod naplók:

`tailpod`

- Belépés egy pod konténerbe:

`execpod {{shell_command}}`

- Egy pod port-továbbítása:

`pfpod {{port_number}}`
