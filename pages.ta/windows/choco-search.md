# choco search

> சாக்லேட்டியுடன் உள்ளூர் அல்லது தொலைநிலைப் பொதியைத் தேடுங்கள்.
> மேலும் தகவல்: <https://chocolatey.org/docs/commands-search>.

- ஒரு தொகுப்பைத் தேடுங்கள்:

`choco search {{query}}`

- உள்நாட்டில் ஒரு தொகுப்பைத் தேடுங்கள்:

`choco search {{query}} --local-only`

- முடிவுகளில் சரியான பொருத்தங்களை மட்டும் சேர்க்கவும்:

`choco search {{query}} --exact`

- அனைத்து அறிவுறுத்தல்களையும் தானாக உறுதிப்படுத்தவும்:

`choco search {{query}} --yes`

- தொகுப்புகளைத் தேட தனிப்பயன் மூலத்தைக் குறிப்பிடவும்:

`choco search {{query}} --source {{source_url|alias}}`

- அங்கீகாரத்திற்கான பயனர்பெயர் மற்றும் கடவுச்சொல்லை வழங்கவும்:

`choco search {{query}} --user {{username}} --password {{password}}`
