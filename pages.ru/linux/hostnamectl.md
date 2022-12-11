# hostnamectl

> Получение и установка имени хоста компьютера.
> Больше информации: <https://manned.org/hostnamectl>.

- Получить имя хоста компьютера:

`hostnamectl`

- Задать имя хоста компьютера:

`sudo hostnamectl set-hostname "{{имя_хоста}}"`

- Задать красивое (короткое) имя хоста компьютера:

`sudo hostnamectl set-hostname --static "{{имя_хоста.example.com}}" && sudo hostnamectl set-hostname --pretty "{{имя_хоста}}"`

- Сбросить имя хоста компьютера к значению по умолчанию:

`sudo hostnamectl set-hostname --pretty ""`
