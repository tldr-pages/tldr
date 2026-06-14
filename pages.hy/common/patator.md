#պատատոր

> Բազմաֆունկցիոնալ բիրտ ուժային միջոց, մոդուլային դիզայնով և ճկուն կիրառմամբ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/lanjelot/patator/wiki/Usage>:.

- Brute force ssh login տոկոսադրույքի սահմանաչափով և ժամանակի դադարի ընտրանքներով (հաջող մուտքը ցույց կտա մուտքի դրոշակ կամ նման բան).:

`patator ssh_login host={{ip_or_host}} user=FILE0 password=FILE1 0={{path/to/users.txt}} 1={{path/to/passwords.txt}} --rate_limit={{seconds}} --timeout={{seconds}} -x ignore:mesg='Authentication failed.'`

- Կոպիտ ուժի կոդավորված ZIP ֆայլ.:

`patator unzip_pass zipfile={{path/to/file.zip}} password=FILE0 0={{path/to/passwords.txt}} -x ignore:code!=0`

- Կոպիտ ուժ http հիմնական վավերացում (վճարման ֆայլը `userpass.txt` պետք է լինի `username:password` ձևաչափով):

`patator http_fuzz url={{http://host:port}} auth_type=basic user_pass=COMBO00:COMBO01 0={{path/to/userpass.txt}} -x ignore:code=401`

- Կոպիտ ուժ FTP/FTPS մուտք.:

`patator ftp_login host={{ip_or_host}} user=FILE0 password=FILE1 0={{path/to/users.txt}} 1={{path/to/passwords.txt}} tls={{0|1}} -x ignore:mesg='Login incorrect.' -x ignore,reset,retry:code=500`

- Թվարկեք բոլոր հասանելի մոդուլները.:

`patator --help`

- Ցուցադրել օգնությունը որոշակի մոդուլի համար.:

`patator {{module_name}} --help`
