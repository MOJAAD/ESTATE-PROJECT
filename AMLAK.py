#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                             IN THE NAME OG GOD                                                    #
#                                            PROJECT   OF  ESTATE                                                   #
#                                           CRAETED BY :    MOJAAD                                                  #
#                                             IN DATE: 2020/05/5                                                    #
#                                                                                                                   # 
#                                                                                                                   #
#################################################### MODULES ########################################################  
import pickle as pooryasays
import os as mostafasays
import time as hossein
import sys as amirmohammadsays
################################################# CLEAN CONSOLE #####################################################
def cls():
    mostafasays.system(['clear','cls'][mostafasays.name=='nt'])
#################################################### WAITNIG... #####################################################
def wait():
    cls()
    print("\t\t\t                 WAITING...               \n\t\t\t",end='')
    for counter in range(39):
        print("*",end='')
        hossein.sleep(0.03)
    print("*")    
############################################## FOR CHECKING FILES ################################################### 
admin_samieian="admin_samieian.txt"
amlak_samieian="amlak_samieian.txt"
findamlak=mostafasays.path.isfile(amlak_samieian)
findadmin=mostafasays.path.isfile(admin_samieian)
if findamlak==False :
    newfile=open(amlak_samieian,'x')
    newfile.close()
if findadmin==False :
    newfile=open(admin_samieian,'wb')
    admin=['behrouz','samiean','0134','admin']
    pooryasays.dump(admin,newfile)
    newfile.close()
