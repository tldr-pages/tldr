# asciiart

> படங்களை ASCII ஆக மாற்றவும்.
> மேலும் விவரத்திற்கு: <https://github.com/nodanaonlyzuul/asciiart>.

- ஒரு கோப்பிலிருந்து ஒரு படத்தைப் படித்து ASCII இல் அச்சிடவும்:

`asciiart {{படம்.jpg/பாதை}}`

- URL இலிருந்து ஒரு படத்தைப் படித்து, ASCII இல் அச்சிடவும்:

`asciiart {{www.example.com/image.jpg}}`

- வெளியீட்டு அகலத்தைத் தேர்வு செய்யவும் (இயல்புநிலை 100):

`asciiart --width {{50}} {{படம்.jpg/பாதை}}`

- ASCII வெளியீட்டை வண்ணமயமாக்கவும்:

`asciiart --color {{படம்.jpg/பாதை}}`

- வெளியீட்டு வடிவமைப்பைத் தேர்வு செய்யவும் (இயல்புநிலை வடிவம் உரை):

`asciiart --format {{text|html}} {{படம்.jpg/பாதை}}`

- எழுத்து வரைபடத்தைத் தலைகீழாக மாற்றவும்:

`asciiart --invert-chars {{படம்.jpg/பாதை}}`
