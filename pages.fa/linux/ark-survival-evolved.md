# ARK: Survival Evolved

> ایجاد و راه‌اندازی یک سرور بدون رابط گرافیکی برای ARK: Survival Evolved.
> اطلاعات بیشتر: <https://ark.wiki.gg/wiki/Server_configuration>.

- راه‌اندازی سرور با یک نقشهٔ مشخص:

`{{path/to}}/ShooterGameServer {{TheIsland}}`

- راه‌اندازی سرور با نام نشست، رمز عبور سرور و رمز عبور مدیر مشخص:

`{{path/to}}/ShooterGameServer {{TheIsland}}?SessionName={{session_name}}?ServerPassword={{server_password}}?ServerAdminPassword={{admin_password}}`

- راه‌اندازی سرور با یک درگاه مشخص و تنظیم حداکثر تعداد بازیکنان:

`{{path/to}}/ShooterGameServer {{TheIsland}}?Port={{7777}}?MaxPlayers={{1..70}}`

- فعال کردن حالت بازیکن در برابر محیط (PvE) و غیرفعال کردن حالت بازیکن در برابر بازیکن (PvP):

`{{path/to}}/ShooterGameServer {{TheIsland}}?ServerPVE=true`

- تنظیم یک ضریب برای مقیاس سختی سرور که بر حداکثر سطح موجودات وحشی تأثیر می‌گذارد:

`{{path/to}}/ShooterGameServer {{TheIsland}}?DifficultyOffset={{1.0}}`

- فعال کردن یک رویداد مشخص:

`{{path/to}}/ShooterGameServer {{TheIsland}} -ActiveEvent={{Summer}}`

- فعال کردن دانلود، نصب و به‌روزرسانی خودکار مودها (فقط Steam):

`{{path/to}}/ShooterGameServer {{TheIsland}} -automanagedmods`

- فعال کردن بازی مشترک بین Steam و Epic Games Store:

`{{path/to}}/ShooterGameServer {{TheIsland}} -crossplay -PublicIPForEpic={{ip_address}}`