################################################# DEFINE CLASSES #################################################### 
class estate:
    area=0
    address=''
    price=0
    description=''
    type_presentation=''

    def __init__(self,area,address,price,description='',type_presentation=''):
        self.area = area
        self.address = address
        self.price = price
        self.description = description
        self.type_presentation = type_presentation

    def __del__(self,area,address,price,description,type_presentation):
        self.area=0
        self.address=''
        self.price=0
        self.description=''
        self.type_presentation=''
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class farming(estate):
    water_period=0
    def __init__(self,area,address,price,description,type_presentation,water_period=0):
        estate.__init__(self,area,address,price,description,type_presentation)
        self.water_period = water_period

    def __del__(self,area,address,price,description,type_presentation,water_period):
        estate.__del__(self,area,adderss,price,description,type_presentation)
        self.water_period=0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class garden(farming):
    def __init__(self,area,address,price,description,type_presentation,water_period,type_garden='',wall=False,bower=False):
        farming.__init__(self,area,address,price,description,type_presentation,water_period)
        self.type_garden = type_garden
        self.wall = wall
        self.bower = bower

    def showclass():
        print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
        print("TYPE OF GARDEN : {}   WATER PERIOD : {}   WALL : {}   BOWER : {}".format(self.type_garden,self.water_period,self.wall,self.bower))
        print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
        print("DESCRIPTION : {}".format(self.description))
        print("___________________________________________________________________________________________")

    def __del__(area,address,price,description,type_presentation,water_period,type_garden,wall,bower):
        farming.__del__(area,adderss,price,description,type_presentation,water_period)
        self.type_garden = ''
        self.wall = False
        self.bower = False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class field(farming):
    def __init__(self,area,address,price,description,type_presentation,water_period,bower=False):
        farming.__init__(self,area,address,price,description,type_presentation,water_period)
        self.bower = bower

    def showclass():
        print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
        print("WATER PERIOD : {}   BOWER : {}".format(self.water_period,self.bower))
        print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
        print("DESCRIPTION : {}".format(self.description))
        print("___________________________________________________________________________________________")

    
    def __del__(area,address,price,description,type_presentation,water_period,bower):
        farming.__del__(self,area,adderss,price,description,type_presentation,water_period)
        self.bower = bower
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class building(estate):
    construction_year = 0
    def __init__(self,area,address,price,description,type_presentation,construction_year=0):
        estate.__init__(self,area,address,price,description,type_presentation)
        self.construction_year = construction_year

    def __del__(self,area,address,price,description,type_presentation,construction_year):
        estate.__del__(self,area,address,price,description,type_presentation)
        self.construction_year = 0
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class residential(building):
    def __init__(self,area,address,price,description,type_presentation,construction_year,residential_type,number_of_rooms,parking,des1,des2,des3):
        building.__init__(self,area,address,price,description,type_presentation,construction_year)
        self.residential_type = residential_type
        self.number_of_rooms = number_of_rooms
        self.parking = parking
        self.des1 = des1 #floor or yard
        self.des2 = des2 #unit or porch
        self.des3 = des3 #elevator or furnished

    def showclass():
        print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
        print("CONSTRUCTION YEAR : {}   RESIDENTIAL TYPE : {}   NUMBER OF ROOMS : {}".format(self.construction_year,self.residential_type,self.number_of_rooms))
        if residential_type=='APARTMENT':
            print("FLOOR : {}   UNIT : {}   ELEVATOR : {}".format(self.des1,self.des2,self.des3))
        elif residential_type=='HOUSE' or residential_type=='VILLA':
            print("YARD : {}   PORCH : {}   FURNISHED : {}".format(self.des1,self.des2,self.des3))    
        print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
        print("DESCRIPTION : {}".format(self.description))
        print("___________________________________________________________________________________________")


    def __del__(self,area,address,price,description,type_presentation,construction_year,residential_type,number_of_rooms,parking,des1,des2,des3):
        building.__del__(self,area,address,price,description,type_presentation,construction_year)
        self.number_of_rooms = 0
        self.parking = False
        self.residential_type = ''
        self.des1 = 0
        self.des2 = 0
        self.des3 = False
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
class commercial(building):
    def __init__(self,area,address,price,description,type_presentation,construction_year,commercial_type,des1=0,des2=0,des3=0,des4=0):
        building.__init__(self,area,address,price,description,type_presentation,construction_year)
        self.commercial_type = commercial_type
        self.des1 = des1 #number_of_rooms or
        self.des2 = des2 #Administrative document or
        self.des3 = des3 #                      or 
        self.des4 = des4 #                      or

    def showclass():
        print("AREA : {}   ADDRESS : {}   PRICE : {}".format(self.area,self.address,self.price))
        print("CONSTRUCTION YEAR : {}   COMMERCIAL TYPE : {}   ".format(self.construction_year,self.commercial_type))
        if commercial_type=='INDUSTRIAL':
            print("NUMBER OF ROOMS : {}   ADMINISTRATIVE DOCUMENT: {}".format(self.des1,self.des2))
        elif commercial_type=='OFFICE':
            print("FLOOR : {}   ELEVATOR : {}   STOREROOM : {}   NUMBER OF ROOMS : {}".format(self.des1,self.des2,self.des3,self.des4)) 
        elif commercial_type=='SHOP': 
            print("NUMBER OF ROOMS : {}   ADMINISTRATIVE DOCUMENT : {}".format(self.des1,self.des2))   
        print("TYPE OF PRESENTATION : {}".format(self.type_presentation))
        print("DESCRIPTION : {}".format(self.description))
        print("___________________________________________________________________________________________")

    
    def __del__(self,area,address,price,description,type_presentation,construction_year,commercial_type,des1,des2,des3,des4):
        building.__del__(self,area,address,price,description,type_presentation,construction_year)
        self.commercial_type=''
        self.des1 = 0
        self.des2 = 0 
        self.des3 = 0 
        self.des4 = 0 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# class official(building):
#     def __init__(self,area,address,price,description,type_presentation,construction_year,commercial_type,des1=0,des2=0,des3=0,des4=0):
#         building.__init__(self,area,address,price,description,type_presentation,construction_year)
#         self.des1 = des1 
#         self.des2 = des2 
#         self.des3 = des3 
#         self.des4 = des4 

#     def __del__(self,area,address,price,description,type_presentation,construction_year,commercial_type,des1,des2,des3,des4):
#         building.__del__(self,area,address,price,description,type_presentation,construction_year)
#         self.des1 = 0 
#         self.des2 = 0 
#         self.des3 = 0 
#         self.des4 = 0 
############################################### WELCOME ANIMATION ###################################################
def welcome_animation():
    cls()
    print("\n\n\n\n\n\t\t\t\t       *\n\n\n\n\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\n\n\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\n\n\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\n\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\n\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\n\t\t\t\t ****     ****\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\t\t\t\t ****     ****\n\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\t\t\t    ********       ********\n\t\t\t\t ****     ****\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\t\t\t\t ****     ****\n\t\t\t    ********       ********\n\n\n")
    hossein.sleep(0.8)
    cls()
    print("\n\t\t\t    ********       ********\n\t\t\t\t ****     ****\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t  *!WELCOME!*\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\t\t\t\t ****     ****\n\t\t\t    ********       ********\n\n\n")      
    hossein.sleep(1)
