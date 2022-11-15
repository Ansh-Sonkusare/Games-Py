import random
class Administrator:
    __slots__ = ("name" , "region" , "departments" , "languages" , "is_chief")

    def __init__(self , name, reg , dep:list , lang, is_chief=False) :
        self.departments = []
        self.languages = []

        self.name = name
        self.region = reg
        self.is_chief = is_chief

        for i in dep:
            self.departments.append(i)
        if(type(lang) == list):
            for i in lang:
                self.languages.append(i)
        else:
            self.languages.append(lang)
        
        # if(is_chief):
        #     self.name = "[Chief] " + self.name

class Council():
    __slots__ = ("Members" , "Chief")
    def __init__(self, membs) -> None:
        self.Members = []
        self.Chief = ""
 
        for i in membs:
            self.Members.append(i)
            if(i.is_chief and self.Chief == ""):
                self.Chief = i
        if(self.Chief == ""):
            idx = random.randint(0 , len(self.Members)-1)

            self.Members[idx].is_chief = True
            self.Chief = self.Members[idx]

def print_admin(admin:Administrator):
    
    name = "[Chief] " + admin.name if admin.is_chief else admin.name
    print(name)
    # region
    print("Region: " , admin.region)

    # department

    print("Departments:")
    for i in admin.departments:
        print("     " + i)
    
    # Languages
    print("Languages:")
    for i in admin.languages:
        print("     " + i)



def print_roster(counc:Council):
    print("Council:")
    for i in counc.Members:
        if(i.is_chief):
            print("[Chief] " + i.name)

        else:
            print(i.name)

    
def find_admin(counc:Council,deps:str):
    for i in counc.Members:
        if(deps in i.departments):
            print("Found Administrator Biography:")
            print_admin(i)

            
    return None


    
def find_chief(counc:Council ):
    for i in counc.Members:
        if(i.is_chief):
            print("Chief Administrator Biography:")

            print_admin(i)

            return i 
    return None
def print_full_bio_roster(Counc:Council):
    print("Council with Biographies:")
    for i in Counc.Members:
        print_admin(i)
        print()

    

def main():
    Nasqu = Administrator("Nasqu Baankai" , "Stakins" , ["Interplanetary Affairs", "Defense"] , ["Meinmese","Vietina"])
    Ittail = Administrator("Ittail Xaqe" , "Bhuhleks" , ["Finance","Transportation" , "Health Services"] , ["Meinmese","Geulmese"])
    Gregzuth = Administrator("Gregzuth Yehrins" , "Aalxo" , ["Resource Management"] , ["Meinmese" , "Geulmese"] )
    Drincaet = Administrator("Drincaet Drephral" , "Teehors" , ["Planetary Affairs","Agriculture"] ,[ "Mienmese " , "Ulbiya"])
    Thrilgiens = Administrator("Thrilgiens Vraurcaels" , "Stadu" , ["Education","Justice","Food Management"] ,["Tezniekani","Meinmese"])
    counc = Council([Nasqu , Ittail,Gregzuth,Drincaet , Thrilgiens])

    
main()