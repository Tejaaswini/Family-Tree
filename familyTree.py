from person import Person
from family import Family


class FamilyTree:
    @staticmethod
    def construct():
        king_shan = Person("King Shan", "M", None, None)
        king_shan.generation = 0
        queen_anga = Person("Queen Anga", "F", None, None)
        family = Family(king_shan)
        family.marriage_of_a_family_member(king_shan, queen_anga)
        new_members_list = [

            # gen1
            {"from_family": True, "name": "Ish",
                "sex": "M", "parent": "King Shan"},
            {"from_family": True, "name": "Chit",
                "sex": "M", "parent": "King Shan"},
            {"from_family": True, "name": "Vich",
                "sex": "M", "parent": "King Shan"},
            {"from_family": True, "name": "Satya",
                "sex": "F", "parent": "King Shan"},
            {"from_family": True, "name": "Aras",
                "sex": "M", "parent": "King Shan"},

            #################################################################

            # gen1-spouses
            {"from_family": False, "name": "Amba",
                "sex": "F", "partner_name": "Chit"},
            {"from_family": False, "name": "Lika",
                "sex": "F", "partner_name": "Vich"},
            {"from_family": False, "name": "Vyan",
                "sex": "M", "partner_name": "Satya"},
            {"from_family": False, "name": "Chitra",
                "sex": "F", "partner_name": "Aras"},

            #################################################################

            # gen2
            # parent-Chit
            {"from_family": True, "name": "Dritha",
                "sex": "F", "parent": "Chit"},
            {"from_family": True, "name": "Vritha",
                "sex": "M", "parent": "Chit"},
            {"from_family": True, "name": "Tritha",
                "sex": "F", "parent": "Chit"},

            # parent-Vich
            {"from_family": True, "name": "Vila",
                "sex": "F", "parent": "Vich"},
            {"from_family": True, "name": "Chika",
                "sex": "F", "parent": "Vich"},

            # Parent-Aras
            {"from_family": True, "name": "Jnki",
                "sex": "F", "parent": "Aras"},
            {"from_family": True, "name": "Ahit",
                "sex": "M", "parent": "Aras"},

            # parent-Satya
            {"from_family": True, "name": "Asva",
                "sex": "M", "parent": "Satya"},
            {"from_family": True, "name": "Vyas",
                "sex": "M", "parent": "Satya"},
            {"from_family": True, "name": "Atya",
                "sex": "F", "parent": "Satya"},

            #################################################################

            # gen2 - spouses
            {"from_family": False, "name": "Jaya",
                "sex": "M", "partner_name": "Dritha"},
            {"from_family": False, "name": "Arit",
                "sex": "M", "partner_name": "Jnki"},
            {"from_family": False, "name": "Satvy",
                "sex": "F", "partner_name": "Asva"},
            {"from_family": False, "name": "Krpi",
                "sex": "F", "partner_name": "Vyas"},

            #################################################################

            # gen3
            {"from_family": True, "name": "Yodhan",
                "sex": "M", "parent": "Dritha"},

            {"from_family": True, "name": "Laki",
                "sex": "M", "parent": "Jnki"},
            {"from_family": True, "name": "Lavnya",
                "sex": "F", "parent": "Jnki"},

            {"from_family": True, "name": "Vasa",
                "sex": "M", "parent": "Asva"},

            {"from_family": True, "name": "Kriya",
                "sex": "M", "parent": "Vyas"},
            {"from_family": True, "name": "Krithi",
                "sex": "F", "parent": "Vyas"}
        ]

        for new_person in new_members_list:
            if new_person["from_family"]:
                FamilyTree.add_person_to_family(family, new_person)
            else:
                FamilyTree.add_spouse_to_family_member(family, new_person)
        return family

    @staticmethod
    def add_person_to_family(family, person):
        family.add_new_born(person["parent"], person["name"], person["sex"])

    @staticmethod
    def add_spouse_to_family_member(family, spouse):
        member = family.find_member_by_name(spouse["partner_name"])
        spouse = Person(spouse['name'], spouse['sex'])
        family.marriage_of_a_family_member(member, spouse)
