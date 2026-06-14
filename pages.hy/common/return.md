#վերադարձ

> Դուրս գալ գործառույթից:.
> Կարող է դուրս գալ սկրիպտից, եթե գործարկվի `source`-ով:.
> Տես նաև՝ `exit`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/bash/manual/bash.html#index-return>:.

- Վաղաժամկետ դուրս գալ գործառույթից.:

`{{func_name}}() { {{echo "This is reached"}}; return; {{echo "This is not"}}; }`

- Նշեք ֆունկցիայի վերադարձի արժեքը.:

`{{func_name}}() { return {{exit_code}}; }`
