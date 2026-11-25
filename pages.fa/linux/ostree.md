# ostree

> کنترل نسخهٔ فایل‌های دودویی مشابه `git`، اما بهینه‌شده برای فایل‌سیستم‌های ریشهٔ سیستم‌عامل.
> زیربنای سیستم‌عامل‌های تغییرناپذیر مبتنی بر تصویر مانند Fedora Silverblue، Fedora IoT یا Fedora CoreOS.
> اطلاعات بیشتر: <https://ostreedev.github.io/ostree/>.

- مقداردهی اولیهٔ مخزن فایل‌های موجود در `$PWD` با فراداده در `$PWD/path/to/repo`:

`ostree init --repo {{path/to/repo}}`

- ایجاد commit (snapshot) از فایل‌ها:

`ostree commit --repo {{path/to/repo}} --branch {{branch_name}}`

- نمایش فایل‌های commit:

`ostree ls --repo {{path/to/repo}} {{commit_id}}`

- نمایش فرادادهٔ commit:

`ostree show --repo {{path/to/repo}} {{commit_id}}`

- نمایش فهرست commitها:

`ostree log --repo {{path/to/repo}} {{branch_name}}`

- نمایش خلاصهٔ مخزن:

`ostree summary --repo {{path/to/repo}} --view`

- نمایش ارجاع‌های موجود (شاخه‌ها):

`ostree refs --repo {{path/to/repo}}`
