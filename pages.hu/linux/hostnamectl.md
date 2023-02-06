# hostnamectl

> A számítógép hostnevének lekérése vagy beállítása. További információ: <https://manned.org/hostnamectl>.

- A számítógép állomásnevének lekérdezése:

`hostnamectl`

- A számítógép állomásnevének beállítása:

`sudo hostnamectl set-hostname "{{hostname}}"`

- Szép hostnév beállítása a számítógéphez:

`sudo hostnamectl set-hostname --static "{{hostname.example.com}}" && sudo hostnamectl set-hostname --pretty "{{hostname}}"`

- A hosztnév alapértelmezett értékre történő visszaállítása:

`sudo hostnamectl set-hostname --pretty ""`
