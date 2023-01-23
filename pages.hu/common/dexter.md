# dexter

> Eszköz a kubectl felhasználók hitelesítésére az OpenId Connect segítségével. További információ: <https://github.com/gini/dexter>.

- Felhasználó létrehozása és hitelesítése a Google OIDC segítségével:

`dexter auth -i {{client_id}} -s {{client_secret}}`

- Az alapértelmezett kube konfigurációs hely felülírása:

`dexter auth -i {{client_id}} -s {{client_secret}} --kube-config {{sample/config}}`
