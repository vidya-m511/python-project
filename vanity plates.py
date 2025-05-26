
def main():
    plate = input("plate :")
    if is_valid (plate):
        print("valid")
    else:
        print("invalid")

def is_valid (v):
    if len(v)<2 or len(v)>6:
        return False 


    if v[0].isalpha()==False or v[1].isalpha() ==False:    
        return False

    i = 0
    while i<len(v):
        if v[i].isalpha()==False:
            if v[i]== "0":
                return False
            else:
                break

        i +=1


    for z in v:
        if z in ['.',' ','!','?']:
            return False

    return True
main()                
