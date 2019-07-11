def string_length(string):
    if len(string) < 8:
        return "false"
    else:
        return "true"

print(string_length("general"))
print(string_length("assembly"))
print(string_length("functions"))
print(string_length("python"))
