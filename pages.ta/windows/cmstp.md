# cmstp

> இணைப்பு சேவை சுயவிவரங்களை நிர்வகிப்பதற்கான கட்டளை வரி கருவி.
> மேலும் தகவல்: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- ஒரு குறிப்பிட்ட சுயவிவரத்தை நிறுவவும்:

`cmstp "{{path/to/profile}}"`

- டெஸ்க்டாப் குறுக்குவழியை உருவாக்காமல் நிறுவவும்:

`cmstp /ns "{{path/to/profile}}"`

- சார்புகளை சரிபார்க்காமல் நிறுவவும்:

`cmstp /nf "{{path/to/profile}}"`

- தற்போதைய பயனருக்கு மட்டும் நிறுவவும்:

`cmstp /su "{{path/to/profile}}"`

- அனைத்து பயனர்களுக்கும் நிறுவவும் (நிர்வாக சலுகைகள் தேவை):

`cmstp /au "{{path/to/profile}}"`

- எந்த அறிவுறுத்தலும் இல்லாமல் அமைதியாக நிறுவவும்:

`cmstp /s "{{path/to/profile}}"`

- குறிப்பிட்ட சுயவிவரத்தை நிறுவல் நீக்கவும்:

`cmstp /u "{{path/to/profile}}"`

- உறுதிப்படுத்தல் அறிவுறுத்தல் இல்லாமல் அமைதியாக நிறுவல் நீக்கவும்:

`cmstp /u /s "{{path/to/profile}}"`