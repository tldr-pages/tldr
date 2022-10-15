# choco install

> சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை நிறுவவும்.
> மேலும் தகவல்: <https://chocolatey.org/docs/commands-install>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட இடம் பிரிக்கப்பட்ட தொகுப்புகளை நிறுவவும்:

`choco install {{package(s)}}`

- தனிப்பயன் உள்ளமைவு கோப்பிலிருந்து தொகுப்புகளை நிறுவவும்:

`choco install {{path/to/packages.config}}`

- ஒரு குறிப்பிட்ட nuspec அல்லது nupkg கோப்பை நிறுவவும்:

`choco install {{path/to/file}}`

- தொகுப்பின் குறிப்பிட்ட பதிப்பை நிறுவவும்:

`choco install {{package}} --version {{version}}`

- ஒரு தொகுப்பின் பல பதிப்புகளை நிறுவ அனுமதிக்கவும்:

`choco install {{package}} --allow-multiple`

- அனைத்து அறிவுறுத்தல்களையும் தானாக உறுதிப்படுத்தவும்:

`choco install {{package}} --yes`

- தொகுப்புகளைப் பெற தனிப்பயன் மூலத்தைக் குறிப்பிடவும்:

`choco install {{package}} --source {{source_url|alias}}`

- அங்கீகாரத்திற்கான பயனர்பெயர் மற்றும் கடவுச்சொல்லை வழங்கவும்:

`choco install {{package}} --user {{username}} --password {{password}}`
