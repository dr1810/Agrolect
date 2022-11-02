from statistics import mean,stdev

def BESTU_BESTU(Crop_list,city):
    crop_name,avg_humidity=[i[1] for i in Crop_list],[i[2] for i in Crop_list]
    avg_ph,avg_temp,price=[i[3] for i in Crop_list],[i[4] for i in Crop_list],[i[5] for i in Crop_list]
    average_humidity=[60.0, 80.0, 101.5, 101.5, 70.0, 93.5, 108.5, 56.0, 100.0, 65.0, 101.5, 104.0, 92.5, 96.5, 104.0, 107.0, 106.5, 80.0, 95.0, 93.0, 87.5, 93.5, 61.5, 136.0, 70.0, 72.5, 80.0]
    average_ph=[10.5, 11.0, 10.0, 12.0, 10.5, 9.5, 11.0, 11.5, 12.0, 9.0, 9.5, 9.0, 10.5, 7.5, 7.0, 10.0, 9.5, 8.0, 9.5, 8.5, 8.0, 9.0, 8.0, 9.5, 10.0, 8.0, 8.5]
    average_temperature=[17.0,22.5,23,5.4,23.3,32,17.8,18.9,17.2,22.7,17.9,27,22.3,20.4,23,12.5,17,15,24.8,28,27.5,24.6,28.6,24.5,22,25.8,23.1]
    grade={'A':10,'B':9,'C':8,'D':7}
    credits={'H':3,'T':4,'PH':2,'P':1}
    C_gpa={}
    temp=['average_humidity','average_ph','average_temperature','price']
    crop_temp=['avg_humidity','avg_ph','avg_temp','price']
    print("crop",Crop_list)
    for i in range(27):
        grade_D=[1,2,3,4]
        for j in range(0,len(temp)):
            m=mean(eval(temp[j]))
            sd=stdev(eval(temp[j]),m)
            if eval(temp[j])[i]<=(eval(crop_temp[j][i])+0.5*sd) and eval(temp[j])[i]>=(eval(crop_temp[j])-0.5*sd):
                grade_D[j]='A'
                if temp[j]=="price":
                    grade_D[j]='D'
            elif eval(temp[j])[i]<=(eval(crop_temp[j][i])+1*sd) and eval(temp[j])[i]>=(eval(crop_temp[j][i])+0.5*sd) or eval(temp[j])[i]>=(eval(crop_temp[j][i])-1*sd) and eval(temp[j])[i]<=(eval(crop_temp[j][i])-0.5*sd):
                grade_D[j]='B'
                if temp[j]=="price":
                    grade_D[j]="C"
            elif eval(temp[j])[i]<=(eval(crop_temp[j][i])+1.5*sd) and eval(temp[j])[i]>=(eval(crop_temp[j][i])+1*sd) or eval(temp[j])[i]>=(eval(crop_temp[j][i])-1*sd) and eval(temp[j])[i]<=(eval(crop_temp[j][i])-1.5*sd):
                grade_D[j]='C'
                if temp[j] == "price":
                    grade_D[j] = 'B'
            elif eval(temp[j])[i]>=(eval(crop_temp[j][i])+1.5*sd) or eval(temp[j])[i]>=(eval(crop_temp[j][i])-1.5*sd):
                grade_D[j]='D'
                if temp[j]=="price":
                    grade_D[j]='A'
        print(grade_D)
        gpa=(grade[grade_D[0]]*credits['H']+grade[grade_D[2]]*credits['T']+grade[grade_D[1]]*credits['PH'])/9
        C_gpa[crop_name[i]]=gpa
    name,grade=[],[]
    for i in sorted(C_gpa.values()):
        for j in C_gpa:
            if C_gpa[j]==i:
                name.append(j)
                grade.append(i)
    grade.reverse()
    name.reverse()
    print("NAME\n",name,"Grade\n",grade)
    return [name,grade]