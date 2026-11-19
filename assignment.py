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
    Top = 0
    if TopOfStack == -1:
        return False
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

def DecimalToBinary(Number):
    global Stack, TopOfStack
    TopOfStack = -1
    Str = ""
    if Number == 0:
        return 0
    else:
        while Number > 0:
            TopOfStack += 1
            Stack[TopOfStack] = Number % 2
            Number = Number // 2
        for i in range(TopOfStack, -1, -1):
            Str = Str + str(Stack[i])
        return Str


# Exercise 4
Stack = []
TopOfStack = -1
for i in range(8):
    Stack.append(-1)

def Editor(Commands):
    global Stack, TopOfStack
    TopOfStack = -1
    for command in Commands:
        parts = command.split(" ")
        if parts[0] == "type":
            if TopOfStack < 7:
                TopOfStack += 1
                Stack[TopOfStack] = parts[1]
        elif parts[0] == "undo":
            if TopOfStack != -1:
                TopOfStack -= 1
    Str = ""
    for i in range(0, TopOfStack + 1):
        Str = Str + Stack[i]
    return Str
