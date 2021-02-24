import os.path

filecount = 0

# while os.path.isfile(f"file{filecount}.txt") != True:
#     filecount += 1
#     print(filecount)
#     if os.path.isfile(f"file{filecount}.txt") != False:
#         print(f"create file file{filecount}.txt")
#         break


# while filecount != 10:
#     filecount += 1
#     print(filecount)

# print("finished!")

while os.path.isfile(f"file{filecount}.txt") == True:
    filecount +=1
    print(filecount)
f = open(f"file{filecount}.txt", "w")
f.write("FLAFLIP")
f.close()