# toolbox create

> புதிய `toolbox` கொள்கலனை உருவாக்கவும்.
> மேலும் விவரத்திற்கு: <https://manned.org/toolbox-create.1>.

- ஒரு குறிப்பிட்ட விநியோகத்திற்காக `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --distro {{விநியோகம்}}`

- தற்போதைய விநியோகத்தின் குறிப்பிட்ட வெளியீட்டிற்கு `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --release {{வெளியீடு}}`

- தனிப்பயன் படத்துடன் `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --image {{பெயர்}}`

- தனிப்பயன் ஃபெடோரா படத்திலிருந்து `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --image {{registry.fedoraproject.org/fedora-toolbox:38}}`

- ஃபெடோரா 36க்கான இயல்புநிலை படத்தைப் பயன்படுத்தி `toolbox` கொள்கலனை உருவாக்கவும்:

`toolbox create --distro {{fedora}} --release {{f38}}`
