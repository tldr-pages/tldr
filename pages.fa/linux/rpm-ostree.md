# rpm-ostree

> سیستم ترکیبی تصویر و بسته.
> مدیریت استقرارهای ostree، لایه‌های بسته، overlayهای فایل‌سیستم و پیکربندی راه‌اندازی.
> اطلاعات بیشتر: <https://coreos.github.io/rpm-ostree/administrator-handbook/>.

- نمایش استقرارهای rpm-ostree به ترتیب نمایش در راه‌انداز:

`rpm-ostree status`

- نمایش بسته‌های قدیمی و قابل به‌روزرسانی:

`rpm-ostree upgrade --preview`

- آماده‌سازی استقرار جدید ostree با بسته‌های ارتقایافته و راه‌اندازی مجدد در آن:

`rpm-ostree upgrade {{[-r|--reboot]}}`

- راه‌اندازی مجدد در استقرار قبلی ostree:

`rpm-ostree rollback {{[-r|--reboot]}}`

- نصب بسته در استقرار جدید ostree و راه‌اندازی مجدد در آن:

`rpm-ostree install {{package}} {{[-r|--reboot]}}`
