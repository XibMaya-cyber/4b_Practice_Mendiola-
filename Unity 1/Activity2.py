class User:
    def __init__(self, name, gmail, password):
        self.name = name
        self.gmail = gmail
        self.__password = password

    def create_post(self, post_type, title, content, likes=0):
        return Post(post_type, title, content, likes)

    def show_post(self, post):
        print(f"{self.name} publicó: {post.title}")

    def greet(self):
        print(f"Welcome {self.name}")


class Post:
    def __init__(self, post_type, title, content, likes=0):
        self.post_types = post_type
        self.title = title
        self.content = content
        self.likes = likes
        self.comments = []        

    def add_comment(self, comment_obj):
        self.comments.append(comment_obj)

    def show_comments(self):
        if not self.comments:
            print("This post has no comments yet.")
        for c in self.comments:
            print(f"{c.user.name}: {c.comment}")

    def show_type(self):
        if self.post_types == 'POST':
            print("This is a post")
        elif self.post_types == 'REELS':
            print("This is a reel")

    def add_likes(self):
        self.likes += 1
        print(f"This post has {self.likes} likes")

    def set_title(self):
        self.title = input("Title of the post: ")
        print(self.title)


class Comments:
    def __init__(self, comment, user, post, receiver=None):
        self.comment = comment
        self.user = user
        self.post = post
        self.receiver = receiver

    def add_comments(self):
        add_comment = input("Add a comment: ")
        self.comment = add_comment
        self.post.add_comment(self)
        print(f"{self.user.name} comment: {self.comment}")


user1 = User("vegetta", "123@gmail.com", "123")
user2 = User("willy", "456@gmail.com", "456")

post1 = user1.create_post("REEL", "planeta veggeta", "contenido del reel...", 19)
user1.show_post(post1)

# user2 comenta en el post de user1
comment1 = Comments("", user2, post1)
comment1.add_comments()

# user1 también comenta en su propio post
comment2 = Comments("", user1, post1)
comment2.add_comments()

# mostrar todos los comentarios del post
post1.show_comments()