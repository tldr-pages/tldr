# wget

> PowerShell இல், அசல் `wget` நிரல் (<https://www.gnu.org/software/wget>) சரியாக நிறுவப்படாதபோது இந்தக் கட்டளை `Invoke-WebRequest` என்பதன் மாற்றுப் பெயராக இருக்கலாம்.
> மேலும் விவரத்திற்கு: <https://learn.microsoft.com/powershell/module/microsoft.powershell.utility/invoke-webrequest>.

- அதன் பதிப்பு எண்ணை அச்சிட்டு `wget` சரியாக நிறுவப்பட்டுள்ளதா என்பதைச் சரிபார்க்கவும். இந்த கட்டளை பிழையாக மதிப்பிடப்பட்டால், PowerShell இந்த கட்டளையை `Invoke-WebRequest` உடன் மாற்றியிருக்கலாம்:

`curl --version`

- அசல் `wget` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr wget -p common`

- `tldr` கட்டளை வரி கிளையண்டின் பழைய பதிப்புகளில் அசல் `wget` கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr wget -o common`

- PowerShell இன் 'Invoke-WebRequest' கட்டளைக்கான ஆவணங்களைக் காண்க:

`tldr invoke-webrequest`
