import requests
import logging
url = "https://background-removal.p.rapidapi.com/remove"

headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "c18f5c5bf6msh22a3c0a6d090a9ap16cf04jsna442316f8c7e",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

# test payload
# payload = "image_url=http://telegra.ph//file/20a29be00da8f854a12d9.jpg"



def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    # logging.info(json()['response']['image_url'])
    return response.json()['response']['image_url']

#print(remove_background('http://telegra.ph//file/20a29be00da8f854a12d9.jpg'))