# choco upgrade

> சாக்லேட்டியுடன் ஒன்று அல்லது அதற்கு மேற்பட்ட தொகுப்புகளை மேம்படுத்தவும்.
> மேலும் தகவல்: <https://chocolatey.org/docs/commands-upgrade>.

- ஒன்று அல்லது அதற்கு மேற்பட்ட இடம் பிரிக்கப்பட்ட தொகுப்புகளை மேம்படுத்தவும்:

`choco upgrade {{package(s)}}` 

- தொகுப்பின் குறிப்பிட்ட பதிப்பிற்கு மேம்படுத்தவும்:

`choco upgrade {{package}} --version {{version}}`

- அனைத்து தொகுப்புகளையும் மேம்படுத்தவும்:

`choco upgrade all`

- குறிப்பிட்ட காற்புள்ளியால் பிரிக்கப்பட்ட தொகுப்புகளைத் தவிர அனைத்தையும் மேம்படுத்தவும்:

`choco upgrade all --except "{{package(s)}}"` 

- அனைத்து அறிவுறுத்தல்களையும் தானாக உறுதிப்படுத்தவும்:

`choco upgrade {{package}} --yes`

- தொகுப்புகளைப் பெற தனிப்பயன் மூலத்தைக் குறிப்பிடவும்:

`choco upgrade {{package}} --source {{source_url|alias}}`

- அங்கீகாரத்திற்கான பயனர்பெயர் மற்றும் கடவுச்சொல்லை வழங்கவும்:

`choco upgrade {{package}} --user {{username}} --password {{password}}`