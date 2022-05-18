import re

pattern = "a0"
string = "a00"

prog = re.compile(pattern)
search = prog.search(string)
full_match = prog.full_match(string)

s = '<html><head><title>Title</title>'
pattern = '<'
prog = re.compile(pattern)
match = prog.match(s)
if match:
    print(match.group(0), match.start(0))
print()

print("The type of compile is", type(prog))
print("The value of compile is", prog)

print("The type of search is", type(search))
print("The value of search is", search)

print("The type of match is", type(match))
print("The value of match is", match)

print("The type of full_match is", type(full_match))
print("The value of full_match is", full_match)

print("The type of compile is", type(prog))
print("The value of compile is", prog)
