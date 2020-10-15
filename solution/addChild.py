import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree
from solution.relations import Relations

class AddChild:

    @staticmethod
    def add_child(family):
        parent_name = input("Enter Parent Name: ")
        options = ["Daughter", "Son"]
        for index, name in enumerate(options):
            print("Enter " + str(index) + " If you want to  " + name + ".")
        option_number = int(input("Your option : "))
        child_name = input("Enter "+options[option_number] + " name :")
        sex = "F" if option_number == 0 else "M"
        family.add_new_born(parent_name, child_name, sex)
        print("Child Added to parent " +parent_name)


if __name__ == "__main__":
    family = FamilyTree().construct()
    AddChild.add_child(family)