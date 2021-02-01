import re

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def validate_html(html):
    """
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.
    #>>> validate_html('<strong>example</strong>')
    True
    #>>> validate_html('<strong>example')
    False
    """
    tags = _extract_tags(html)
    s = Stack()
    balanced = True
    index = 0

    while index < len(tags) and balanced:
        tag = tags[index]
        if '/' not in tag:
            s.push(tag)
        #print(s.peek())
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not match(top, tag):
                    balanced = False
        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


def match(first, second):
    first_rep, second_rep = first.replace('<', ""), second.replace('<', "")
    first_rep, second_rep = first.replace('<', ""), second.replace('<', "")
    first_rep, second_rep = first.replace('/', ""), second.replace('/', "")
    return first_rep == second_rep

def _extract_tags(html):
    """
    Helper function for `validate_html`.
    :argument takes a string input
    :returns list of all html tags contained in the input string
    """
    tags = re.findall(r'<[^>]+>', html)

    return tags


yo = '<strong>example'

print(validate_html(yo))
