# expiry

> Check and enforce the password expiration policy of the current user.
> See also: `chage`, `passwd`.
> More information: <https://manned.org/expiry>.

- Check whether the current user's password has expired:

`expiry {{[-c|--check]}}`

- Force a password change if the current user's password has expired:

`expiry {{[-f|--force]}}`
