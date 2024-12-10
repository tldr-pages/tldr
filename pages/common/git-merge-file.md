
# git-merge-file

```bash
git merge-file [-L <current-name> [-L <base-name> [-L <other-name>]]]
	[--ours|--theirs|--union] [-p|--stdout] [-q|--quiet] [--marker-size=<n>]
	[--[no-]diff3] [--object-id] <current> <base> <other>
```

### DESCRIPTION

- **merge changes of three files (current, base, other)**
  ```bash
  git merge-file <current> <base> <other>
  ```

- **resolve conflicts by keeping 'ours' (current file's changes)**
  ```bash
  git merge-file --ours <current> <base> <other>
  ```

- **resolve conflicts by keeping 'theirs' (other file's changes)**
  ```bash
  git merge-file --theirs <current> <base> <other>
  ```

- **resolve conflicts by combining both changes ('union')**
  ```bash
  git merge-file --union <current> <base> <other>
  ```

- **show conflicts in diff3 style (default is normal)**
  ```bash
  git merge-file --diff3 <current> <base> <other>
  ```

- **output merged result to stdout instead of updating current file**
  ```bash
  git merge-file -p <current> <base> <other>
  ```

- **list conflicts quietly without warnings**
  ```bash
  git merge-file -q <current> <base> <other>
  ```

- **specify custom labels for each file**
  ```bash
  git merge-file -L <current-label> -L <base-label> -L <other-label> <current> <base> <other>
  ```

### EXAMPLES

- **Basic Merge Example**
  ```bash
  git merge-file README.my README README.upstream
  ```

- **Merge with custom labels**
  ```bash
  git merge-file -L a -L b -L c tmp/a123 tmp/b234 tmp/c345
  ```

- **Merge using object IDs and output to stdout**
  ```bash
  git merge-file -p --object-id abc1234 def567 890abcd
  ```
