
# First-Class Example

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]) # list of strings as the lyrics

happy_bday.sing_me_a_song()

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

bulls_on_parade.sing_me_a_song()

# put the lyrics in a separate variable
bday_lyric = ["Happy birthday to you",
              "I don't want to get sued",
              "So I'll stop right there"]

happy_bday = Song(bday_lyric)
happy_bday.sing_me_a_song()

# SELF make clear that you mean the instance attribute and not local variable.