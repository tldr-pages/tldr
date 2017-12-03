# chage

> Change user account and password expiry information.

- List password information for the user:

`chage -l {{user_name}}`

- Enable password expiration:

`sudo chage -M {{days_before_password_change}} {{user_name}}`

- Disable password expiration:

`sudo chage -M 99999 {{user_name}}`

- Set account expiration date:

`sudo chage -E {{YYYY-MM-DD}}`

- Force user to chage password on next log in:

`sudo chage -d 0`
 
