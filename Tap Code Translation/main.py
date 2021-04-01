def tap_code_translation(text):
    table = [
        ['a', 'b', 'c/k', 'd', 'e'],
        ['f', 'g', 'h', 'i', 'j'],
        ['l', 'm', 'n', 'o', 'p'],
        ['q', 'r', 's', 't', 'u'],
        ['v', 'w', 'x', 'y', 'z'],
    ]

    result = ""

    for x in text:
        for i in table:
            if x in i:
                result += "." * (table.index(i) + 1) + " " + "." * (i.index(x) + 1) + " "
                break
            elif x == 'c' or x == 'k':
                result += ". ... "
                break 

    return result.strip()

print(tap_code_translation("breaks"), "->", ". .. .... .. . ..... . . . ... .... ...")
print(tap_code_translation("taps"), "->", ".... .... . . ... ..... .... ...")
print(tap_code_translation("knocks"), "->", ". ... ... ... ... .... . ... . ... .... ...")