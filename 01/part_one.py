max_psum = -1
psum = 0
for line in open("input.txt"):
    line = line.strip()

    if len(line) > 0:
        psum += int(line)
    else:
        max_psum = max(psum, max_psum)
        psum = 0

print(max_psum)