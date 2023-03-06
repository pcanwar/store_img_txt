
import requests
import os

filtered_listings = []
counter = 1
api_uri = 'https://www.example.com/listings/all?page'
while True:
    res = requests.get(f'{api_uri}={counter}')
    listings = res.json()
    if (len(listings) == 0) :
        break
    your_keys = ['title', 'images', 'data', 'description']
    for listing in listings:
        if(listing["owner"] == "615c5ec1a202c51a5b3340fe"):
            temp = {key: listing[key] for key in your_keys}
            filtered_listings.append(temp)
    counter+=1

# print(filtered_listings)
list_to_remove = [ 'Test', 'TEst', 'Test Upload','Test Rewards']

collection_listings = []
for filtered_listing in filtered_listings :
    if filtered_listing['title'] not in list_to_remove:
        collection_listings.append(filtered_listing)
        # print(filtered_listing['title'])

# print(collection_listings[0])

# here to create dirc with title name and save the images

for collection_listing in collection_listings:
    dir_name = collection_listing['title']
    image_link = collection_listing['images']
    data_info = collection_listing['data']
    description = collection_listing['description']

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        
    for i, download_image in enumerate(image_link):
        res = requests.get(download_image)
        with open(f'{dir_name}/image{i+1}.jpg', "wb") as f:
            f.write(res.content)

    with open(os.path.join(dir_name, 'data.txt'), 'w') as f:
        for k, j in data_info['extra'].items():
            # f.write(str(data_info))
            f.write(f"{k.capitalize()}: {j.lower()}\n")


    with open(os.path.join(dir_name, 'description.txt'), 'w') as f:
        f.write(str(description))
    