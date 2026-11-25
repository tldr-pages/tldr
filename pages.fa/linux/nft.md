# nft

> امکان پیکربندی جدول‌ها، زنجیره‌ها و قوانین ارائه‌شده توسط دیوار آتش هستهٔ لینوکس.
> Nftables جایگزین iptables است.
> اطلاعات بیشتر: <https://wiki.nftables.org/wiki-nftables/index.php/Main_Page>.

- مشاهدهٔ پیکربندی فعلی:

`sudo nft list ruleset`

- افزودن جدول جدید با خانوادهٔ «inet» و جدول «filter»:

`sudo nft add table {{inet}} {{filter}}`

- افزودن زنجیرهٔ جدید برای پذیرش همهٔ ترافیک ورودی:

`sudo nft add chain {{inet}} {{filter}} {{input}} \{ type {{filter}} hook {{input}} priority {{0}} \; policy {{accept}} \; \}`

- افزودن قانون جدید برای پذیرش چند پورت TCP:

`sudo nft add rule {{inet}} {{filter}} {{input}} {{tcp}} {{dport \{ telnet, ssh, http, https \} accept}}`

- افزودن قانون NAT برای ترجمهٔ همهٔ ترافیک زیرشبکهٔ `192.168.0.0/24` به IP عمومی میزبان:

`sudo nft add rule {{nat}} {{postrouting}} ip saddr {{192.168.0.0/24}} {{masquerade}}`

- نمایش شناسه‌های قوانین:

`sudo nft --handle --numeric list chain {{family}} {{table}} {{chain}}`

- حذف قانون:

`sudo nft delete rule {{inet}} {{filter}} {{input}} handle {{3}}`

- ذخیرهٔ پیکربندی فعلی:

`sudo nft list ruleset >{{/etc/nftables.conf}}`
