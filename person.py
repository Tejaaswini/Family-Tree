class Person:
    brothers = []
    sisters = []

    def __init__(self, name, sex, mother=None, father=None):
        self.name = name
        self.sex = sex
        self.mother = mother
        self.father = father
        self.sons = []
        self.daughters = []
        self.spouse = None
        self.generation = None

    def add_child(self, child):
        if child.sex == "M":
            self.sons.append(child)
        else:
            self.daughters.append(child)

    def add_spouse(self, spouse):
        self.spouse = spouse

    @staticmethod
    def get_brothers(person):
        if person is None:
            return []
        brothers_list = []
        if person.father:
            brothers_list = person.father.sons.copy()
            if person in brothers_list:
                brothers_list.remove(person)
        return brothers_list

    @staticmethod
    def get_sisters(person):
        if person is None:
            return []
        sisters_list = []
        if person.father:
            sisters_list = person.father.daughters.copy()
            if person in sisters_list:
                sisters_list.remove(person)
        return sisters_list

    @staticmethod
    def get_children(person):
        if person is None:
            return []
        return person.sons + person.daughters

    @staticmethod
    def get_grand_daughter(person):
        offsprings = person.sons + person.daughters
        grand_daughters = []
        for person in offsprings:
            grand_daughters.extend(person.daughters)
        return grand_daughters

    @staticmethod
    def get_grand_son(person):
        offsprings = person.sons + person.daughters
        grand_sons= []
        for person in offsprings:
            grand_sons.extend(person.sons)
        return grand_sons

    @staticmethod
    def get_mother(person):
        if person.mother:
            return [person.mother]
        return []

    @staticmethod
    def get_father(person):
        if person.father:
            return [person.father]
        return []

    @staticmethod
    def get_sons(person):
        return person.sons

    @staticmethod
    def get_daughters(person):
        return person.daughters