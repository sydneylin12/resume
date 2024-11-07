import requests
import json

# Usage
# python3 get-resume.py

# Define the API URL
url = "https://resumake.io/api/generate/resume"

# Load data from a local JSON file
with open("resume.json", "r") as file:
    data = json.load(file)

# Send POST request to the API
response = requests.post(url, json=data)

# Check if request was successful
if response.status_code == 200:
    # Save the PDF content to a file
    with open("Sydney Lin - Resume.pdf", "wb") as file:
        file.write(response.content)
    print("Resume downloaded successfully!")
else:
    print(f"Failed to generate resume. Status code: {response.status_code}")
