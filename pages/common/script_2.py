
# Continue creating remaining Command Line pages

pages_created = []

# 5. ibmcloud-regions
content = create_tldr_page(
    "ibmcloud regions",
    "List all available regions on IBM Cloud.",
    [
        ("View information for all regions", "ibmcloud regions")
    ]
)
with open("pages/common/ibmcloud-regions.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-regions.md")

# 6. ibmcloud-target
content = create_tldr_page(
    "ibmcloud target",
    "Set or view the target account, region, or resource group.",
    [
        ("View the current target account and region", "ibmcloud target"),
        ("Set the target account", "ibmcloud target -c {{account_id}}"),
        ("Switch to a specific region", "ibmcloud target -r {{region_name}}"),
        ("Set the target resource group", "ibmcloud target -g {{resource_group_name}}"),
        ("Clear the targeted region", "ibmcloud target --unset-region"),
        ("Clear the targeted resource group", "ibmcloud target --unset-resource-group")
    ]
)
with open("pages/common/ibmcloud-target.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-target.md")

# 7. ibmcloud-update
content = create_tldr_page(
    "ibmcloud update",
    "Update the IBM Cloud CLI to the most recent version.",
    [
        ("Update the CLI", "ibmcloud update"),
        ("Force an update without confirmation", "ibmcloud update -f")
    ]
)
with open("pages/common/ibmcloud-update.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-update.md")

# 8. ibmcloud-version
content = create_tldr_page(
    "ibmcloud version",
    "Print the version of the IBM Cloud CLI.",
    [
        ("Display the CLI version", "ibmcloud version")
    ]
)
with open("pages/common/ibmcloud-version.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-version.md")

# 9. ibmcloud-help
content = create_tldr_page(
    "ibmcloud help",
    "Display help information for IBM Cloud CLI commands.",
    [
        ("Display general help for the IBM Cloud CLI", "ibmcloud help"),
        ("Display help for a specific command", "ibmcloud help {{command}}"),
        ("Display help for a specific namespace", "ibmcloud help {{namespace}}")
    ]
)
with open("pages/common/ibmcloud-help.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-help.md")

print(f"Command Line pages completed: {len(pages_created)} pages")
print("Files created:", ", ".join(pages_created))
