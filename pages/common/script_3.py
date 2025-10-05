
# Create Platform category pages

pages_created = []

# 10. ibmcloud-account
content = create_tldr_page(
    "ibmcloud account",
    "Manage IBM Cloud accounts and users.",
    [
        ("List all accounts", "ibmcloud account list"),
        ("Show details of the current account", "ibmcloud account show"),
        ("List users in the account", "ibmcloud account users"),
        ("Invite a user to the account", "ibmcloud account user-invite {{email}}"),
        ("List organizations in the account", "ibmcloud account orgs"),
        ("View documentation for account management subcommands", "tldr ibmcloud-account-{{subcommand}}")
    ]
)
with open("pages/common/ibmcloud-account.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-account.md")

# 11. ibmcloud-assist
content = create_tldr_page(
    "ibmcloud assist",
    "Get answers to IBM Cloud questions using AI assistant powered by watsonx.",
    [
        ("Ask a question to the AI assistant", 'ibmcloud assist "{{How do I create a Kubernetes cluster?}}"'),
        ("Get help about updating the CLI", 'ibmcloud assist "How do I update the CLI?"'),
        ("Ask about resource management", 'ibmcloud assist "How do I list my resources?"')
    ]
)
with open("pages/common/ibmcloud-assist.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-assist.md")

# 12. ibmcloud-billing
content = create_tldr_page(
    "ibmcloud billing",
    "Retrieve usage and billing information for IBM Cloud.",
    [
        ("View account usage", "ibmcloud billing account-usage"),
        ("View resource group usage", "ibmcloud billing resource-group-usage {{resource_group_name}}"),
        ("View organization usage", "ibmcloud billing org-usage {{org_name}}"),
        ("View resource instances usage", "ibmcloud billing resource-instances-usage"),
        ("View billing information for a specific month", "ibmcloud billing account-usage -d {{YYYY-MM}}")
    ]
)
with open("pages/common/ibmcloud-billing.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-billing.md")

# 13. ibmcloud-catalog
content = create_tldr_page(
    "ibmcloud catalog",
    "Manage the IBM Cloud catalog.",
    [
        ("List all catalog entries", "ibmcloud catalog search"),
        ("Search for a specific service", "ibmcloud catalog search {{service_name}}"),
        ("Get details of a catalog entry", "ibmcloud catalog entry {{entry_id}}"),
        ("List all templates", "ibmcloud catalog templates"),
        ("Filter catalog by category", "ibmcloud catalog search --category {{compute}}")
    ]
)
with open("pages/common/ibmcloud-catalog.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-catalog.md")

# 14. ibmcloud-cbr
content = create_tldr_page(
    "ibmcloud cbr",
    "Manage Context Based Restrictions in IBM Cloud.",
    [
        ("List all network zones", "ibmcloud cbr zones"),
        ("Create a network zone", "ibmcloud cbr zone-create --name {{zone_name}}"),
        ("List all context-based restriction rules", "ibmcloud cbr rules"),
        ("Create a context-based restriction rule", "ibmcloud cbr rule-create"),
        ("Delete a network zone", "ibmcloud cbr zone-delete {{zone_id}}")
    ]
)
with open("pages/common/ibmcloud-cbr.md", "w") as f:
    f.write(content)
pages_created.append("ibmcloud-cbr.md")

print(f"Platform pages (1-5): {len(pages_created)} pages")
print("Files created:", ", ".join(pages_created))
