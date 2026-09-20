# nono

> Secure, kernel-enforced sandbox CLI for AI agents and untrusted processes.
> Leverages Landlock (Linux) and Seatbelt (macOS) to restrict filesystem, network, and execution capabilities.
> More information: <https://nono.sh/docs>.

- Run a command with read and write access scoped automatically to the current working directory:
  nono run --allow-cwd -- {{command}}

- Run a command with granular split capabilities (separated read and write paths):
  nono run --read {{path/to/input}} --write {{path/to/output}} -- {{command}}

- Run a command with network egress completely blocked:
  nono run --allow-cwd --net-block -- {{command}}

- Run an agent or tool using a specific security profile:
  nono run --profile {{profile_name}} -- {{agent_command}}

- List all installed, built-in, and local security profiles:
  nono profile list

- Initialize and scaffold a custom security profile extending a base configuration:
  nono profile init {{custom_name}} --extends {{base_profile}}

- Start an interactive sandboxed shell scoped to a specific directory:
  nono shell --allow {{path/to/directory}}

- Explain why access to a path or operation is permitted or blocked:
  nono why --path {{path/to/file}} --op {{read|write}}
