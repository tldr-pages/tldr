# gitlab-ctl

> Կառավարեք GitLab omnibus-ը:.
> Լրացուցիչ տեղեկություններ. <https://docs.gitlab.com/omnibus/maintenance/>:.

- Ցուցադրել յուրաքանչյուր ծառայության կարգավիճակը.:

`sudo gitlab-ctl status`

- Ցուցադրել որոշակի ծառայության կարգավիճակը.:

`sudo gitlab-ctl status {{nginx}}`

- Վերագործարկեք յուրաքանչյուր ծառայություն.:

`sudo gitlab-ctl restart`

- Վերագործարկեք հատուկ ծառայություն.:

`sudo gitlab-ctl restart {{nginx}}`

- Ցուցադրեք յուրաքանչյուր ծառայության մատյանները և շարունակեք կարդալ, մինչև սեղմվի `<Ctrl c>`:

`sudo gitlab-ctl tail`

- Ցուցադրել որոշակի ծառայության տեղեկամատյանները.:

`sudo gitlab-ctl tail {{nginx}}`

- Ուղարկեք SIGKILL ազդանշանը կոնկրետ ծառայությանը.:

`sudo gitlab-ctl kill {{nginx}}`

- Վերակազմավորեք հավելվածը.:

`sudo gitlab-ctl reconfigure`
