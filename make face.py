
def main():
    msg = input()
    result = convert(msg)
    print(result)

def convert(msg):
    string = msg.replace(":)",'-_-')
    string1 = string.replace(":(", '-__-')
    return string1

main()

