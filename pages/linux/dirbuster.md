# dirbuster

> Brute force directories and filenames on servers.
> More information: <https://www.kali.org/tools/dirbuster/>.

- Start in GUI mode:

`dirbuster -u {{http://example.com}}`

- Start in headless (no GUI) mode:

`dirbuster -H -u {{http://example.com}}`

- Set the file extension list:

`dirbuster -e {{txt,html}}`

- Enable verbose output:

`dirbuster -v`

- Set the report location:

`dirbuster -r {{path/to/report.txt}}`
