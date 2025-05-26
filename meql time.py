
def main():
    time = input("what time is it?")
    ans = convert(time)
    if ans >= 7 and ans <=8 :
        print("breakfast time")
    if ans >=12 and ans <=13:
        print("lunch time") 
    if ans >= 17 and ans <=19:
        print("dinner time")


def convert(ans):
    hours, minutes = ans.split(":") 
    minute = float(minutes)/60
    return float(hours) + minute   


if __name__ =="__main__":
    main ()







