import time

start = time.time()
line = {} # строки
k = 0
spisok = []
with open("C:/d/100.csv") as f:
    f.seek(45)
    for i in range(5000005):
        line[i] = f.readline() #чтение строки из файла как массив
        m = line[i] #присваиваем локальной переменной строку в массиве
        #print(m,'\n')
        s = ""
        if m !="":
            if m[0]=='"':
                #print(m)
                n = (m[1:-2]) #убирает кавычки спереди и в конце
                calday = (n.partition (',')[0]) #здесь с помощью даного метода отделяем дату
                other = (n.partition (',')[2]) #здесь идет отделение остального после даты, после запятой, и присвоение переменной
                descr = (other.partition (',')[0]) #здесь идет отделение описания от остального и присвоение переменной
                other2 = (other.partition (',')[2]) 
                #print(other2)
                a = []
                b = 0
                c = []
                d = 0
                
                for j in other2:
                    a.append(j)
                    if a[0]=='"':
                        b=1
                    else:
                        b=2
                if b==1:
                    other2=(other2[2:])
                    other2=(other2.partition ('"')[2])
                    other2=(other2[2:])
                    if other2[0]=='"':
                        other2 = other2[2:]
                        other2=(other2.partition ('"')[0])
                    else:
                        other2=(other2.partition (',')[0])
                    other2 = (other2.translate({ord(','): None}))
                    other2 = (other2.translate({ord('"'): None}))
                else:
                    other2=(other2.partition (',')[2])
                    for k in other2:
                        c.append(k)
                        if c[0]=='"':
                            d=1
                        else:
                            d=2
                    if d==1:
                        other2=(other2[2:])
                        other2=(other2.partition ('"')[0])
                    else:
                        other2=(other2.partition (',')[0])
                    other2 = (other2.translate({ord(','): None}))
                    other2 = (other2.translate({ord('"'): None}))
                #print(other2)
                spisok2 = [i,calday,descr,other2]
                spisok.append(spisok2)
                i +=1
                #print(spisok)
            else:
                calday_2 = (m.partition(',')[0])
                other_2 = (m.partition (',')[2])
                descr_2 = (other_2.partition (',')[0])
                other_3 = (other_2.partition (',')[2])
                other_4 = (other_3.partition (',')[2])
                withdr = (other_4.partition (',')[0])
                spisok3 = [i,calday_2,descr_2,withdr]
                spisok.append(spisok3)
                i +=1
                #print(spisok)
        else:
            break

spisok3 = spisok.pop(0)
#print(spisok,'\n')
date_unique = []
descr_unique = []
for x in range(len(spisok)):
    for y in range(1):
        spisok[x][3] = float (spisok[x][3])
        date_unique.append(spisok[x][1])
        descr_unique.append(spisok[x][2])
        
set_date = set(date_unique)
set_descr = set(descr_unique)

list_date = (list(set_date))
list_descr = (list(set_descr))

date_count = 0
descr_count = 0

for item in list_date:
    date_count +=1
for item in list_descr:
    descr_count +=1
abc = ('Date,Min,Max,Averegae\n')    

#######################################################################################
f = open('by_date_and_type.csv', 'w')
f.write(abc)

for date_cycle1 in range(len(list_date)):
    peremen1 = list_date[date_cycle1]
    for descr_cycle in range(len(list_descr)):
        peremen2 = list_descr[descr_cycle]
        output_text2 = []
        count_1 = 0
        summ=0
        #avg=0
        min_val = 50000000000.00
        max_val = 0.00
        bool_val = 0
        for date_cycle2 in range(len(spisok)):
            if (spisok[date_cycle2][1]==peremen1) and (spisok[date_cycle2][2]==peremen2):
                #print(peremen1,spisok[date_cycle2][1],peremen2,spisok[date_cycle2][2],spisok[date_cycle2][3])
                summ = summ + spisok[date_cycle2][3]
                count_1 +=1
                bool_val=1
                if spisok[date_cycle2][3] <= min_val:
                    min_val = spisok[date_cycle2][3]
                if spisok[date_cycle2][3] >= max_val:
                    max_val = spisok[date_cycle2][3]
            else:
                pass

        if bool_val != 0:
            avg = summ/count_1
            output_text2 = peremen1,peremen2,('%.2f' % min_val),('%.2f' % max_val),('%.2f' % avg)
            output_text = str (output_text2)
            print(output_text)
            f.write(output_text + '\n')
f.close()
##########################################################################################
f = open('by_date.csv', 'w')
f.write(abc)

for date_cycle1 in range(len(list_date)):
    peremen1 = list_date[date_cycle1]
    #print(date_cycle1)
    #print(peremen1)
    output_text1 = []
    count_1 = 0
    summ=0
    avg=0
    min_val = 50000000000.00
    max_val = 0.00
    for date_cycle2 in range(len(spisok)):
        if spisok[date_cycle2][1]==peremen1:
            summ = summ + spisok[date_cycle2][3]
            count_1 +=1
            if spisok[date_cycle2][3] <= min_val:
                min_val = spisok[date_cycle2][3]
            if spisok[date_cycle2][3] >= max_val:
                max_val = spisok[date_cycle2][3]
    avg = summ/count_1
    
    output_text1 = peremen1,('%.2f' % min_val),('%.2f' % max_val),('%.2f' % avg)
    output_text = str (output_text1)
    #print(output_text)
    f.write(output_text + '\n')
f.close()

end = time.time()
result = end - start
print('Time for execution is:')
print(result)






