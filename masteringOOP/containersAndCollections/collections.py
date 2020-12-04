import collections
import weakref


class Tree(collections.abc.MutableSet):
    def __init__(self, iterable=None):
        self.root = TreeNode(None)
        self.size = 0
        if iterable:
            for item in iterable:
                self.root.add(item)

    def add(self, item):
        self.root.add(item)
        self.size += 1

    def discard(self, item):
        try:
            self.root.more.remove(item)
            self.size -= 1
        except KeyError:
            pass

    def __contains__(self, item):
        try:
            self.root.more.find(item)
            return True
        except KeyError:
            return False

    def __iter__(self):
        for item in iter(self.root.more):
            yield item

    def __len__(self):
        return self.size


t1 = Tree()


class TreeNode:
    def __init__(self, item, less=None, more=None, parent=None):
        self.item = item
        self.less = less
        self.more = more
        if parent != None:
            self.parent = parent

    @property
    def parent(self):
        return self.parent_ref()

    @parent.setter
    def parent(self, value):
        self.parent_ref = weakref.ref(value)

    def __repr__(self):
        return ("TreeNode({item!r},{less!r},{more!r})".format(**self.__dict__))

    def find(self, item):
        if self.item is None:  # Root
            if self.more: return self.more.find(item)
        elif self.item == item:
            return self
        elif self.item > item and self.less:
            return self.less.find(item)
        elif self.item < item and self.more:
            return self.more.find(item)
        raise KeyError

    def __iter__(self):
        if self.less:
            for item in iter(self.less):
                yield item
        yield self.item
        if self.more:
            for item in iter(self.more):
                yield item

    def add(self, item):
        if self.item is None:  # Root Special Case
            if self.more:
                self.more.add(item)
            else:
                self.more = TreeNode(item, parent=self)
        elif self.item >= item:
            if self.less:
                self.less.add(item)
            else:
                self.less = TreeNode(item, parent=self)
        elif self.item < item:
            if self.more:
                self.more.add(item)
            else:
                self.more = TreeNode(item, parent=self)


s1 = Tree(["Item 1", "Another", "Middle"])
print(s1)
