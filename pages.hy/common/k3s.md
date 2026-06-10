# k3s

> Տեղադրեք և կառավարեք թեթև Kubernetes կլաստերները:.
> Լրացուցիչ տեղեկություններ. <https://docs.k3s.io/cli>:.

- Գործարկեք ներկառուցված `kubectl` հրամանը՝:

`k3s kubectl get nodes`

- Վերցրեք կլաստերի etcd պատկերը.:

`k3s etcd-snapshot save`

- Պտտեցնել CA վկայագիրը.:

`k3s certificate rotate-ca`

- Կառավարեք bootstrap նշանները.:

`k3s token list`

- Տեղահանեք K3-ները և հեռացրեք բոլոր բաղադրիչները.:

`k3s-uninstall.sh`
