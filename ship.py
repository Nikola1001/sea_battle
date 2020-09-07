'''строится 3-палубный корабль'''

def virtShip(x, y, fleet):
    virt = []
    for i in range(x - 2, x + 1):
        virt.append((i, y))
    return virt

def three(fleet):
    '''выбор первой палубы'''
    return fleet

if __name__ == '__main__':
    fleet = [[0 for j in range(10)] for i in range(10)]
    three(fleet)
