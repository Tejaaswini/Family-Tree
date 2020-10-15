from person import Person

class Family:
    members = []
    relation_list = ["Brother(s)", "Sister(s)", "Cousin(s)", "Paternal Uncle(s)",
                     "Maternal Uncle(s)", "Paternal Aunt(s)", "Maternal Aunt(s)",
                     "Brother in law(s)", "Sister in law(s)", "Mother",
                     "Father", "Children", "Son", "Daughter", "Granddaughter", "Grandson"]

    def __init__(self, leader_man):
        self.leader_man = leader_man
        self.members.append(leader_man)

    def marriage_of_a_family_member(self, member, spouse):
        member.add_spouse(spouse)
        spouse.add_spouse(member)
        spouse.generation = member.generation
        self.add_member_in_family(spouse)

    def add_new_born(self, parent_name, child_name, sex):
        parent = self.find_member_by_name(parent_name)
        if parent is None:
            print("No person name " + parent_name)
        if parent.spouse is None:
            print("Single parent can't have children")
        if parent.sex == "M":
            child = Person(child_name, sex, mother=parent.spouse, father=parent)
            child.generation = parent.generation + 1
            Family.connect_new_born_to_parent(child, [parent, parent.spouse])
        else:
            child = Person(child_name, sex, mother=parent, father=parent.spouse)
            child.generation = parent.generation + 1
            Family.connect_new_born_to_parent(child, [parent, parent.spouse])
        self.add_member_in_family(child)

    @staticmethod
    def connect_new_born_to_parent(child, parents):
        if child.sex == "M":
            for parent in parents:
                parent.sons.append(child)
        else:
            for parent in parents:
                parent.daughters.append(child)

    def add_member_in_family(self, new_member):
        self.members.append(new_member)

    def find_member_by_name(self, name):
        for member in self.members:
            if member.name == name:
                return member
        return None

    @staticmethod
    def get_brother_in_laws(person):
        if person is None:
            return []
        brother_in_laws = []
        spouse_brothers = Person.get_brothers(person.spouse)
        brother_in_laws.extend(spouse_brothers)
        girl_siblings = Person.get_sisters(person)
        for girl in girl_siblings:
            if girl.spouse:
                brother_in_laws.append(girl.spouse)
        return brother_in_laws

    @staticmethod
    def get_sister_in_laws(person):
        if person is None:
            return []
        sister_in_laws = []
        spouse_sisters = Person.get_sisters(person.spouse)
        sister_in_laws.extend(spouse_sisters)
        boy_siblings = Person.get_brothers(person)
        for boy in boy_siblings:
            if boy.spouse:
                sister_in_laws.append(boy.spouse)
        return sister_in_laws

    @staticmethod
    def get_uncles(person, parent):
        if person is None:
            return []
        pUncles = []
        if parent and parent.father:
            parent_brothers = Person.get_brothers(parent)
            pUncles.extend(parent_brothers)
        parent_brother_in_laws = Family.get_brother_in_laws(parent)
        pUncles.extend(parent_brother_in_laws)
        return pUncles

    @staticmethod
    def get_aunt(person, parent):
        if person is None:
            return []
        aunts = []
        if parent and parent.father:
            sisters = Person.get_sisters(parent)
            aunts.extend(sisters)
        sister_in_laws = Family.get_sister_in_laws(parent)
        aunts.extend(sister_in_laws)
        return aunts

    @staticmethod
    def get_cousins(person):
        if person is None:
            return []
        mother = person.mother
        father = person.father
        cousins = []
        mother_sibling = Person.get_brothers(mother) + Person.get_sisters(mother)
        for sibling in mother_sibling:
            cousins.extend(Person.get_children(sibling))
        father_sibling = Person.get_brothers(father) + Person.get_sisters(father)
        for sibling in father_sibling:
            cousins.extend(Person.get_children(sibling))
        return cousins