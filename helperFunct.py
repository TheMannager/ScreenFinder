#height = diagonal / sqrt(1 + ratio^2)
def find_height(size, vert, hor):
    return size / ((1 + (hor / float(vert))**(2))**(1/float(2)))


def find_width(size, vert, hor):
    return find_height(size, vert, hor) * (hor / float(vert))
