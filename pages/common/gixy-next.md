# gixy-next

> Analyze NGINX configuration files for security and performance misconfigurations.
> An actively maintained fork of `gixy`.
> More information: <https://gixy.io/usage/>.

- Analyze nginx configuration (default path: `/etc/nginx/nginx.conf`):

`gixy {{path/to/nginx.conf}}`

- Analyze a rendered configuration dump via `stdin` (`-`):

`cat {{path/to/nginx-dump.conf}} | gixy -`

- Run only specific checks (comma-separated):

`gixy --tests {{http_splitting,ssrf,version_disclosure}} {{path/to/nginx.conf}}`

- Skip specific checks (comma-separated):

`gixy --skips {{low_keepalive_requests,worker_rlimit_nofile_vs_connections}} {{path/to/nginx.conf}}`

- Only report issues at a given severity or higher:

`gixy {{-l|-ll|-lll}} {{path/to/nginx.conf}}`

- Output as uncolored text or machine-readable JSON:

`gixy {{[-f|--format]}} {{text|json}} {{path/to/nginx.conf}}`
