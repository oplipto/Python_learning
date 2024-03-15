import requests

def channel_info():
    url = "https://api.freeapi.app/api/v1/public/youtube/channel"
    response = requests.get(url)
    data = response.json()

    if data ["success"] and "data" in data:
        channel_data = data["data"]
        channel = channel_data["info"]["snippet"]
        channel_title = channel_data["info"]["snippet"]["title"]
        channel_description = channel_data["info"]["snippet"]["description"]
        return channel_title, channel_description
    
def main():
    try:
        channel = channel_info()
        print(f"Channel: {channel[0]}\nDescription: {channel[1]}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()