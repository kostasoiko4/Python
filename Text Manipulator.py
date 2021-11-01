class switch(object):
    value = None
    def __new__(class_, value):
        class_.value = value
        return True

def case(*args):
    return any((arg == switch.value for arg in args))

s1 = ""

def validInput(s1):
    if s1.isspace() or s1 == "":
        return False
    else:
        return True
    

x = 0

while (x != 4):
 print("1. Πληκτολογήστε το κείμενο σας: ")
 print("2. Μέτρα πεζά και κεφαλαία: ")
 print("3. Αντίστρεψε τα γράμματα: ")
 print("4. Έξοδος")

 x = int(input("**Πηκτρολογήστε εναν ακεραιο αριθμό απο το 1 - 4**"))

 while switch(x):
     if case(1):
        s1 = str(input("Γράψτε το κείμενο σας: "))
        l1 = len(s1)
        while (not validInput(s1)):
         s1 = input
         ("**Πρέπει να υπάρχει τουλάχιστον ένας μη-κενός χαρακτήρας**")
        print("**Το κείμενο αποθηκεύτηκε**")
        break
     if case(2):
        if s1.isspace() or s1 == "":
         print("Δεν υπάρχει κάποιο κείμενο")
        else:
         l1 = len(s1)
         l2 = 0
         l3 = 0
         while l1 > 0:
          if s1[l1-1].islower():
           l2 = l2 + 1
          elif s1[l1-1].isupper():
           l3 = l3 + 1
          l1 = l1 - 1
         print("Μικρά: ", l2)
         print("Κεφαλαία: ", l3)
        break
     if case(3):
        if s1.isspace() or s1 == "":
         print("Δεν υπάρχει κάποιο κείμενο")
        else:
         l1 = len(s1)
         while l1 > 0:
          print(s1[l1-1],end ='');
          l1-=1;
         print("\n **Το κείμενο σας ανάποδα**")
        break
     if case(4):
        print("Έξοδος!")
        break
     break