################################################# BYE ANIMATION #####################################################
def bye_animation():
    cls()
    print("\n\t\t\t    ********       ********\n\t\t\t\t ****     ****\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t    *!BYE!*\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\t\t\t\t ****     ****\n\t\t\t    ********       ********\n\n\n") 
    hossein.sleep(0.8)
    cls()
    print("\n\t\t\t    ********       ********\n\t\t\t\t ****     ****\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\t\t\t\t ****     ****\n\t\t\t    ********       ********\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\n\t\t\t\t ****     ****\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\t\t\t\t ****     ****\n\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\n\n\t\t\t\t    **   **\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\t\t\t\t    **   **\n\n\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\n\n\n\t\t\t\t      * *\n\t\t\t\t       *\n\t\t\t\t      * *\n\n\n\n\n\n")
    hossein.sleep(0.08)
    cls()
    print("\n\n\n\n\n\t\t\t\t       *\n\n\n\n\n\n\n")
    hossein.sleep(0.1)
    cls()
############################################### ADDING NEW ESTATE ###################################################
def ADD():
    flag1='0'
    flag2='0'
    while flag1=='0' and flag2=='0':
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|     PLEASE  ENTER SPECIFICATIONS:    |")
        try:
            area=int(input("\t\t\t|   1) AREA : "))
            address=str(input("\t\t\t|   2) ADDRESS : "))
            price=int(input("\t\t\t|   3) PRICE $ : "))
        except ValueError:
            cls()
            input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
            cls()
            continue
        while flag2=='0':
            print("\t\t\t|______________________________________|")
            print("\t\t\t|   WHAT IS YOUR ESTATE?(BY NUMBER:)   |")
            print("\t\t\t|   1) FARMING                         |")
            print("\t\t\t|   2) BUILDING                        |")
            selector=input("\t\t\t|   3) BACK TO MAIN MENU!              |")
            print("\t\t\t|______________________________________|")
            if selector=='1':
                print("\t\t\t|            GARDEN OR FIELD?          |")
                print("\t\t\t|   1) GARDEN                          |")
                print("\t\t\t|   2) FIELD                           |")
                inselector=input("\t\t\t|   3) BACK                            |")
                print("\t\t\t|______________________________________|")
                if inselector=='1':
                    while True:
                        print("\t\t\t|          ENTER INFORMATION:          |")
                        try:
                            water_period=int(input("\t\t\t|   1) WATER PERIOD(PER MONTH) :"))
                            type_garden=str(input("\t\t\t|   2) TYPE OF GARDEN :"))
                            wall=bool(input("\t\t\t|   3) HAVE WALL?( NO = ENTER ) :"))
                            bower=bool(input("\t\t\t|   4) HAVE BOWER? ( NO = ENTER ) :"))
                            description=str(input("\t\t\t|   5) DESCRIPTION:"))
                            print("\t\t\t|______________________________________|")
                            print("\t\t\t|     ENTER TYPE OF PRESENTATION :     |")
                            print("\t\t\t|   1) FOR BUY AND SELL :              |")
                            print("\t\t\t|   2) FOR MORTGAGE AND RENT :         |")
                            type_presentation=input("\t\t\t|______________________________________|")
                            if type_presentation=='1':
                                type_presentation='FOR BUY AND SELL'
                            elif type_presentation=='2':
                                type_presentation='FOR MORTGAGE AND RENT'
                            else:
                                type_presentation=int("kerm dari?")
                            wait()
                            garden1=garden(area,address,price,description,type_presentation,water_period,type_garden,wall,bower)
                            newfile=open(amlak_samieian,'ab')
                            pooryasays.dump(garden1,newfile)
                            newfile.close()
                            print("\t\t\t|            ESTATE CREATED!           |")
                            input("\t\t\t|____(press any key to continue...)____|")
                            cls()
                            flag2='1'
                            break
                        except ValueError:
                            cls()
                            input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                            cls()
                            continue
                elif inselector=='2':
                    while True:
                        print("\t\t\t|          ENTER INFORMATION:          |")
                        try:
                            water_period=int(input("\t\t\t|   1) WATER PERIOD(PER MONTH) :"))
                            bower=bool(input("\t\t\t|   2) HAVE BOWER?(True OR False) :"))
                            description=str(input("\t\t\t|   3) DESCRIPTION:"))
                            print("\t\t\t|______________________________________|")
                            print("\t\t\t|     ENTER TYPE OF PRESENTATION :     |")
                            print("\t\t\t|   1) FOR BUY AND SELL :              |")
                            print("\t\t\t|   2) FOR MORTGAGE AND RENT :         |")
                            type_presentation=input("\t\t\t|______________________________________|")
                            if type_presentation=='1':
                                type_presentation='FOR BUY AND SELL'
                            elif type_presentation=='2':
                                type_presentation='FOR MORTGAGE AND RENT'
                            else:
                                type_presentation=int("kerm dari?")
                            wait()
                            field1=field(area,address,price,description,type_presentation,water_period,bower)
                            newfile=open(amlak_samieian,'ab')
                            pooryasays.dump(field1,newfile)
                            newfile.close()
                            print("\t\t\t|            ESTATE CREATED!           |")
                            input("\t\t\t|____(press any key to continue...)____|")
                            cls()
                            flag2='1'
                            break
                        except ValueError:
                            cls()
                            input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                            cls()
                            continue
            elif selector=='2':
                print("\t\t\t|RESIDENTIAL OR COMMERCIAL OR OFFICIAL?|")
                print("\t\t\t|   1) RESIDETIAL                      |")
                print("\t\t\t|   2) COMMERCIAL                      |")
                inselector=input("\t\t\t|   3) BACK                            |")
                print("\t\t\t|______________________________________|")
                if inselector=='1':
                    while True:
                        print("\t\t\t|          ENTER INFORMATION:          |")
                        try:
                            residential_type=str(input("\t\t\t|   1) RESIDENTIAL TYPE(APARTMENT OR HOUSE OR VILLA) :"))
                            residential_type=residential_type.upper()
                            if residential_type=='APARTMENT' :
                                try:
                                    des1=int(input("\t\t\t|   2) FLOOR :"))
                                    des2=int(input("\t\t\t|   3) UNIT :"))
                                    des3=bool(input("\t\t\t|   4) ELEVATOR? ( NO = ENTER ) :"))
                                except ValueError:
                                    cls()
                                    input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                                    cls()
                                    continue
                            elif  residential_type=='HOUSE' or residential_type=='VILLA':
                                try:
                                    des1=bool(input("\t\t\t|   2) YARD? ( NO = ENTER ) :"))
                                    des2=bool(input("\t\t\t|   3) PORCH? ( NO = ENTER ) :"))
                                    des3=bool(input("\t\t\t|   4) FURNISHED? ( NO = ENTER ) :"))
                                except ValueError:
                                    cls()
                                    input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                                    cls()
                                    continue
                            else :
                                residential_type=int('kerm dari?')
                            construction_year=int(input("\t\t\t|   5) CONSTRUCTION YEAR :"))
                            number_of_rooms=int(input("\t\t\t|   6) NUMBER OF ROOMS :"))
                            parking=bool(input("\t\t\t|   7) HAVE PARKING? ( NO = ENTER ) :"))
                            description=str(input("\t\t\t|   8) DESCRIPTION:"))
                            print("\t\t\t|______________________________________|")
                            print("\t\t\t|     ENTER TYPE OF PRESENTATION :     |")
                            print("\t\t\t|   1) FOR BUY AND SELL :              |")
                            print("\t\t\t|   2) FOR MORTGAGE AND RENT :         |")
                            type_presentation=input("\t\t\t|______________________________________|")
                            if type_presentation=='1':
                                type_presentation='FOR BUY AND SELL'
                            elif type_presentation=='2':
                                type_presentation='FOR MORTGAGE AND RENT'
                            else:
                                type_presentation=int("kerm dari?")
                            wait()
                            residential1=residential(area,address,price,description,type_presentation,construction_year,residential_type,number_of_rooms,parking,des1,des2,des3)
                            newfile=open(amlak_samieian,'ab')
                            pooryasays.dump(residential1,newfile)
                            newfile.close()
                            print("\t\t\t|            ESTATE CREATED!           |")
                            input("\t\t\t|____(press any key to continue...)____|")
                            cls()
                            flag2='1'
                            break
                        except ValueError:
                            cls()
                            input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                            cls()
                            continue
                elif inselector=='2':
                    while True:
                        print("\t\t\t|          ENTER INFORMATION:          |")
                        try:
                            commercial_type=str(input("\t\t\t|   1) COMMERCIAL TYPE(INDUSTRIAL OR OFFICE OR SHOP) :"))
                            commercial_type=commercial_type.upper()
                            if commercial_type=='INDUSTRIAL' :
                                try:
                                    des1=int(input("\t\t\t|   2) NUMBER OF ROOMS :"))
                                    des2=bool(input("\t\t\t|   3) HAVE ADMINISTRATIVE DOCUMENT? ( NO = ENTER ) :"))
                                    des3=False
                                    des4=0
                                except ValueError:
                                    cls()
                                    input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                                    cls()
                                    continue
                            elif  commercial_type=='OFFICE' :
                                try:
                                    des1=int(input("\t\t\t|   2) FLOOR :"))
                                    des2=bool(input("\t\t\t|   3) HAVE ELEVATOR? ( NO = ENTER ) :"))
                                    des3=bool(input("\t\t\t|   4) HAVE STOREROOM? ( NO = ENTER ) :"))
                                    des4=int(input("\t\t\t|   5) NUMBER OF ROOMS :"))
                                except ValueError:
                                    cls()
                                    input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                                    cls()
                                    continue
                            elif commercial_type=='SHOP':
                                try:
                                    des1=int(input("\t\t\t|   2) NUMBER OF ROOMS :"))
                                    des2=bool(input("\t\t\t|   3) HAVE ADMINISTRATIVE DOCUMENT? ( NO = ENTER ):"))
                                    des3=False
                                    des4=0
                                except ValueError:
                                    cls()
                                    input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                                    cls()
                                    continue
                            else :
                                commercial_type=int('kerm dari?')
                            construction_year=int(input("\t\t\t|  -->) CONSTRUCTION YEAR :"))
                            description=str(input("\t\t\t|  -->) DESCRIPTION:"))
                            print("\t\t\t|______________________________________|")
                            print("\t\t\t|     ENTER TYPE OF PRESENTATION :     |")
                            print("\t\t\t|   1) FOR BUY AND SELL :              |")
                            print("\t\t\t|   2) FOR MORTGAGE AND RENT :         |")
                            type_presentation=input("\t\t\t|______________________________________|")
                            if type_presentation=='1':
                                type_presentation='FOR BUY AND SELL'
                            elif type_presentation=='2':
                                type_presentation='FOR MORTGAGE AND RENT'
                            else:
                                type_presentation=int("kerm dari?")
                            wait()
                            commercial1=commercial(area,address,price,description,type_presentation,construction_year,commercial_type,des1,des2,des3,des4)
                            newfile=open(amlak_samieian,'ab')
                            pooryasays.dump(commercial1,newfile)
                            newfile.close()
                            print("\t\t\t|            ESTATE CREATED!           |")
                            input("\t\t\t|____(press any key to continue...)____|")
                            cls()
                            flag2='1'
                            break
                        except ValueError:
                            cls()
                            input("\n\n\t\t\t\t   PLEASE ENTER CORRECTLY!")
                            cls()
                            continue
            elif selector=='3':
                flag1='1'
                break
