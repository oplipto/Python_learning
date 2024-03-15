import requests

def random_jokes():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    data = response.json()

    if data ["success"] and "data" in data:
        jokes_data = data["data"]
        joke = jokes_data["content"]
        return joke
    else:
        raise Exception("Failed to fetch jokes")
    

def main():
    try:
        joke = random_jokes()
        print(f"LOL: {joke}")

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()