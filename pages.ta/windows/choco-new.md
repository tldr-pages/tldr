# choco new

> சாக்லேட்டியுடன் புதிய தொகுப்பு விவரக்குறிப்பு கோப்புகளை உருவாக்கவும்.
> மேலும் தகவல்: <https://chocolatey.org/docs/commands-new>.

- ஒரு புதிய தொகுப்பு எலும்புக்கூட்டை உருவாக்கவும்:

`choco new {{package_name}}`

- ஒரு குறிப்பிட்ட பதிப்பில் புதிய தொகுப்பை உருவாக்கவும்:

`choco new {{package_name}} --version {{version}}`

- குறிப்பிட்ட பராமரிப்பாளர் பெயருடன் புதிய தொகுப்பை உருவாக்கவும்:

`choco new {{package_name}} --maintainer {{maintainer_name}}`

- தனிப்பயன் வெளியீட்டு கோப்பகத்தில் புதிய தொகுப்பை உருவாக்கவும்:

`choco new {{package_name}} --output-directory {{path/to/directory}}`

- குறிப்பிட்ட 32-பிட் மற்றும் 64-பிட் நிறுவி URLகளுடன் புதிய தொகுப்பை உருவாக்கவும்:

`choco புதிய {{package_name}} url="{{url}}" url64="{{url}}"`
