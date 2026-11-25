# pacstall

> مدیر بستهٔ AUR برای Ubuntu.
> اطلاعات بیشتر: <https://github.com/pacstall/pacstall>.

- جست‌وجوی نام بسته در پایگاه دادهٔ بسته‌ها:

`pacstall {{[-S|--search]}} {{query}}`

- نصب بسته:

`pacstall {{[-I|--install]}} {{package}}`

- حذف بسته:

`pacstall {{[-R|--remove]}} {{package}}`

- افزودن مخزن به پایگاه داده (فقط GitHub و GitLab پشتیبانی می‌شوند):

`pacstall {{[-A|--add-repo]}} {{remote_repository_location}}`

- به‌روزرسانی اسکریپت‌های pacstall:

`pacstall {{[-U|--update]}}`

- به‌روزرسانی همهٔ بسته‌ها:

`pacstall {{[-Up|--upgrade]}}`

- نمایش اطلاعات بسته:

`pacstall {{[-Ci|--cache-info]}} {{package}}`

- فهرست کردن همهٔ بسته‌های نصب‌شده:

`pacstall {{[-L|--list]}}`
