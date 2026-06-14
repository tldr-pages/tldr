# adb տեղադրում

> Փաթեթները միացված Android սարքին կամ էմուլյատորին մղեք:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/adb>:.

- Android հավելվածը մղեք էմուլյատորին/սարքին.:

`adb install {{path/to/file}}.apk`

- Անդրոիդ հավելվածը մղեք կոնկրետ էմուլյատորի/սարքի վրա (փոխանցում է `$ANDROID_SERIAL`):

`adb -s {{serial_number}} install {{path/to/file}}.apk`

- [r]տեղադրեք գոյություն ունեցող հավելված՝ պահպանելով դրա տվյալները.:

`adb install -r {{path/to/file}}.apk`

- Սեղմեք Android հավելվածը, որը թույլ է տալիս տարբերակի կոդը [d] downgrade (միայն վրիպազերծվող փաթեթները).:

`adb install -d {{path/to/file}}.apk`

- [g]տրամադրել հավելվածի մանիֆեստում թվարկված բոլոր թույլտվությունները.:

`adb install -g {{path/to/file}}.apk`

- Արագ թարմացրեք տեղադրված փաթեթը՝ թարմացնելով միայն APK-ի այն մասերը, որոնք փոխվել են.:

`adb install --fastdeploy {{path/to/file}}.apk`
