# Bruteforce

def search(string_1, string_2):
    count = 0
    for i in range ((len(string_1)-len(string_2))+1):
        for j in range(len(string_2)):
                if string_1[i+j] != string_2[j]:
                    break
                elif j == len(string_2) - 1:
                    count += 1
    return count   

print('Here string_2 occur in string_1 ', search("i love muri .ilovemuri. muriislife .without mur i'm nothing . murei is valobasha", "muri") , ' times')