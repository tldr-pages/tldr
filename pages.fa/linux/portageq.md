# portageq

> پرس‌وجوی اطلاعات Portage، مدیر بستهٔ Gentoo Linux.
> متغیرهای محیطی مختص Portage که قابل پرس‌وجو هستند در `/var/db/repos/gentoo/profiles/info_vars` فهرست شده‌اند.
> اطلاعات بیشتر: <https://wiki.gentoo.org/wiki/Portageq>.

- نمایش مقدار متغیر محیطی مختص Portage:

`portageq envvar {{variable}}`

- نمایش فهرست مفصل مخازن پیکربندی‌شده با Portage:

`portageq repos_config /`

- نمایش فهرست مخازن مرتب‌شده بر اساس اولویت (بالاترین ابتدا):

`portageq get_repos /`

- نمایش فرادادهٔ مشخص یک atom (یعنی نام بسته همراه با نسخه):

`portageq metadata / {{ebuild|porttree|binary|...}} {{category}}/{{package}} {{BDEPEND|DEFINED_PHASES|DEPEND|...}}`
