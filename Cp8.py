#
# def displayMessage():
#     print('Hello World!')
# displayMessage()

def show_magicians(magicians):
    if magicians:
        for magician in magicians:
            print(magician)

def make_great(magicians):
    if magicians:
        for i in range(0, len(magicians)):
            magicians[i] = 'the Great ' + magicians[i]
        return magicians

magicians = ['Alpha', 'Beta', 'Theta']
show_magicians(magicians)
show_magicians(make_great(magicians[:]))
