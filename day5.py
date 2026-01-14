print('============🥇STUDENTS MARKS MANAGER🥇==============')
marks=[]
while True:
 sub=int(input('Enter How Many Subjects are there:'))
 for i in range(sub):
    mark=int(input('Enter Marks='))
    marks.append(mark)
 avg=sum(marks)/len(marks)
 total=sum(marks)
 outoff=len(marks)*100
 h=max(marks)
 l=min(marks)
 if avg > 90:
    print('A+ GRADE')
 elif avg >=80 and avg <=90:
    print('A GARDE')
 elif avg >=70 and avg<=80:
    print("B GRADE")
 elif avg >=60 and avg<=70:
    print('C GRADE')
 elif avg >=50 and avg<=60:
    print('D GARDE')
 elif avg>=40 and avg <=50:
    print('E GARDE')
 elif avg==35:
    print('FAIL')
 print('Percentage=',avg,'Highest=',h,'Lowest=',l,"Total=",total,'/',outoff)