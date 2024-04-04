
class Post :
    def __init__(self, text, poster):
        self.text = text
        self.poster = poster

    def __repr__(self):
        return "["+self.poster.name+"]:" + self.text

class User:
    def __init__(self, name):
        self.name = name
        self.friends = [] # store objects of type user who are my friends
        self.requests = []
        self.wall = Wall (self)

    def addFriend (self, user):
        #self.friends.append(user)
        friendrequest = Request(self, user)
        #user.addFriendRequest(friendrequest)
        user.requests.append (friendrequest)

    def approve (self, request):
        request.from_.friends.append (request.to_)
        request.to_.friends.append (request.from_)
    def __repr__(self):
        return self.name

    def post (self, text):
        p  = Post (text, self)
        print (str (self)+ " just posted " + text )
        self.wall.posts.append(p)
        for f in self.friends:
            f.wall.posts.append (p)


class Wall :
    def __init__(self, owner):
        self.posts = []
        self.owner = owner
    def __repr__(self):
        print ("Wall "+ self.owner.name )
        print ("=============")
        for p in self.posts:
            print (p)


class Request :
    def __init__(self, from_, to_):
        self.from_ = from_
        self.to_ = to_
    def __repr__(self):
        return "Add friend request from " + str (self.from_)

u1 = User ("Joe")
u2 = User ("Jill")
print (u1.name + " Friend List = " + str(u1.friends))
u1.addFriend(u2)
print (u2.name + " Friend Requests = " + str(u2.requests))
u2.approve (u2.requests[0])
print (u1.name + " Friend List = " + str(u1.friends))
#Joe Friend List = []
#Jill Friend Requests = [Add friend request from Joe]
#Approving

p1 = u1.post("What a lovely weekend")
print (u2.wall)
p2 = u2.post("Sunny and warm!")