# bluetoothctl

> കമാൻഡ് ലൈനിൽ നിന്ന് ബ്ലൂടൂത്ത് ഉപകരണങ്ങൾ മാനേജുചെയ്യുക.
> കൂടുതൽ വിവരങ്ങൾ: <https://bitbucket.org/serkanp/bluetoothctl>.

- ബ്ലൂടൂത്ത്സിറ്റിഎൽ ഷെല്ലിൽ കേറാൻ:

`bluetoothctl`

- ഉപകരണങ്ങളുടെ പട്ടിക കാണാൻ:

`bluetoothctl --devices`

- ഒരു ഉപകരണം ജോടിയാക്കുക:

`bluetoothctl --pair {{മാക്_വിലാസം}}`

- ഒരു ഉപകരണം നീക്കംചെയ്യുക:

`bluetoothctl --remove {{മാക്_വിലാസം}}`

- ജോഡിയായ ഉപകരണവുമായി ബന്ധിപ്പിക്കുക:

`bluetoothctl --connect {{മാക്_വിലാസം}}`

- ഒരു ജോഡിയായ ഉപകരണവുമായുള്ള ബന്ധം വിച്ഛേദിക്കുക:

`bluetoothctl --disconnect {{മാക്_വിലാസം}}`
