# toolbox rmi

> حذف تصاویر Toolbx.
> همچنین ببینید: `toolbox rm`.
> اطلاعات بیشتر: <https://manned.org/toolbox-rmi>.

- حذف یک یا چند تصویر Toolbx:

`toolbox rmi {{image_name1 image_name2 ...}}`

- حذف همهٔ تصاویر Toolbx:

`toolbox rmi {{[-a|--all]}}`

- حذف اجباری تصویر Toolbx که کانتینری اکنون از آن استفاده می‌کند (کانتینر نیز حذف می‌شود):

`toolbox rmi {{[-f|--force]}} {{image_name}}`
