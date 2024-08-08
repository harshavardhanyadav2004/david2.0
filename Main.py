import pandas as pd
import random
names = ["B.Sri Harsha Vardhan","S.Hemanth Srinivas","N.Charan Manikanta","P.Naveen",
         "G.Gayatri","k.Preethi Karen","B.Gowtham","M.Yeshwanth",
         "p.Likitha","M.Vijay Kumar","N.Raghavendra","M.Vinay",
         "G.Naimisha","D.Vasanth","M.Jitendra","B.Vivek",
         "Barnali Das","A.Vidhan","K.Srinath","P.Phani Kumar"         
         ]
Gender = ["M","M","M","M",
          "F","F","M","M",
          "F","M","M","M",
          "F","M","M","M",
          "F","M","M","M"
          ]
status_list = [0, 1]
rolls_list = ["21981a44{:02d}".format(i) for i in range(1, 21)]
emails = [name.lower().replace(" ", "") + "@gmail.com" for name in names]
phone_numbers = []
for i in range(20): 
  new_str = str('+91 ')+random.choice(['6','7','8','9'])
  for new_number in range(1,10):
     new_str+=random.choice("1234567890")
  phone_numbers.append(new_str)
attendance_periods = [[str(random.choice(status_list)) for _ in range(1, 9)] for _ in range(1,21)]
data_frame = pd.DataFrame({
    "Name": names,
    "Roll": rolls_list,
    "Email": emails,
    "Phone Number": phone_numbers,
    "Attendance Periods": [" : ".join(periods) for periods in attendance_periods],
    "Section": ["CSM"] * 20,
    "Gender":Gender
})
# Converting into the CSV File
data_frame.to_csv("attendance.csv", index=False)

print(data_frame.head())





