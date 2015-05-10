def name_banner():
    name = raw_input("enter your name: ")

    if name:
        length_name = range(len(name) + 4)
        list = []
        print "".join(["*" for i in length_name])
        for i in length_name:
            if i >=  2 and i <= len(name) + 1:
                list.append(name[i-2])
            else:
                list.append("*")
            
        print "".join(list)
        print "".join(["*" for i in length_name])