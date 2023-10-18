# hostnamectl

> Wyświetl lub ustaw nazwę hosta tego komputera.
> Więcej informacji: <https://manned.org/hostnamectl>.

- Wyświetl nazwę hosta tego komputera:

`hostnamectl`

- Ustaw nazwę hosta tego komputera:

`sudo hostnamectl set-hostname "{{nazwa_hosta}}"`

- Ustaw ładną nazwę hosta tego komputera:

`sudo hostnamectl set-hostname --static "{{nazwa_hosta.example.com}}" && sudo hostnamectl set-hostname --pretty "{{nazwa_hosta}}"`

- Zresetuj nazwę hosta do jej domyślnej wartości:

`sudo hostnamectl set-hostname --pretty ""`
