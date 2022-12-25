import os
from os import listdir
from os.path import isfile, join

alf = {'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'E','Ж':'ZH','З':'Z','И':'I','Й':'Y','К':'K','Л':'L','М':'M','Н':'N','О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H','Ц':'TS','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':"'",'Ы':'I','Ь':'','Э':'E','Ю':'YU','Я':'YA',
       'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e','ж':'zh','з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h','ц':'ts','ч':'ch','ш':'sh','щ':'sch','ъ':"'",'ы':'i','ь':'','э':'e','ю':'yu','я':'ya'}
mypath = input("Enter the path to the files: ")
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i, name in enumerate(onlyfiles):
    print("PROCESSING: " + str(i) + " of " + str(len(onlyfiles)) + ' "' + name + '"')
    name_2 = ''
    name = name.lower()
    for ch in name:
        if ch in alf:
            name_2 += alf[ch]
        else:
            name_2 += ch
    if name != name_2:
        os.rename(os.path.join(mypath, name), os.path.join(mypath, name_2))
end = input("Press any key to continue...")
