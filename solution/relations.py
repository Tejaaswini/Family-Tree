import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree
from family import Family
from person import Person

class Relations:
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
        get_members_in_relation = Relations.get_relation_function(relation_number)
        if relation_number in [3, 5]:
            members_in_relation = get_members_in_relation(person, person.father)
        elif relation_number in [4, 6]:
            members_in_relation = get_members_in_relation(person, person.mother)
        else:
            members_in_relation = get_members_in_relation(person)
        return members_in_relation

    @staticmethod
    def print_relatives_of_member(family):
        print("\n problem 1 :-")
        person_name = input("Person : ")
        for index, relation in enumerate(family.relation_list):
            print("Enter " + str(index) + " For " + relation + ".")
        relation_number = int(input("Choose Relation: "))
        members_in_relation = Relations.get_members_in_relation(family, relation_number, person_name)
        print(person_name + " " + family.relation_list[relation_number] + " :")
        print(", ".join([x.name for x in members_in_relation]))


if __name__ == "__main__":
    family = FamilyTree().construct()
    Relations.print_relatives_of_member(family)