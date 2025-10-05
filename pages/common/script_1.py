
import os

# Create directory structure for the pages
os.makedirs("pages/common", exist_ok=True)

# Template for creating tldr pages
def create_tldr_page(command, description, examples):
    """Generate tldr page content"""
    content = f"""# {command}

> {description}
> More information: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli>.

"""
    for example_desc, example_cmd in examples:
        content += f"- {example_desc}:\n\n`{example_cmd}`\n\n"
    
    return content.strip() + "\n"

# Create all the command pages
pages_created = []

# 1. ibmcloud-api
content = create_tldr_page(
    "ibmcloud api",
    "Set or view the IBM Cloud API endpoint.",
    [
        ("View the current API endpoint", "ibmcloud api"),
        ("Set the API endpoint to cloud.ibm.com", "ibmcloud api cloud.ibm.com"),
        ("Set a private API endpoint", "ibmcloud api private.cloud.ibm.com"),
        ("Use a VPC connection for a private endpoint", "ibmcloud api private.cloud.ibm.com --vpc"),
        ("Bypass SSL validation of HTTP requests", "ibmcloud api https://cloud.ibm.com --skip-ssl-validation"),
        ("Remove the API endpoint setting", "ibmcloud api --unset")
    ]
)
with open("pages/common/ibmcloud-api.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-api.md")

# 2. ibmcloud-config
content = create_tldr_page(
    "ibmcloud config",
    "Modify or read out values in the IBM Cloud CLI configuration.",
    [
        ("Set HTTP request timeout to 30 seconds", "ibmcloud config --http-timeout 30"),
        ("Enable trace output for HTTP requests", "ibmcloud config --trace true"),
        ("Trace HTTP requests to a specific file", "ibmcloud config --trace {{path/to/trace_file}}"),
        ("Disable color output", "ibmcloud config --color false"),
        ("Set the locale to a specific language", "ibmcloud config --locale {{zh_Hans}}"),
        ("Enable automatic SSO one-time passcode acceptance", "ibmcloud config --sso-otp auto")
    ]
)
with open("pages/common/ibmcloud-config.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-config.md")

# 3. ibmcloud-logout
content = create_tldr_page(
    "ibmcloud logout",
    "Log out of the IBM Cloud CLI.",
    [
        ("Log out of the current session", "ibmcloud logout")
    ]
)
with open("pages/common/ibmcloud-logout.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-logout.md")

# 4. ibmcloud-plugin
content = create_tldr_page(
    "ibmcloud plugin",
    "Manage plugins and plugin repositories for the IBM Cloud CLI.",
    [
        ("List all installed plugins", "ibmcloud plugin list"),
        ("Install a plugin from a repository", "ibmcloud plugin install {{plugin_name}}"),
        ("Uninstall a plugin", "ibmcloud plugin uninstall {{plugin_name}}"),
        ("Update all plugins", "ibmcloud plugin update --all"),
        ("List available plugins in repositories", "ibmcloud plugin repo-plugins"),
        ("Add a plugin repository", "ibmcloud plugin repo-add {{repo_name}} {{repo_url}}")
    ]
)
with open("pages/common/ibmcloud-plugin.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-plugin.md")

print(f"Created {len(pages_created)} pages so far...")
print("Files created:", ", ".join(pages_created))
