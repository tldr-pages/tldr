# spa-acp-tool

> اشکال‌زدایی شناسایی پروفایل کارت ALSA بدون اجرای PipeWire.
> اطلاعات بیشتر: <https://docs.pipewire.org/page_man_spa-acp-tool_1.html>.

- فهرست کردن همهٔ اشیای ALSA:

`spa-acp-tool {{[l|list]}}`

- بررسی کارت ALSA مشخص با شناسه:

`spa-acp-tool {{[c|card]}} {{card_id}}`

- فهرست کردن پروفایل‌های ALSA موجود برای کارت:

`spa-acp-tool {{[lpr|list-profiles]}} {{card_id}}`

- تنظیم پروفایل فعال ALSA با شناسه:

`spa-acp-tool {{[spr|set-profile]}} {{profile_id}}`

- فهرست کردن دستگاه‌های موجود برای کارت:

`spa-acp-tool {{[ld|list-devices]}} {{card_id}}`

- دریافت میزان صدای دستگاه:

`spa-acp-tool {{[gv|get-volume]}} {{device_id}}`

- تنظیم میزان صدای دستگاه:

`spa-acp-tool {{[v|set-volume]}} {{device_id}} {{volume_level}}`

- تغییر وضعیت بی‌صدایی دستگاه:

`spa-acp-tool {{[m|toggle-mute]}} {{device_id}}`
