#The authors are Maggie Dunn and Cody Brown
def replace_substring(string, sub, replacement):
    output = []
    index = 0
    while index < len(string):
        if string[index: index + len(sub)] == sub:
            output.append(replacement)
            index += len(sub)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))


st = "My name is Maggie and I hate coding"
sub = "hate"
re = "love"

replace_substring(st, sub, re)
