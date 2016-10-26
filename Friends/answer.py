from collections import defaultdict

class Friends:
    def __init__(self, connections):
        self.link = defaultdict(set)
        for a,b in connections:
            self.link[a].add(b)
            self.link[b].add(a)

    def add(self, connection):
        a,b = connection
        if a in self.link and b in self.link[a]:
            return False
        else:
            self.link[a].add(b)
            self.link[b].add(a)
            return True

    def remove(self, connection):
        a,b = connection
        if a in self.link and b in self.link[a]:
            self.link[a].remove(b)
            self.link[b].remove(a)
            if not self.link[a]:
                del self.link[a]
            if not self.link[b]:
                del self.link[b]
            return True
        else:
            return False

    def names(self):
        print self.link
        return set(self.link.keys())

    def connected(self, name):
        return self.link[name]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