################################################## EDIT ESTATE ######################################################

################################################# SEARCH ESTATE #####################################################
def SEARCH():
    flag0='0'
    while True:
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|              SEARCH BY :             |")
        print("\t\t\t|      PLEASE  SELECT BY NUMBER:       |")
        print("\t\t\t|   1) BY TYPE OF ESTATE               |")
        print("\t\t\t|   2) BY ADDRESS                      |")
        print("\t\t\t|   3) BY RANGE OF PRICE               |")
        print("\t\t\t|   4) ADVANCE                         |")
        selector=input("\t\t\t|   5) BACK                            |")
        if selector=='4':
            flag0='1'
        print("\t\t\t|______________________________________|")
        if selector=='1' or flag0=='1':    
            print("\t\t\t|   -->) CHOOSE TYPE OF ESTATE         |")
            print("\t\t\t|   1) FARMING                         |")
            print("\t\t\t|   2) BUILDING                        |")
            inselector=input("\t\t\t|   3) ADVANCE                         |")
            print("\t\t\t|______________________________________|")
            if inselector=='1':
                newfile=open(amlak_samieian,'rb')
                for line in newfile:
                    #farming1=pooryasays.load(newfile)
                    farming1=newfile.readline()
                    farming1=pooryasays.load(farming1)
                    if water_period in farming1 :
                    #if temp==True :
                        farming1.showclass() 
                print("\t\t\t\tpress any key to continue...")
                newfile.close()
            elif inselector=='2':
                temp=0
            elif inselector=='3':
                print("\t\t\t|   -->) CHOOSE TYPE OF ESTATE         |")
                print("\t\t\t|   1) GARDEN                          |")
                print("\t\t\t|   2) FIELD                           |")
                print("\t\t\t|   3) APARTMENT                       |")
                print("\t\t\t|   4) HOUSE                           |")
                print("\t\t\t|   5) VILLA                           |")
                print("\t\t\t|   6) INDUSTRIAL                      |")
                print("\t\t\t|   7) OFFICE                          |")
                print("\t\t\t|   8) SHOP                            |")
                ininselector=input("\t\t\t|   Other) BACK                        |")
                print("\t\t\t|______________________________________|")
                if ininselector=='1':
                    temp=0
                elif ininselector=='2':
                    temp=0
                elif ininselector=='3':
                    temp=0
                elif ininselector=='4':
                    temp=0
                elif ininselector=='5':
                    temp=0
                elif ininselector=='6':
                    temp=0
                elif ininselector=='7':
                    temp=0
                elif ininselector=='8':
                    temp=0
        if selector=='2' or flag0=='1':    
            inselector=input("\t\t\t|   -->)ENTER CITY OR ZONE :")
            print("\t\t\t|______________________________________|")

        if selector=='3' or flag0=='1':
                try:    
                    least=int(input("\t\t\t|   -->) ENTER LEAST PRICE :"))
                    most=int(input("\t\t\t|   -->) ENTER MOST PROCE : "))
                    print("\t\t\t|______________________________________|")
                    
                except ValueError:
                    cls()
                    input("\n\n\t\t\t\t    PLEASE ENTER CORRECTLY!")
        if selector=='4':
            temp=0
        elif selector=='5':
            break

