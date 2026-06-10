# ntp-ctl

> Կառավարման հաճախորդ `ntpd-rs` դեյմոնի համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.ntpd-rs.pendulum-project.org/man/ntp-ctl.8/>:.

- Ցուցադրել տեղեկատվություն NTP դեյմոնի ներկայիս վիճակի մասին.:

`ntp-ctl status`

- Ստուգեք, արդյոք նշված կազմաձևման ֆայլը (կանխադրված՝ `/etc/ntpd-rs/ntp.toml`) վավեր է.:

`ntp-ctl {{[-c|--config]}} {{path/to/config}} validate`

- Ինտերակտիվ կերպով գործարկել ժամացույցի մեկ համաժամացումը.:

`sudo ntp-ctl force-sync`
