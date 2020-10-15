import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree
from family import Family
from person import Person

#Add child
class GeekTrust:
    @staticmethod
    def choose_choice(family):
        choices = ["Add Child", "Find All Relations", "Find Relationship"]
        for index, selctions in enumerate(choices):
            print("Enter " + str(index) + " If you want to  " + selctions + ".")
        choice_number = int(input("Your Choice : "))
        if choice_number == 0:
          selection = GeekTrust.add_child(family)
        elif  choice_number == 1:
            selection = GeekTrust.print_relatives_of_member(family)
        else:
            selection = GeekTrust.know_relationship(family)
        return selection

    @staticmethod
    def add_child(family):
        print("*****************************************************************")
        print("Add Child to family!")
        parent_name = input("Enter Parent Name: ")
        options = ["Daughter", "Son"]
        for index, name in enumerate(options):
            print("Enter " + str(index) + " If you want to  " + name + ".")
        option_number = int(input("Your option : "))
        child_name = input("Enter "+options[option_number] + " name :")
        sex = "F" if option_number == 0 else "M"
        family.add_new_born(parent_name, child_name, sex)
        print("Child Added to parent " +parent_name)
        print("*****************************************************************")

#Find Relations
    @staticmethod
    def get_relation_function(x):
        return {0: Person.get_brothers,
                1: Person.get_sisters,
                2: Family.get_cousins,
                3: Family.get_uncles,
                4: Family.get_uncles,
                5: Family.get_aunt,
                6: Family.get_aunt,
                7: Family.get_brother_in_laws,
                8: Family.get_sister_in_laws,
                9: Person.get_mother,
                10: Person.get_father,
                11: Person.get_children,
                12: Person.get_sons,
                13: Person.get_daughters,
                14: Person.get_grand_daughter,
                15: Person.get_grand_son,
                }[x]

    @staticmethod
    def get_members_in_relation(family, relation_number, name):
        person = family.find_member_by_name(name)
        get_members_in_relation = GeekTrust.get_relation_function(relation_number)
        if relation_number in [3, 5]:
            members_in_relation = get_members_in_relation(person, person.father)
        elif relation_number in [4, 6]:
            members_in_relation = get_members_in_relation(person, person.mother)
        else:
            members_in_relation = get_members_in_relation(person)
        return members_in_relation

    @staticmethod
    def print_relatives_of_member(family):
        print("*****************************************************************")
        print("Find out all the Relatives!")
        person_name = input("Person : ")
        for index, relation in enumerate(family.relation_list):
            print("Enter " + str(index) + " For " + relation + ".")
        relation_number = int(input("Choose Relation: "))
        members_in_relation = GeekTrust.get_members_in_relation(family, relation_number, person_name)
        print(person_name + " " + family.relation_list[relation_number] + " :")
        print(", ".join([x.name for x in members_in_relation]))
        print("*****************************************************************")

#Find Relationship between two specific people
    @staticmethod
    def get_relation_between_two(family, person, relative):
        if person.generation == relative.generation:
            sister_list = family.get_sisters(person)
            if relative in sister_list:
                return "Sister"
            brother_list = family.get_brothers(person)
            if relative in brother_list:
                return "Brother"
            cousin_list = family.get_cousins(person)
            if relative in cousin_list:
                return "Cousin"
            sister_in_law_list = family.get_sister_in_laws(person)
            if relative in sister_in_law_list:
                return "Sister-in-law"
            brother_in_law_list = family.get_brother_in_laws(person)
            if relative in brother_in_law_list:
                return "Brother-in-law"
            if relative.spouse == person:
                return "Spouse"
        if person.generation > relative.generation:
            if person.father == relative:
                return "Father"
            if person.mother == relative:
                return "Mother"
            if relative in family.get_uncles(person, person.father):
                return "Paternal Uncle"
            if relative in family.get_aunt(person, person.father):
                return "Paternal Aunt"
            if relative in family.get_uncles(person, person.mother):
                return "Maternal Uncle"
            if relative in family.get_aunt(person, person.mother):
                return "Maternal Aunt"
            if person in family.get_grand_daughter(relative):
                return "Grand Father"
            if person in family.get_grand_son(relative):
                return "Grand Father"
        if person.generation < relative.generation:
            if relative.father == person or relative.mother == person:
                if relative.sex == "M":
                    return "Son"
                else:
                    return "Daughter"
            uncle_aunt_list = family.get_uncles(relative, relative.father) + family.get_aunt(relative, relative.father) + \
                              family.get_uncles(relative, relative.mother) + family.get_aunt(relative, relative.mother)
            if person in uncle_aunt_list:
                if relative.sex == "M":
                    return "Nephew"
                else:
                    return "Niece"
            if relative in family.get_grand_daughter(person):
                return "Grand Daughter"
            if relative in family.get_grand_son(person):
                return "Grand Son"

    @staticmethod
    def know_relationship(family):
        print("*****************************************************************")
        print("Know the relationship between two Specific People!")
        person_name = input("Person Name: ")
        relative_name = input("Relative Name: ")
        person = family.find_member_by_name(person_name)
        relative = family.find_member_by_name(relative_name)
        print(GeekTrust.get_relation_between_two(family, person, relative))
        print("*****************************************************************")


if __name__ == "__main__":
    family = FamilyTree().construct()
    GeekTrust.choose_choice(family)