import requests

def fetch_random_username():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data ["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"] ["username"]
        password = user_data["login"] ["password"]
        return username, password
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        username, password = fetch_random_username()
        print(f"Username: {username}\npassword : {password}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
