def build_table(l):
    # Use a dictionary to build a frequency table
    frequency = {}

    # For each number, create a new entry in the table or increment the frequency
    for n in l:
        if n in frequency.keys():
            frequency[n] = frequency[n] + 1
        else:
            frequency[n] = 1

    return(frequency)

def sort_table(fdict):
    # First build a list of the form (r,n)
    flist = [ (fdict[n],n) for n in fdict.keys() ]

    # Sort this list using built in sort, which will sort first by frequency, then by value
    flist.sort()

    # Flip each pair and return
    return( [ (n,r) for (r,n) in flist ])

def histogram(l):
    frequency_table = build_table(l)
    return(sort_table(frequency_table))

def transcript(coursedetails,studentdetails,grades):

    coursedict = setup_coursedict(coursedetails)
    studentdict = setup_studentdict(studentdetails)
    gradedict = setup_gradedict(grades)


    outputlist = []

    for r in sorted(gradedict.keys()):
        gradelist = []
        for (ccode,grade) in sorted(gradedict[r]):
            gradelist.append((ccode,coursedict[ccode],grade))

        outputlist.append((r,studentdict[r],gradelist))

    return(outputlist)

def setup_coursedict(details):

    dict = {}
    for (ccode,cname) in details:
        dict[ccode] = cname

    return(dict)

def setup_studentdict(details):

    dict = {}
    for (rollno,name) in details:
        dict[rollno] = name

    return(dict)

def setup_gradedict(details):

    dict = {}
    for (rollno,ccode,grade) in details:
        if rollno in dict.keys():
            dict[rollno].append((ccode,grade))
        else:
            dict[rollno] = [(ccode,grade)]

    return(dict)
# Hidden code below

import ast

fncall = input()
lparen = fncall.find("(")
rparen = fncall.rfind(")")
fname = fncall[:lparen]
farg = fncall[lparen+1:rparen]

if fname == "histogram":
   arg = ast.literal_eval(farg)
   print(histogram(arg),end="\n")
elif fname == "transcript":
   arg = ast.literal_eval(farg)
   print(transcript(arg[0],arg[1],arg[2]),end="\n")
else:
   print("Function", fname, "unknown")