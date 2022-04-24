"""
分别输入学生的数学成绩与英语成绩
成绩大于等于85为“优秀”；小于60为“不及格”；60~85为“良好”

Date: 2022-04-24
"""

math_score = float(input("请输入数学成绩："))
en_score = float(input("请输入英语成绩："))

if math_score >= 85 and en_score >= 85:
    grade = '优秀'
elif math_score < 60 and en_score < 60:
    grade = '不及格'
else:
    grade = '良好'

print("你两门课所属的等级为：", grade)
