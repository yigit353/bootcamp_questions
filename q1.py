'''
Check if two circles intersect given by the user input x, y, r
'''

__author__ = 'Yigit Bekir Kaya <admin@cbilab.org>'

try:
    # First circle
    x1 = int(raw_input("First circle's center x: "))
    y1 = int(raw_input("First circle's center y: "))
    r1 = int(raw_input("First circle's radius: "))

    # Second circle
    x2 = int(raw_input("Second circle's center x: "))
    y2 = int(raw_input("Second circle's center y: "))
    r2 = int(raw_input("Second circle's radius: "))

    # Euclidean distance between centers of the circles
    distance_centers = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if distance_centers <= r1 + r2:
        print 'Circles intersect'
    else:
        print 'Circles does not intersect'
except:
    print 'All of the values should be integers!'
