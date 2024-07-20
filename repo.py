print(my_cookok_list[0])
print(my_cookok_list[1])
print(my_cookok_list[2])
print(my_cookok_list[3])
print(my_cookok_list[4])
print(my_cookok_list[5])
print(my_cookok_list[6])
print(my_cookok_list[7])
print(my_cookok_list[8])
print(my_cookok_list[9])
print(my_cookok_list[10])
print(my_cookok_list[11])
print(my_cookok_list[12])
print(my_cookok_list[13])
print(my_cookok_list[14])
print(my_cookok_list[15])
print(my_cookok_list[16])
print(my_cookok_list[17])
print(my_cookok_list[18])
print(my_cookok_list[19])
print(my_cookok_list[20])
print(my_cookok_list[21])
print(my_cookok_list[22])
print(my_cookok_list[23])
print(my_cookok_list[24])
print(my_cookok_list[25])
print(my_cookok_list[26])
print(my_cookok_list[27])
print(my_cookok_list[28])
print(my_cookok_list[29])
print(my_cookok_list[30])
print(my_cookok_list[31])
print(my_cookok_list[32])
print(my_cookok_list[33])
print(my_cookok_list[34])
print(my_cookok_list[35])
print(my_cookok_list[36])
print(my_cookok_list[37])
print(my_cookok_list[38])
print(my_cookok_list[39])
print(my_cookok_list[40])
print(my_cookok_list[41])
print(my_cookok_list[42])
print(my_cookok_list[43])
print(my_cookok_list[44])
print(my_cookok_list[45])
print(my_cookok_list[46])
print(my_cookok_list[47])
print(my_cookok_list[48])
print(my_cookok_list[49])
print(my_cookok_list[50])
print(my_cookok_list[51])
print(my_cookok_list[52])
print(my_cookok_list[53])
print(my_cookok_list[54])
print(my_cookok_list[55])
print(my_cookok_list[56])
print(my_cookok_list[57])
print(my_cookok_list[58])
print(my_cookok_list[59])
print(my_cookok_list[60])
print(my_cookok_list[61])
print(my_cookok_list[62])
print(my_cookok_list[63])
print(my_cookok_list[64])
print(my_cookok_list[65])
print(my_cookok_list[66])
print(my_cookok_list[67])
print(my_cookok_list[68])
print(my_cookok_list[69])
print(my_cookok_list[70])
print(my_cookok_list[71])
print(my_cookok_list[72])
print(my_cookok_list[73])
print(my_cookok_list[74])
print(my_cookok_list[75])
print(my_cookok_list[76])
print(my_cookok_list[77])
print(my_cookok_list[78])
print(my_cookok_list[79])
print(my_cookok_list[80])
print(my_cookok_list[81])
print(my_cookok_list[82])
print(my_cookok_list[83])
print(my_cookok_list[84])
print(my_cookok_list[85])
print(my_cookok_list[86])
print(my_cookok_list[87])
print(my_cookok_list[88])
print(my_cookok_list[89])
print(my_cookok_list[90])
print(my_cookok_list[91])
print(my_cookok_list[92])
print(my_cookok_list[93])
print(my_cookok_list[94])
print(my_cookok_list[95])
print(my_cookok_list[96])
print(my_cookok_list[97])
print(my_cookok_list[98])
print(my_cookok_list[99])




import random

first_names = [
    "John", "Jane", "Michael", "Sarah", "David", "Emily", "Robert", "Laura", "James", "Jessica",
    "Daniel", "Mary", "Paul", "Jennifer", "Mark", "Linda", "Chris", "Elizabeth", "Andrew", "Susan",
    "Matthew", "Angela", "Joshua", "Karen", "Kevin", "Lisa", "Brian", "Nancy", "Charles", "Margaret",
    "Steven", "Sandra", "Anthony", "Ashley", "Donald", "Kimberly", "Timothy", "Michelle", "Jason", "Deborah",
    "Joseph", "Laura", "George", "Helen", "Thomas", "Cynthia", "Frank", "Donna", "Patrick", "Carol"
]

surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
]

# Generate the list of 100 names
names_list = [f"{random.choice(first_names)} {random.choice(surnames)}" for _ in range(100)]

# Print each name
for i in range(100):
    print(names_list[i])
    # -----------------------------------------------


