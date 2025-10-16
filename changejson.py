import json

# Load existing dictionary
with open("sign_dict.json", "r") as f:
    data = json.load(f)

# Modify lowercase letter entries
for key in list(data.keys()):
    if len(key) == 1 and key.islower():  # lowercase letters like 'a', 'b', etc.
        upper_key = key.upper()
        data[key] = f"letters/LETTER-{upper_key}.mp4"

# Save back the modified JSON
with open("sign_dict.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ Lowercase letter paths updated to correct format.")
