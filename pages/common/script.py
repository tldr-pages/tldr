
# Create all IBM Cloud CLI tldr pages based on the command list

commands = {
    "Command Line": {
        "ibmcloud-api": "Set or view target API endpoint",
        "ibmcloud-config": "Modify or read out values in the config",
        "ibmcloud-logout": "Log user out",
        "ibmcloud-plugin": "Manage plug-ins and plug-in repositories",
        "ibmcloud-regions": "List all the regions",
        "ibmcloud-target": "Set or view the targeted region, account or resource group",
        "ibmcloud-update": "Update CLI to the latest version",
        "ibmcloud-version": "Print the version",
        "ibmcloud-help": "Show help"
    },
    "Platform": {
        "ibmcloud-account": "Manage accounts and users",
        "ibmcloud-assist": "Get answers to IBM Cloud questions by searching documentation, tutorials, and other IBM sources",
        "ibmcloud-billing": "Retrieve usage and billing information",
        "ibmcloud-catalog": "Manage catalog",
        "ibmcloud-cbr": "Manage Context Based Restrictions",
        "ibmcloud-enterprise": "Manage enterprise, account groups and accounts",
        "ibmcloud-iam": "Manage identities and access to resources",
        "ibmcloud-resource": "Manage resource groups and resources",
        "ibmcloud-resources": "List all resources",
        "ibmcloud-sat": "Manage IBM Cloud Satellite clusters"
    },
    "Containers": {
        "ibmcloud-cr": "Manage IBM Cloud Container Registry content and configuration",
        "ibmcloud-ks": "Manage Kubernetes and OpenShift clusters in IBM Cloud"
    },
    "Databases": {
        "ibmcloud-cloud-databases": "Manage IBM Cloud Databases"
    },
    "Infrastructure": {
        "ibmcloud-cos": "Interact with IBM Cloud Object Storage services",
        "ibmcloud-sl": "Manage Classic infrastructure services"
    },
    "Security": {
        "ibmcloud-key-protect": "Manage IBM Key Protect API",
        "ibmcloud-pag": "Manage Privileged Access Gateway",
        "ibmcloud-secrets-manager": "Manage IBM Cloud Secrets Manager API"
    },
    "Additional Services": {
        "ibmcloud-logging": "Manage IBM Cloud logging"
    }
}

# Display the commands to be created
print("IBM Cloud CLI tldr Pages to Create\n")
print("=" * 70)
for category, cmds in commands.items():
    print(f"\n{category}:")
    for cmd, desc in cmds.items():
        print(f"  - {cmd}.md")

print(f"\n\nTotal pages to create: {sum(len(cmds) for cmds in commands.values())}")
