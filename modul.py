#import unittest

def f(s):

    i = len(s)
    while s[i-1] == '':
        i -= 1
        s = s[:i]

    print(s)

    j = len(s) - 1
    while j != 0:
        if s[j] == u'':
            i = j
            while s[i] == '':
                s[i:j] = ''
                j = i
                i -= 1
                if i == 0:
                    break
        j -= 1
    print(s)

    i = 0
    while s[i] == '':
        i += 1
    else:
        del s[:i]

    print(s)


'''
class Test(unittest.TestCase):
    def test_normal(self):
        res = f( ["", "abc", "123", "", "x", "", "", "y", "", "" ] )
        self.assertEqual( res, ["abc", "123", "", "x", "", "y"] )
'''
if __name__ == '__main__':
    #unittest.main()
    print( f(["", "","","","","","","abc", "123", "","","","","","","","","","","", "x", "", "","","","","","","","","", "y","","","","","","", "", "" ]) )