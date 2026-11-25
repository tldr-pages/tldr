# nsenter

> اجرای دستور جدید در فضای نام فرایند در حال اجرا.
> به‌ویژه برای تصاویر Docker یا محیط‌های محصور chroot مفید است.
> اطلاعات بیشتر: <https://manned.org/nsenter>.

- اجرای دستور مشخص با همان فضاهای نام فرایند موجود:

`nsenter {{[-t|--target]}} {{process_id}} {{[-a|--all]}} {{command}} {{command_arguments}}`

- اجرای دستور مشخص در فضای نام mount، UTS، IPC، شبکه، PID، کاربر، cgroup یا زمان فرایند موجود:

`nsenter {{[-t|--target]}} {{process_id}} --{{mount|uts|ipc|net|pid|user|cgroup}} {{command}} {{command_arguments}}`

- اجرای دستور مشخص در فضاهای نام UTS، زمان و IPC فرایند موجود:

`nsenter {{[-t|--target]}} {{process_id}} {{[-u|--uts]}} {{[-T|--time]}} {{[-i|--ipc]}} -- {{command}} {{command_arguments}}`

- اجرای دستور مشخص در فضای نام فرایند موجود با ارجاع به procfs:

`nsenter {{[-n|--net=]}}/proc/{{process_id}}/ns/net -- {{command}} {{command_arguments}}`
