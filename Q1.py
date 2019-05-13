"""
Question A

Your goal for this question is to write a program that accepts two lines (x1,x2)
and (x3,x4) on the x-axis and returns whether they overlap. As an example,
(1,5) and (2,6) overlaps but not (1,5) and (6,8).
"""
def overlap(line1, line2):
    """Determines if line1 and line2 intersect one another, this assumes the
    input must be a line1 and not a single point.

    Args:
        line1: Line 1 on the 1D x-axis, aceepts a tuple.
        line2: Line 2 on the 1D x-axis, accepts a tuple.

    Returns:
        The return value. True for overlap, False otherwise.
    """
    line1_range = range(line1[0],line1[1])
    if (line2[0] in line1_range or line2[1] in line1_range ):
        return True
    return False

#Some tests
if __name__ == "__main__":
    print(overlap((1,2),(1,5))) #True
    print(overlap((6,8),(1,5))) #False
    print(overlap((-1,8),(-2,5))) #True
    print(overlap((-10,-1),(-20,-11))) #False
    print(overlap((-10,-1),(-20,-5))) #True
    print(overlap((-20,-5),(-1,-9))) #True
#(1,5) and (2,6) overlaps but not (1,5) and (6,8)
