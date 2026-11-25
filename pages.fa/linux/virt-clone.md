# virt-clone

> شبیه‌سازی ماشین مجازی libvirt.
> اطلاعات بیشتر: <https://manned.org/virt-clone>.

- شبیه‌سازی ماشین مجازی و تولید خودکار نام، مسیر ذخیره‌سازی و آدرس MAC جدید:

`virt-clone {{[-o|--original]}} {{vm_name}} --auto-clone`

- شبیه‌سازی ماشین مجازی با تعیین نام، مسیر ذخیره‌سازی و آدرس MAC جدید:

`virt-clone {{[-o|--original]}} {{vm_name}} {{[-n|--name]}} {{new_vm_name}} {{[-f|--file]}} {{path/to/new_storage}} {{[-m|--mac]}} {{ff:ff:ff:ff:ff:ff|RANDOM}}`
