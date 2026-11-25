# renice

> تغییر اولویت زمان‌بندی یا niceness فرایندهای در حال اجرا.
> مقادیر niceness از ۲۰- (مطلوب‌ترین برای فرایند) تا ۱۹ (کم‌مطلوب‌ترین) هستند.
> همچنین : `nice`.
> اطلاعات بیشتر: <https://manned.org/renice>.

- تنظیم اولویت مطلق فرایند در حال اجرا:

`renice --priority {{3}} {{[-p|--pid]}} {{process_id}}`

- افزایش اولویت فرایند در حال اجرا:

`sudo renice --relative {{-4}} {{[-p|--pid]}} {{process_id}}`

- کاهش اولویت همهٔ فرایندهای متعلق به کاربر:

`renice --relative {{4}} {{[-u|--user]}} {{user_id|username}}`

- تنظیم اولویت همهٔ فرایندهای متعلق به گروه فرایند:

`sudo renice {{-5}} {{[-g|--pgrp]}} {{process_group}}`
