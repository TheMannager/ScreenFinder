#Variable decleration

NUM        = 0
DENOM      = 1


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

#(x,y)
def simplify(numer, denom, which):

    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.
    if which == 0:
        return reduced_num
    if which == 1:
        return reduced_den

def find_height(size, vert, hor):
    ratio   = ((simplify(hor, vert, NUM)) / (simplify(hor, vert, DENOM)))
    return (size/((1 + ratio**2 )**(1/2)))

def find_width(size, vert, hor):
    ratio   = ((simplify(hor, vert, NUM)) / (simplify(hor, vert, DENOM)))
    return find_height(size, vert, hor) * ratio
