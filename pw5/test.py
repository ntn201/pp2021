file = open("marks.txt","r")
c_id = 1
s_id = 3
m = 456
lines = file.readlines()
for i, l in enumerate(lines):
    if f"{c_id} {s_id}" in l:
        lines[i] = f"{c_id} {s_id} {m}"
file = open("marks.txt","w")
file.writelines(lines)
file.close()