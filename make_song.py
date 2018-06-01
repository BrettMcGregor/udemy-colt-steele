'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''


def make_song(count=99, beverage="soda"):
    for i in range(count+1, 0, -1):
        if i == 1:
            yield "No more {}!".format(beverage)
        elif i == 2:
            yield "Only {} bottle of {} left!".format(i - 1, beverage)
        else:
            yield "{} bottles of {} on the wall.".format(i - 1, beverage)
        i -= 1

soda = make_song(5, "beer")
print(next(soda))
print(next(soda))
print(next(soda))
print(next(soda))
print(next(soda))
print(next(soda))
