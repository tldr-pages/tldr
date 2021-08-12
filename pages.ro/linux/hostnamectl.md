# hostnamectl

> Obțineți sau setați numele de gazdă al computerului.

- Obțineți numele de gazdă al computerului:

`hostnamectl`

- Setați numele de gazdă al computerului:

`sudo hostnamectl set-hostname "{{hostname}}"`

- Setați un nume de gazdă destul pentru computer:

`sudo hostnamectl set-hostname --static "{{hostname.example.com}}" && sudo hostnamectl set-hostname --pretty "{{hostname}}"`

- Resetați numele gazdei la valoarea implicită:

`sudo hostnamectl set-hostname --pretty ""`
