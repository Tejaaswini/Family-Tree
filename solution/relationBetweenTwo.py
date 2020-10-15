import sys
sys.path.insert(0, "../")
from familyTree import FamilyTree

class RelationBetweenTwo:

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
        person_name = input("Person Name: ")
        relative_name = input("Relative Name: ")
        person = family.find_member_by_name(person_name)
        relative = family.find_member_by_name(relative_name)
        print(RelationBetweenTwo.get_relation_between_two(family, person, relative))


if __name__ == "__main__":
    family = FamilyTree.construct()
    RelationBetweenTwo.know_relationship(family)