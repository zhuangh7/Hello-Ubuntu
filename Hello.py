def Hex_to_RGB(hex):
    r = int(hex[1:3],16)
    g = int(hex[3:5],16)
    b = int(hex[5:7], 16)
    rgb = str(r)+';'+str(g)+';'+str(b)
    return rgb

outbuf=""

with open("chars_","r") as f:
    ab = f.read().split(" ")
    for line in ab:
        if line.startswith("color"):
            line = line[7:]
            # if line[0] == '\':
            if line[0] == '#':
                rgb_ = Hex_to_RGB(line[0:7])
                print(rgb_)
                char_ = line.split("<")[0][9:]
                print(char_)
                outbuf += "\\033[38;2;"+rgb_+"m"+char_+"\\033[0m"
            if "<br>" in line:
                outbuf += "\\n"

out = open("out_", "w")
#print("echo -en \""+outbuf+"\"", file=out)
print("echo \""+outbuf+"\"", file=out)
