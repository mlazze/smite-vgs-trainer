"""get content of smite site and parse it"""
try:
    import os
    os.system('clear')
    import re
    import random

    FH = open('parsed.txt',"r")
    text = FH.read()

    tmp_list = text.split("$$$")
    tmp_list = filter(None, tmp_list)
    DICT = {}

    for group in tmp_list:
        elements = group.split("\n")
        match = re.search("(V[A-Z]*) - ", elements.pop(0))
        if match:
            partial = match.group(1)
        else: 
            exit(1)
        elements = filter(None, elements)

        for i in elements:
            match = re.search("([A-Z0-9]*)[ ]*([^(  )].*)[ ]*", i)
            if match:
                DICT[partial + match.group(1)] = match.group(2)
            else: exit(1)

    #print DICT
    totali = 0
    first = 0
    errati = 0
    while True:
        hadato = 0
        num = 0
        start = 1
        current_key = random.choice(DICT.keys())
        current_value = DICT[current_key]
        ans = None
        while ans == None or ans != current_key:
            ans = str(raw_input("\033[1;44mFrase = " + current_value + "\033[1;m\n"))
            if ans == "":
                num += 1
                print("\033[1;33mSuggerimento = " + current_key[0:num] + "\033[1;m\n")
            else:
                ans = ans.upper()
                if ans != current_key:
                    print "\033[1;38mErrato\033[1;m"
                    try:
                        print ans + " = " + DICT[ans]
                    except KeyError:
                        pass
                    if hadato == 0:
                        hadato += 1
                        errati += 1

        print("\033[1;32mCorretto, " + current_key + " = " + current_value + "\033[1;m\n")
        os.system('clear')
        if num == 0 and hadato == 0:
            first += 1
        totali += 1
except KeyboardInterrupt:
    try:
        print "\033[1;32m\rCorretti al primo:\033[1;m " + str(first) + " (" + str(float(first)/float(totali)*100)[0:5] + "%)"
        print "\033[1;31mErrati:\033[1;m " + str(errati) + " (" + str(float(errati)/float(totali)*100)[0:5] + "%)"
        print "Totali: " + str(totali) + " (" + str(float(totali)/float(totali)*100)[0:5] + "%)"
        print "\033[1;m"
    except ZeroDivisionError:
        print "\033[1;32m\rCorretti al primo:\033[1;m " + str(first) + " (" + str(100) + "%)"
        print "\033[1;31mErrati:\033[1;m " + str(errati) + " (" + str(100) + "%)"
        print "Totali: " + str(totali) + " (" + str(100) + "%)"
        print "\033[1;m"