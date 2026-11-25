# lxc profile

> مدیریت پروفایل‌های کانتینرهای LXD.
> اطلاعات بیشتر: <https://canonical.com/lxd/docs/latest/reference/manpages/lxc/profile/>.

- فهرست کردن همهٔ پروفایل‌های موجود:

`lxc profile list`

- نمایش پیکربندی پروفایل مشخص:

`lxc profile show {{profile_name}}`

- ویرایش پروفایل مشخص در ویرایشگر پیش‌فرض:

`lxc profile edit {{profile_name}}`

- ویرایش پروفایل مشخص با وارد کردن مقادیر پیکربندی از فایل:

`lxc <{{config.yaml}} profile edit {{profile_name}}`

- راه‌اندازی کانتینر جدید با پروفایل‌های مشخص:

`lxc launch {{container_image}} {{container_name}} {{[-p|--profile]}} {{profile1}} {{[-p|--profile]}} {{profile2}}`

- تغییر پروفایل‌های کانتینر در حال اجرا:

`lxc profile assign {{container_name}} {{profile1,profile2}}`
