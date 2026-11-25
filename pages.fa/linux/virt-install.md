# virt-install

> ایجاد ماشین‌های مجازی با libvirt و شروع نصب سیستم‌عامل.
> توجه: ممکن است لازم باشد `--connect URI` را به دستورها بدهید یا URI را در `$XDG_CONFIG_HOME/libvirt/libvirt.conf` تنظیم کنید.
> اطلاعات بیشتر: <https://manned.org/virt-install>.

- ایجاد ماشین مجازی با ۱ گیگابایت RAM و ۱۲ گیگابایت فضای ذخیره‌سازی و شروع نصب Debian:

`virt-install {{[-n|--name]}} {{vm_name}} --memory {{1024}} --disk path={{path/to/image.qcow2}},size={{12}} {{[-c|--cdrom]}} {{path/to/debian.iso}}`

- ایجاد ماشین مجازی x86-64 مبتنی بر UEFI با شتاب‌دهی KVM، چیپست Q35، چهار GiB حافظهٔ RAM و ۱۶ GiB فضای ذخیره‌سازی RAW و شروع نصب Fedora:

`virt-install {{[-n|--name]}} {{vm_name}} --arch {{x86_64}} --virt-type {{kvm}} --machine {{q35}} --boot {{uefi}} --memory {{4096}} --disk path={{path/to/image.raw}},size={{16}} {{[-c|--cdrom]}} {{path/to/fedora.iso}}`

- ایجاد ماشین مجازی زنده و بدون دیسک، بدون دستگاه صدای شبیه‌سازی‌شده یا کنترل‌کنندهٔ USB؛ بدون شروع نصب یا اتصال خودکار به کنسول، اما با اتصال CD-ROM (مثلاً برای استفاده از CD زنده‌ای مانند tails):

`virt-install {{[-n|--name]}} {{vm_name}} --memory {{512}} --disk {{none}} --controller {{type=usb,model=none}} --sound {{none}} --autoconsole {{none}} --install {{no_install=yes}} {{[-c|--cdrom]}} {{path/to/tails.iso}}`

- ایجاد ماشین مجازی با ۱۶ GiB حافظهٔ RAM، فضای ذخیره‌سازی ۲۵۰ GiB، هشت هسته با hyperthreading، توپولوژی مشخص CPU و مدلی که بیشتر ویژگی‌های CPU میزبان را دارد:

`virt-install {{[-n|--name]}} {{vm_name}} --cpu {{host-model}},topology.sockets={{1}},topology.cores={{4}},topology.threads={{2}} --memory {{16384}} --disk path={{path/to/image.qcow2}},size={{250}} {{[-c|--cdrom]}} {{path/to/debian.iso}}`

- ایجاد ماشین مجازی و شروع استقرار خودکار مبتنی بر Fedora 43 فقط با منابع راه دور (بدون نیاز به ISO):

`virt-install {{[-n|--name]}} {{vm_name}} --memory {{2048}} --disk path={{path/to/image.qcow2}},size={{20}} {{[-l|--location]}} {{https://download.fedoraproject.org/pub/fedora/linux/releases/43/Everything/x86_64/os/}} {{[-x|--extra-args]}} "{{inst.ks=https://example.com/path/to/kickstart.ks}}"`
