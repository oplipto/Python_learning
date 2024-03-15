
import json

def load_data():
     try:
         with open("youtube.txt", "r") as file:
            test = json.load(file)
            # print(type(test))
            return test
     except FileNotFoundError:
            return []

def add_video(videos):
    name = input("Enter the name of the video: ")
    duration = input("Enter the duration of the video: ")
    videos.append({"name": name, "duration": duration})
    save_data_helper(videos)

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def remove_video(videos):
    show_all_video(videos)
    remove_video_number = int(input("Enter the video number of the video you want to remove: "))

    if 1 <= remove_video_number <= len(videos):
        del videos[remove_video_number - 1]
        save_data_helper(videos)
    else:
        print("Invalid video number selected")

def show_all_video(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos):
       print(f"{index + 1}. {video['name']}, duration: {video['duration']}")

    print("\n")
    print("*" * 70)
              

def update_video(videos):
    show_all_video(videos)
    index_number = int(input("Enter the video number of the video you want to update: "))
    if 1 <= index_number <= len(videos):
        name = input("Enter the new name of the video: ")
        duration = input("Enter the new duration of the video: ")
        videos[index_number - 1] = {"name": name, "duration": duration}
        save_data_helper(videos)
    else:
        print("Invalid video number selected")


def main():

    videos = load_data()

    while True:
        print("Welcome to the Youtube Manager App | Choose an option:")
        print("1. Add a video")
        print("2. Remove a video")
        print("3. Update a video")
        print("4. Show all videos")
        print("5. Exit")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case "1":
                add_video(videos)
            case "2":
                remove_video(videos)
            case "3":
                update_video(videos)
            case "4":
                show_all_video(videos)
            case "5":
                print("Exiting the app")
                break 
            case _:
                print("Invalid choice")
            
if __name__ == "__main__":

    main()