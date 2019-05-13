class Node:#1 is black and 0 is red

    def __init__(self, val, parent, color: bool, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

    def __repr__(self):
        if not self.color:
            col = "Red"
        else:
            col = "Black"
        return "{color} {val} Node".format(color=col, val=self.val)

    def __eq__(self, other):

        if self.val == other.val:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.val < other.val:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.val > other.val:
            return True
        else:
            return False

    def swapColor(self):
        if self.color is False:
            self.color = True
        else:
            self.color = False






