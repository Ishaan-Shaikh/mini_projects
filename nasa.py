import requests
import os
from PIL import Image
from io import BytesIO

# Load API key from environment or config file
NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")  # Use DEMO_KEY for testing

# NASA APOD API endpoint
url = "https://api.nasa.gov/planetary/apod" 

# Parameters
params = {
    'api_key': NASA_API_KEY,
    'count': 1  # Get one APOD
}

# Make the request
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()[0]  # Get the first result

    if data['media_type'] == 'image':
        image_url = data['url']
        print("Title:", data['title'])
        print("Explanation:", data['explanation'][:300] + "...")

        # Download image
        image_response = requests.get(image_url)
        image_data = BytesIO(image_response.content)

        # Open and show image
        img = Image.open(image_data)
        img.show()  # This will open the default image viewer

        # Optional: Save image
        img.save("nasa_apod.jpg")
        print("Image saved as 'nasa_apod.jpg'")
    else:
        print("Today's APOD is not an image.")
else:
    print("Error fetching APOD:", response.status_code)
    print(response.text)