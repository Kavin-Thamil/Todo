import webbrowser

user_input = input("Enter Google or Youtube: ")
user = user_input.capitalize()

if user == "Google":
    value = input("Enter you search: ")
    webbrowser.open(f"https://google.com/search?q={value}")
elif user == "Youtube":
    value = input("Enter you video: ")
    webbrowser.open(f"https://www.youtube.com/results?search_query={value}")
else:
    print("Invalid command")