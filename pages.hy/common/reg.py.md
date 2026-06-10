# reg.py

> Հարցրեք, ավելացրեք, ջնջեք, պահեք կամ պահուստավորեք ռեեստրի ստեղները/արժեքները հեռավոր Windows սարքի վրա SMB/RPC-ի միջոցով:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Հարցման ենթաբանալներ և արժեքներ ռեեստրի ուղու տակ.:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}'`

- Գրանցման ուղու տակ գտնվող բոլոր ենթաբանալների և արժեքների հարցում ռեկուրսիվ կերպով.:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} query -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -s`

- Ավելացնել նոր ռեեստրի բանալի կամ արժեք (նշանակված արժեքի տեսակն է `REG_SZ`):

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} add -keyName '{{HKLM\SOFTWARE\Microsoft\Windows}}' -v {{value_name}} -vt {{REG_SZ|REG_NONE|REG_EXPAND_SZ|REG_BINARY|REG_DWORD|REG_DWORD_BIG_ENDIAN|REG_LINK|REG_MULTI_SZ|REG_QWORD}} -vd {{value_data}}`

- Ջնջել ռեեստրի բանալի կամ արժեքը.:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} delete -keyName '{{HKLM\SOFTWARE\Example}}' -v {{value_name}}`

- Պահպանեք ռեեստրի բանալի (և ենթաստեղներ) թիրախի վրա գտնվող ֆայլում UNC ուղու միջոցով.:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} save -keyName '{{HKLM\SOFTWARE\Example}}' -o '\\{{target}}\{{share}}\{{output_file.reg}}'`

- Կրկնօրինակեք SAM-ը, SYSTEM-ը և SECURITY փեթակները թիրախի վրա գտնվող ֆայլում UNC ուղու միջոցով (պահանջում է SYSTEM-ի արտոնություններ).:

`reg.py {{domain}}/{{username}}:{{password}}@{{target}} backup -o '\\{{target}}\{{share}}'`
