# azcopy

> அஸூர் கிளவுட் ஸ்டோரேஜ் கணக்குகளில் பதிவேற்றுவதற்கான கோப்பு பரிமாற்றக் கருவி.
> மேலும் தகவல்: <https://learn.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- அசூர் குத்தகைதாரரிடம் உள்நுழையவும்:

`azopy login`

- உள்ளூர் கோப்பைப் பதிவேற்றவும்:

`azcopy copy '{{path/to/source/file}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}/{{blob_name}}'`

- `.txt` மற்றும் `.jpg` நீட்டிப்புகளுடன் கோப்புகளைப் பதிவேற்றவும்:

`azcopy copy '{{path/to/source}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --include-pattern '{{*.txt;*.jpg}}'`

- இரண்டு அசூர் சேமிப்பு கணக்குகளுக்கு இடையே நேரடியாக ஒரு கொள்கலனை நகலெடுக்கவும்:

`azcopy copy 'https://{{source_storage_account_name}}.blob.core.windows.net/{{container_name}}' 'https://{{destination_storage_account_name}}.blob.core.windows.net/{{container_name}}'`

- ஒரு உள்ளூர் கோப்பகத்தை ஒத்திசைக்கவும், மேலும் மூலத்தில் கோப்புகள் இல்லை என்றால் இலக்கில் உள்ள கோப்புகளை நீக்கவும்:

`azcopy sync '{{path/to/source}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --recursive --delete-destination=true`

- விரிவான பயன்பாட்டுத் தகவலைக் காண்பி:

`azcopy --help`
