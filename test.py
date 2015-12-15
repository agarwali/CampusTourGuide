import sys
import unittest


def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def main():
    
    v = [2, 3]
    possibleMoves =  [1, 2, 3, 4]
    print [move for move in possibleMoves if move not in v]

    ls = ['asd', 'sd','sd', 'asd']
    cities = []
    for i in ls:
        try:
            a= int(i)
        except:
            cities.append(i)
    print cities

main()