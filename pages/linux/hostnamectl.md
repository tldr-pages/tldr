# hostnamectl

> Get or set the hostname of the computer.
> More information: <https://manned.org/hostnamectl>.

- Get the hostname of the computer:

`hostnamectl`

- Set the hostname of the computer:

`sudo hostnamectl set-hostname "{{hostname}}"`

- Set a pretty hostname for the computer:

`sudo hostnamectl set-hostname --static "{{hostname.example.com}}" && sudo hostnamectl set-hostname --pretty "{{hostname}}"`

- Reset hostname to its default value:

`sudo hostnamectl set-hostname --pretty ""`