################################################## SORT  ESTATE #####################################################

################################################### MAIN MENU #######################################################
welcome_animation()
while True:
    cls()
    print("\t\t\t ______________________________________")
    print("\t\t\t|             WELCOME USER!            |")
    print("\t\t\t|      PLEASE  SELECT BY NUMBER:       |")
    print("\t\t\t|   1) ADD NEW ESTATE                  |")
    print("\t\t\t|   2) SHOW ALL ESTATES (SORTED!)      |")
    print("\t\t\t|   3) EDIT ESTATE                     |")
    print("\t\t\t|   4) SEARCH ESTATE                   |")
    print("\t\t\t|   5) HELP!                           |")
    print("\t\t\t|   6) ABOUT US!                       |")
    print("\t\t\t|   7) EXIT!                           |")
    print("\t\t\t|______________________________________|")
    selector=input()
    if selector=='1' :
        ADD()
    elif selector=='2' :
        #SHOW()
        num=0
    elif selector=='3' :
        #EDIT()
        num=0
    elif selector=='4' :
        SEARCH()
    elif selector=='5' :
        cls()
        print("\t\t\t ______________________________________")
        print("\t\t\t|                                      |")
        print("\t\t\t|              DEAR USER !             |")
        print("\t\t\t|             I ADVISE YOU             |")
        print("\t\t\t|   EVERYTHING THAT YOU DON'T KNOW     |")
        print("\t\t\t|         SEARCH IN GOOGLE !!!         |")
        print("\t\t\t|______________________________________|")   
        hossein.sleep(2)
    elif selector=='6' :
            cls()
            print("\t\t\t ______________________________________ ")
            print("\t\t\t|             CREATED BY:              |")
            print("\t\t\t|               MOJAAD                 |")
            print("\t\t\t|        ELECTRONIC ENGINIEER          |")
            print("\t\t\t|        IN DATE : 2020/24/5           |")
            print("\t\t\t|                                      |")
            print("\t\t\t|      1) BACK TO MAIN MENU            |")
            print("\t\t\t|      2) EXIT FROM APP                |")
            print("\t\t\t|______________________________________|")
            us=input()
            if us=='2':
                cls()
                exit=input("\n\n\t\t\tARE YOU SURE?(YES or NO)\n")
                if exit.upper()=="YES" or exit.upper()=='Y' :
                    bye_animation()
                    amirmohammadsays.exit(0)
                elif exit.upper()=="NO" or exit.upper()=='N' :
                    pass
            else :
                pass        
    elif selector=='7' :
        cls()
        exit=input("\n\n\t\t\tARE YOU SURE?(YES or NO)\n")
        if exit.upper()=="YES" or exit.upper()=='Y' :
            bye_animation()
            amirmohammadsays.exit(0)
        elif exit.upper()=="NO" or exit.upper()=='N' :
            pass
        