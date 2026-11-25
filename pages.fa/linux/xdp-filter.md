# xdp-filter

> بارگذاری و مدیریت فیلتر بستهٔ eBPF XDP.
> بخشی از مجموعهٔ xdp-tools است.
> اطلاعات بیشتر: <https://github.com/xdp-project/xdp-tools/tree/main/xdp-filter#running-xdp-filter>.

- بارگذاری فیلتر روی واسط در حالت skb (عمومی) با سیاست پیش‌فرض اجازه:

`sudo xdp-filter load {{[-p|--policy]}} allow {{[-m|--mode]}} skb {{network_interface}}`

- برداشتن فیلتر از واسط:

`sudo xdp-filter unload {{network_interface}}`

- منع ترافیک به پورت مقصد مشخص:

`sudo xdp-filter port {{destination_port}}`

- منع ترافیک از آدرس IP مبدأ مشخص:

`sudo xdp-filter ip {{[-m|--mode]}} src {{source_ip}}`

- منع ترافیک از آدرس MAC مبدأ مشخص:

`sudo xdp-filter ether {{[-m|--mode]}} src {{mac_address}}`

- پرس‌وجوی بسته‌ها و نمایش آمار هر ۱۰۰۰۰ میلی‌ثانیه:

`sudo xdp-filter poll {{[-i|--interval]}} 10000`
