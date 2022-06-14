import main

print("Pair no.\t"+"Major Color\t"+"Minor Color")
print("--------\t"+"-----------\t"+"-----------")

count = 1
for i in range(len(main.MAJOR_COLORS)):
    for j in range(len(main.MINOR_COLORS)):
        print(str(count)+"\t\t"+main.MAJOR_COLORS[i]+"\t\t"+main.MINOR_COLORS[j])
        count=count+1
