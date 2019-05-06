class Proposition:
    pass


class Atom(Proposition):
    _instance = {}

    def __init__(self, index):
        self._index = index

    def __new__(cls, index):
        if index not in cls._instance:
            cls._instance[index] = super().__new__(cls)
        return cls._instance[index]

    @property
    def index(self):
        return self._index

    def __str__(self):
        return f'P_{self._index}'


class UnaryProposition(Proposition):
    def __init__(self, sub_prop: Proposition):
        self._sub_prop = sub_prop

    @property
    def sub_prop(self):
        return self._sub_prop


class ConditionalProposition(Proposition):
    def __init__(self, sub_prop1: Proposition, sub_prop2: Proposition):
        self._sub_prop1 = sub_prop1
        self._sub_prop2 = sub_prop2

    @property
    def sub_prop1(self):
        return self._sub_prop1

    @property
    def sub_prop2(self):
        return self._sub_prop2


class Negation(UnaryProposition):
    def __str__(self):
        return f'￢({self.sub_prop})'


class Conjunction(ConditionalProposition):
    def __str__(self):
        return f'({self.sub_prop1})∧({self.sub_prop2})'


class Disjunction(ConditionalProposition):
    def __str__(self):
        return f'({self.sub_prop1})∨({self.sub_prop2})'


class Implication(ConditionalProposition):
    def __str__(self):
        return f'({self.sub_prop1})→({self.sub_prop2})'


class Equivalence(ConditionalProposition):
    def __str__(self):
        return f'({self.sub_prop1})↔({self.sub_prop2})'
