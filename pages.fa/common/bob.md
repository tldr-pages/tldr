# bob

> مدیریت و جابجایی بین نسخه های مختلف Neovim.
> اطلاعات بیشتر: <https://github.com/MordechaiHadad/bob>.

- نصب و جابجایی به نسخه خاصی از Neovim:

`bob use {{nightly|stable|latest|version_string|commit_hash}}`

- فهرست نسخه های نصب شده و نسخه ای که اکنون استفاده می شود:

`bob list`

- حذف یک نسخه خاص از Neovim:

`bob uninstall {{nightly|stable|latest|version_string|commit_hash}}`

- حذف Neovim و پاک کردن هر تغییری که `bob` اعمال کرده است:

`bob erase`

- بازگشت به نسخه شبانه قبلی:

`bob rollback`
