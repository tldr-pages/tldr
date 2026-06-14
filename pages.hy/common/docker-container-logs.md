# դոկեր կոնտեյների տեղեկամատյաններ

> Տպել բեռնարկղերի տեղեկամատյանները:.
> Լրացուցիչ տեղեկություններ. <https://docs.docker.com/reference/cli/docker/container/logs/>:.

- Տպել տեղեկամատյանները կոնտեյներից.:

`docker {{[logs|container logs]}} {{name|id}}`

- Տպեք տեղեկամատյանները և հետևեք դրանց.:

`docker {{[logs|container logs]}} {{name|id}} {{[-f|--follow]}}`

- Տպել վերջին 5 տողերը.:

`docker {{[logs|container logs]}} {{name|id}} {{[-n|--tail]}} 5`

- Տպեք տեղեկամատյանները և կցեք դրանք ժամանակային դրոշմանիշներով.:

`docker {{[logs|container logs]}} {{name|id}} {{[-t|--timestamps]}}`

- Տպել տեղեկամատյանները կոնտեյների կատարման ժամանակի որոշակի կետից (այսինքն՝ 23 մ, 10 վրկ, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{name|id}} --until {{time}}`
