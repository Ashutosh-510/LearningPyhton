# anime_menu = {"DBZ" : "Goku" , "One piece" : "Luffy"}

# try:

#     anime_menu["DBZ"]
#     print(anime_menu)
# except KeyError:
#     print("The key that you are trying to access does not exists")

# def anime(value):
#     try:
#         print("Selecting anime ")
#         if value == "unknown":
#             raise ValueError("We don't know that anime")
#     except ValueError as e:
#         print("Error: " ,e)
#     else:
#         print(f"{value} there is your anime")
#     # finally always works when function is called
#     finally:
#         print("Select another anime")


# anime("Naruto")
# anime("unknown")

'''File handling exceptions'''


try:
    with open("file.txt" , "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file you are trying to access does not exist")
    
