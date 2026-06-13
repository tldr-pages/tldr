# am

> ஆண்ட்ராய்டு செயல்பாட்டு மேலாளர்.
> மேலும் விவரத்திற்கு: <https://developer.android.com/tools/adb#am>.

- ஒரு குறிப்பிட்ட செயல்பாட்டைத் தொடங்கவும்:

`am start -n {{com.android.settings/.Settings}}`

- ஒரு செயல்பாட்டைத் தொடங்கி, அதற்குத் தரவை அனுப்பவும்:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- குறிப்பிட்ட செயலுக்கும் வகைக்கும் பொருந்தும் செயல்பாட்டைத் தொடங்கவும்:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- ஒரு நோக்கத்தை URI ஆக மாற்றவும்:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
