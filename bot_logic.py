
import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password
def remoji():
    emojis = [":+1",":smile:", ":grinning:", ":zany_face:", ":wink:"]
    emoji = random.choice(emojis)

    return emoji

def randomnum():
    num = random.randint(1, 100)

    return num

def algo():
    alg = random.randint(1, 3)
    if alg == 1:
        gen_pass()
    elif alg == 2:
        remoji()
    else:
        randomnum()
    return alg