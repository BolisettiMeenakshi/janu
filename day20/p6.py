posts = [
    {"user": "alice", "post" : "hi"},
    {"user": "bob", "post" : "hello"},
    {"user": "alice", "post" : "again"},
    {"user": "x", "post" : "xyz"},
    {"user": "bob", "post" : "again"},
]
posts_number = {}
for i in posts:
    user = i["user"]
    if user in posts_number:
        posts_number[user] += 1
    else:
        posts_number[user] = 1
#for i in posts:
    #if i["user"] in posts_number:
        #posts_number[i["user"]] = posts_number[i["user"]] + 1
    #else:
        #posts_number[i["user"]] = 1
print(posts_number)