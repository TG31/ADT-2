# Exercise 1
Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append(-1)

def Push(Item):
    global TopOfStack, Stack
    if TopOfStack == 7:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = Item
        return True

def Pop():
    global TopOfStack, Stack
    if TopOfStack == -1:
        return -1
    else:
        Top = Stack[TopOfStack]
        TopOfStack -= 1
    return Top


# Exercise 2
Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append(-1)

def ShowStack():
    global TopOfStack, Stack
    Str = ""
    for i in range(TopOfStack, -1, -1):
        Str = Str + str(Stack[i]) + " "
    return Str.strip()


# Exercise 3
Stack = []
TopOfStack = -1

for i in range(8):
    Stack.append(-1)


def Push(Item):
    global Stack, TopOfStack

    if TopOfStack == 7:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = Item
        return True


def Pop():
    global Stack, TopOfStack

    if TopOfStack == -1:
        return -1
    else:
        Item = Stack[TopOfStack]
        TopOfStack -= 1
        return Item


def DecimalToBinary(Number):
    global Stack, TopOfStack

    TopOfStack = -1

    if Number == 0:
        return "0"

    while Number > 0:
        Push(Number % 2)
        Number = Number // 2

    Str = ""

    while TopOfStack != -1:
        Str = Str + str(Pop())

    return Str


# Exercise 4
Stack = []
TopOfStack = -1

for i in range(8):
    Stack.append(-1)


def Push(Item):
    global Stack, TopOfStack

    if TopOfStack == 7:
        return False
    else:
        TopOfStack += 1
        Stack[TopOfStack] = Item
        return True


def Pop():
    global Stack, TopOfStack

    if TopOfStack == -1:
        return -1
    else:
        Item = Stack[TopOfStack]
        TopOfStack -= 1
        return Item


def Editor(Commands):
    global Stack, TopOfStack

    TopOfStack = -1

    for command in Commands:
        parts = command.split(" ")

        if parts[0] == "type":
            Push(parts[1])

        elif parts[0] == "undo":
            Pop()

    Str = ""

    for i in range(0, TopOfStack + 1):
        Str = Str + Stack[i]

    return Str
