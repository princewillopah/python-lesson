# def text(name):
#     print("i am from {}".format(name))
# def num(name, age, *ar):
#     print("i am %s, and %d years old and my friends re %s "%(name,age,ar))
#     for i in ar:
#         print(i)
#     for i in ar:
#         print(i,end=" ")
# def dick(**names):
#     print("names are ", names["first"],names["second"],names["third"])
#
# def dick1(a, b,*tuples,**namesset):
#     print("names are ",a,b,tuples, namesset["first"], namesset["second"], namesset["third"])
# num("prince",56,"tony","grace","alade",78)
# dick(first="tony",second="rose",third="lola")
# dick1("my ",5,7,78,89,89,first="tony",second="rose",third="lola")

# -----------------------return-----------------------
# def myRange():
#    print("range is :",perform())
#    for i in perform():
#        print(i,end=" ")
#
# def perform(start,end,step):
#     return range(start,end,step)
#
# start_num=int(input("enter start number: "))
# end_num=int(input("enter end number: "))
# step_num=int(input("enter step number: "))
# perform(start_num,end_num,step_num)
# myRange()

# ----------------------recharge card--------------------------------
# import random
# class RandomGenerator:
#     def __init__(self):
#         self.min_number = 1111
#         self.max_number = 9999
#     def getMaxNumber(self):
#         return self.max_number
#     def getMinNumber(self):
#         return self.min_number
#     # def setMaxNumber(self, maxNum):
#     #     self.max_number = maxNum
#     # def setMinNumber(self, minNum):
#     #     self.min_number = minNum
#     def getRandom(self):
#         return random.randint(self.min_number, self.max_number)
# ran = RandomGenerator()  # INITIALS ARE ALREADY GENERATED
# for i in range(5):  # print it five times
#     print(ran.getRandom(),end=" ")
#
# =====================single inheritance================================
# class Apple:
#     manufacturer="Apple inc."
#     contactWebsite="www.apple.com/contact"
#     def contactDetales(self):
#         print("to contact us, log on to ",self.contactWebsite)
#
# class MacBook(Apple):
#     def __init__(self):
#         self.yearOfManufacturer=2007
#     def manufactureDetails(self):
#         print("this MacBook was manufactured in the year {} by {}".format(self.yearOfManufacturer,self.manufacturer))
#
# macBook=MacBook()
# macBook.manufactureDetails()
# print(macBook.yearOfManufacturer)
# print(macBook.manufacturer)
# print(macBook.contactWebsite)
# macBook.contactDetales()
# =====================multiple inheritance==============
# class Mother:
#     M_eyeColor="Blue"
#     M_complex="Chocolate"
#     def fight(self):
#         print("i can speak good english")
#     def intelligence(self):
#         print("i am intelligent")
#
# class Father:
#     F_eyeColor = "Black"
#     F_complex = "Light"
#     def outponken(self):
#         print("i am always quiet")
# class Son(Father,Mother):
#     s_height="tall"
#     def __init__(self,n):
#         self.name=n
#     def emotion(self):
#         print("my name is {}".format(self.name))
#         print("i am emotional")
# myson=Son("princewill")
# myson.emotion()
# print("i inherited {} eyes and, {} complexion from my father and  mother respectively ".format(myson.F_eyeColor,myson.M_complex))
# myson.fight()
# myson.intelligence()
# myson.outponken()
# ==========================multilevel inheritances===============================
# class GrandFather:
#     G_women=["Tonia","adanma","gina "," Alade"]
#     G_men = ["Tony", "popoola", "ify ", " Alake"]
#
#     def Gwomen(self):
#        self.addlist=[]
#        self.addlist.extend(self.G_women)
#        return self.addlist
#     def Gmen(self):
#         self.addlist = []
#         self.addlist.extend(self.G_men)
#         return self.addlist
#
#     def Gtotal(self):
#         self.joinlist=[]
#         self.joinlist.extend(self.Gwomen())
#         self.joinlist.extend(self.Gmen())
#         return self.joinlist
#
# class Father(GrandFather):
#     F_women = ["laide", "ada", "grace ", " Akudo"]
#     F_men = ["jude", "james", "john", " tanko"," mathew"]
#     def Ftotal(self):
#         self.joinlist=[]
#         self.joinlist.extend(self.F_women)
#         self.joinlist.extend(self.F_men)
#         return self.joinlist
#
# class Myself(Father):
#     S_women = ["lolo", "tatiana"]
#     S_men = ["long man", "silvester"]
#
#     def mY(self):
#         self.joinlist=self.S_women+self.S_men
#         return self.joinlist
# obj=Myself()
# print("my grand father has %s children, %s males and %s females"%(len(obj.Gtotal()),len(obj.G_men),len(obj.G_women)))
# print("my father has %s children, %s males and %s females"%(len(obj.Ftotal()),len(obj.F_men),len(obj.F_women)))
# print("my grand father has %s children, %s males and %s females"%(len(obj.mY()),len(obj.S_men),len(obj.S_women)))
# print("the total of the dynasty is %s"%(len(obj.Gtotal())+len(obj.Ftotal())+len(obj.mY())))
# women=len(obj.S_women)+len(obj.F_women)+len(obj.G_women)
# men=len(obj.S_men)+len(obj.F_men)+len(obj.G_men)
# print("that is, %s females and %s males"%(women,men))
# ====================================shopping cart=================================================================
def get_item():
    print("add to list: ")
    return input()

def go_shopping():
    cart=[]
    while True:
       t= get_item()
       if  t=="":
            break
       cart.append(t)
    print("list: ",end="")
    print(cart)
    print("finished")

go_shopping()






















