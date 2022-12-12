max_psums = []
psum = 0
for line in open("input.txt"):
    line = line.strip()

    if len(line) > 0:
        psum += int(line)
    else:
        max_psums.append(psum)
        psum = 0

print(sum(sorted(max_psums)[-3:]))