def hunk_start(header):
    # header looks like "@@ -0,0 +1,2 @@"
    plus_start=header.split()[2]
    start=plus_start[1:].split(",")[0]
    return int(start)

def added_lines(patch):
    result=[]
    current=0
    for line in patch.splitlines():
        if line.startswith("@@"):
            current=hunk_start(line)
        elif line.startswith("+"):
            result.append(current)
            current+=1
        elif line.startswith("-") or line.startswith("\\"):
            continue
        else:
            current+=1
    return result

if __name__=="__main__":
    example="@@ -0,0 +1 @@\n+# Diagrams\n\\ No newline at end of file"
    print(added_lines(example))