# wpctl settings

> مدیریت تنظیمات زمان اجرای WirePlumber.
> اطلاعات بیشتر: <https://pipewire.pages.freedesktop.org/wireplumber/daemon/configuration/configuration_option_types.html>.

- فهرست کردن همهٔ تنظیمات:

`wpctl settings`

- مشاهدهٔ مقدار تنظیم مشخص:

`wpctl settings {{setting_id}}`

- تنظیم صدای کل سیستم به حالت مونو:

`wpctl settings node.features.audio.mono true`

- تنظیم توقف پخش هنگام قطع بلندگوها:

`wpctl settings linking.pause-playback {{true|false}}`
