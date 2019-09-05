class Stack:
    def __init__(self):
        self.deva = []
    def is_empty(self):
        return self.deva == []
    def push(self, data):
        self.deva.append(data)
    def pop(self):
        return self.deva.pop()
subi= Stack()
barathii = input(' ') 
for char in barathii:
    subi.push(char)
rev_text = ''
while not subi.is_empty():
    rev_text = rev_text + subi.pop()
if barathii== rev_text:
    print('YES')
else:
    print('NO')
