with open("input.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]
# print(content)
for i in range(len(content)):
    for j in range(i + 1, len(content)):
        for k in range(j + 1, len(content)):
            if content[i] + content[j] + content[k] == 2020:
                print(content[i],
                      "+", content[j],
                      "+", content[k],
                      "=", content[i] + content[j] + content[k],
                      ";", content[i],
                      "*", content[j],
                      "*", content[k],
                      "=", content[i] * content[j] * content[k])
                break