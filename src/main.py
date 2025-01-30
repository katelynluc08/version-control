from datetime import datetime

# Get current date and time
now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

# Write to version.md in the root directory

with open('src/version.md', 'w') as f:
    f.write(f"Last updated: {current_time}")


print(f"Current time written to version.md")

# Used AI to help with code
