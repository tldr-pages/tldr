# dnf install

> نصب بسته‌ها در توزیع‌های مبتنی بر رد هت.
> اطلاعات بیشتر: <https://dnf.readthedocs.io/en/latest/command_ref.html#install-examples>.

- نصب بسته‌ها بر اساس نام:

`sudo dnf {{[in|install]}} {{package1 package2 ...}}`

- نصب یک بسته از فایل محلی:

`sudo dnf {{[in|install]}} {{path/to/file}}`

- نصب یک بسته از اینترنت:

`sudo dnf {{[in|install]}} {{https://example.com/package.rpm}}`

- افزودن مخزن بسته‌های غیرآزاد فدورا:

`sudo dnf {{[in|install]}} https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm`

- افزودن مخازن بسته‌های اضافی برای لینوکس سازمانی (EPEL):

`sudo dnf {{[in|install]}} epel-release`

- افزودن مخزن RPM متعلق به Remi:

`sudo dnf {{[in|install]}} https://rpms.remirepo.net/enterprise/remi-release-{{8}}.rpm`
