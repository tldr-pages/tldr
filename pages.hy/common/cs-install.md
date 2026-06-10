# cs տեղադրում

> Տեղադրեք հավելված տեղադրման գրացուցակում, որը կազմաձևված է `cs`-ը տեղադրելու ժամանակ (երկուականը բեռնելու հնարավորություն տալու համար ձեր `.bash_profile`-ին ավելացրեք `$ eval "$(cs install --env)"` հրամանը):.
> Լրացուցիչ տեղեկություններ. <https://get-coursier.io/docs/cli-install>:.

- Տեղադրեք հատուկ հավելված.:

`cs install {{application_name}}`

- Տեղադրեք հավելվածի որոշակի տարբերակ.:

`cs install {{application_name}}:{{application_version}}`

- Որոնեք հավելված հատուկ անունով.:

`cs search {{application_partial_name}}`

- Թարմացրեք հատուկ հավելված, եթե առկա է.:

`cs update {{application_name}}`

- Թարմացրեք բոլոր տեղադրված հավելվածները.:

`cs update`

- Տեղահանել հատուկ հավելված.:

`cs uninstall {{application_name}}`

- Նշեք բոլոր տեղադրված հավելվածները.:

`cs list`

- Տեղադրված հավելվածին փոխանցեք Java-ի հատուկ ընտրանքներ.:

`{{application_name}} {{-Jjava_option_name1=value1 -Jjava_option_name2=value2 ...}}`
