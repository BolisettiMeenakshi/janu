id = int(input())
posts = [
  {"id": 1, "content": "Hello", "timestamp": "2024-05-01 10:00"},
  {"id": 2, "content": "World", "timestamp": "2024-06-01 09:00"}
]
time_stamp = {}
class time_stamp:
    def __init__(self,id,content,timestamp):
        self.id = id
        self.content = content
        self.timestamp = timestamp
    def __str__(self):
        return f"id = {self.id}, content = {self.content}, timestamp = {self.timestamp}"
for post in posts[:id]:
    print(time_stamp(post["id"],post["content"],post["timestamp"]))