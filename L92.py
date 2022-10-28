#The authors are Maggie Dunn and Cody Brown
def remove_substring(string, sub):
    output = []
    index = 0
    while index < len(string):
        if string[index: index + len(sub)] == sub:
            index += len(sub)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))

