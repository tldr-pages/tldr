# ARK: Survival Ascended

> ایجاد و راه‌اندازی یک سرور بدون رابط گرافیکی برای ARK: Survival Ascended.
> اطلاعات بیشتر: <https://ark.wiki.gg/wiki/Server_configuration>.

- راه‌اندازی سرور با یک نقشهٔ مشخص:

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}}`

- راه‌اندازی سرور با نام نشست، رمز عبور سرور و رمز عبور مدیر مشخص:

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}}?SessionName={{session_name}}?ServerPassword={{server_password}}?ServerAdminPassword={{admin_password}}`

- راه‌اندازی سرور با یک درگاه مشخص و تنظیم حداکثر تعداد بازیکنان:

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}} -port={{7777}} -WinLiveMaxPlayers={{1..70}}`

- فعال کردن حالت بازیکن در برابر محیط (PvE) و غیرفعال کردن حالت بازیکن در برابر بازیکن (PvP):

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}}?ServerPVE=true`

- تنظیم یک ضریب برای مقیاس سختی سرور که بر حداکثر سطح موجودات وحشی تأثیر می‌گذارد:

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}}?DifficultyOffset={{1.0}}`

- غیرفعال کردن بهینه‌سازی پویانمایی موجودات برای جلوگیری از مشکلات برخورد:

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}} -AlwaysTickDedicatedSkeletalMeshes`

- فعال کردن مودهای مشخص با شناسهٔ آن‌ها (جداشده با ویرگول):

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}} -mods={{mod_id1,mod_id2,...}}`

- اجازه دادن به اتصال از پلتفرم‌های مشخص:

`{{path/to}}/ArkAscendedServer {{TheIsland_WP}} -ServerPlatform={{PC+XSX+PS5}}`
