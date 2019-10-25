# hydra

> Password brute forcing tool.
> More information: <https://github.com/vanhauser-thc/thc-hydra/>.

- Run hydra against an ftp server:

`hydra -l {{username}} -P {{password_list}} ftp://{{ip_address}}`

- Run hydra against an imap server with plain authentication:

`hydra -L {{username_list}} -p {{password}} imap://{{ip_address}}/PLAIN`

- Run hydra against a pop3s server. The credentials file should be a list in the form `user:password`:

`hydra -C {{credentials_file}} -6 pop3s://[{{ip_v6_address}}]:{{port}}/TLS:DIGEST-MD5`

- Run hydra against all ftp servers in an ip range, testing a specific username and password:

`hydra -l {{username}} -p {{password}} ftp://[{{ip_address}}/{{subnet}}]/`

- Run hydra against ssh on all a list of targets with every combination usernames and passwords:

`hydra -L {{username_list}} -P {{password_list}} -M {{target_list}} ssh`

- Run hydra against an online login post form:

`hydra -L {{username_list}} -P {{password_list}} {{ip_address}} http-post-form "/{{path_to_login_request}}:{{useaname_parameter}}=^USER^&{{password_parameter}}=^PASS^&{{other_parameters}}:{{string_in_failed_responce}}"`
