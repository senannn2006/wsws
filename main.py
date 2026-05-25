# import requests
# url="https://jsonplaceholder.typicode.com/posts/1"
# cavab=requests.get(url)
# print(cavab.status_code)
# data=cavab.json()
# print(data["title"])
#       2 ci sual    
# import requests
# url="https://jsonplaceholder.typicode.com/posts"
# cavab=requests.get(url)
# data=cavab.json()
# for i in range(1,11):
#     print(data[i]["id"])
#     print(data[i]["title"])
# #                       3 cu sual
# import requests
# url="https://jsonplaceholder.typicode.com/comments"
# salam={"postId": 1}

# cavab=requests.get(url,params=salam)
# sagol=cavab.json()
# say=len(sagol)
# print(say)
#                  4 cu sual
# import requests
# url="https://jsonplaceholder.typicode.com/users"
# ad=input("istifadeci adi daxil edin")
# cavab=requests.get(url)
# data=cavab.json()

# for user in data:
#     d= user["name"]
#     if ad==d:
#          print(user["email"])
#          print(user["address"]["city"])

   
#                       5 ci suall
# import requests
# username=input("ad daxil edin... ")
# url=f"https://api.github.com/users/{username}"
# cavab=requests.get(url)
# data=cavab.json()
# if cavab.status_code==200:
#  print(data["name"])
#  print(data["public_repos"])
#  print(data["followers"])
#  print(data["following"])
# else:
#  print("user not found")