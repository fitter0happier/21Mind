def card2string(cardList):
        str = ''
        str = ','.join(cardList)
        str = str.replace('C', 'Club ')
        str = str.replace('S', 'Spade ')
        str = str.replace('H', 'Heart ')
        str = str.replace('D', 'Diamond ')
        str = str.replace('T', '10')
        return str
