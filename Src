import json

# Read asset data from JSON file
with open("asset.json", "r") as file:
    assets = json.load(file)

print("=========================================")
print("     CYBERSECURITY ASSET INVENTORY")
print("=========================================")

for asset in assets:
    print("Asset ID :", asset["Asset ID"])
    print("Asset Name :", asset["Asset Name"])
    print("Asset Type :", asset["Asset Type"])
    print("IP Address :", asset["IP Address"])
    print("OS :", asset["Operating System"])
    print("Department :", asset["Department"])
    print("Risk Level :", asset["Risk Level"])
    print("Status :", asset["Security Status"])
    print("-----------------------------------------")

# Count assets
total = len(assets)
critical = 0
high = 0
medium = 0
vulnerable = 0

for asset in assets:
    if asset["Risk Level"] == "Critical":
        critical += 1

    if asset["Risk Level"] == "High":
        high += 1

    if asset["Risk Level"] == "Medium":
        medium += 1

    if asset["Security Status"] == "Vulnerable":
        vulnerable += 1

print("Total Assets :", total)
print("Critical Assets :", critical)
print("High Risk Assets :", high)
print("Medium Risk Assets :", medium)
print("Vulnerable Assets :", vulnerable)
print("=========================================")
