import requests

# Send a GET request to the API
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)  # Print the data
else:
    print(f"Error: {response.status_code}")  # Print the error code if something went wrong