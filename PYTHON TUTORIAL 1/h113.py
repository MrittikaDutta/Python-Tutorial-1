def split_and_join(line):
    for i in range(len(line)):
        if line[i]==" ":
            line=line[0:i]+"-"+line[i+1:]
    print(line)  

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    