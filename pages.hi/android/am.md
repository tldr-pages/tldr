# am

> एंड्रॉइड गतिविधि प्रबंधक।
> अधिक जानकारी: <https://developer.android.com/studio/command-line/adb#am>।

- एक विशिष्ट गतिविधि प्रारंभ करें:

`am start -n {{com.android.settings/.Settings}}`

- एक गतिविधि शुरू करें और उसमें डेटा[d] पास करें:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- किसी विशिष्ट क्रिया और श्रेणी[c] से मेल खाती गतिविधि प्रारंभ करें:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- एक उद्देश्य को यूआरआई में बदलें:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
