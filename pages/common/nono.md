# nono

> Secure, kernel-enforced sandbox CLI for AI agents and untrusted processes.
> Leverages Landlock (Linux) and Seatbelt (macOS) to restrict filesystem, network, and execution capabilities.
> More information: <https://nono.sh/docs>.

- Run a command using a configured profile with read and write access scoped to a specific path:
  `nono run --profile {{profile_name}} --allow {{path/to/input}} -- {{command}}`

- Run a command with granular split capabilities (separated read and write paths):
  `nono run --read {{path/to/input}} --write {{path/to/output}} -- {{command}}`

- Run a command with with read and write access for the current working directory with network egress completely blocked:
  `nono run --allow-cwd --block-net -- {{command}}`

- List all installed, built-in, and local security profiles:
  `nono profile list`

- Initialize and scaffold a custom security profile extending a base configuration:
  `nono profile init {{custom_name}} --extends {{base_profile}}`

- Start an interactive sandboxed shell scoped to a specific directory:
  `nono shell --allow {{path/to/directory}}`

- Explain why access to a path or operation is permitted or blocked:
  `nono why --path {{path/to/file}} --op {{read|write}}`
