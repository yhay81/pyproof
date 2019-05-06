from typing import List
from propositions import Proposition, Implication


class Proof:
    def __init__(self, premises: List[Proposition], conclusion: Proposition):
        self._premises = premises
        self._conclusion = conclusion

    @property
    def premises(self):
        return self._premises

    @property
    def conclusion(self):
        return self._conclusion


class Premise(Proof):
    def __init__(self, prop: Proposition):
        super().__init__([prop], prop)
        self.sub = prop


class ImplicationElimination(Proof):
    def __init__(self, pr1: Proof, pr2: Proof):
        conclusion: Implication = pr2.conclusion
        if pr1.conclusion != conclusion.sub_prop1:
            raise TypeError
        premises = []
        gather_unique_obj(premises, pr1.premises)
        gather_unique_obj(premises, pr2.premises)
        super().__init__(premises, conclusion.sub_prop2)
        self.sub1 = pr1
        self.sub2 = pr2


def gather_unique_obj(outs, ins):
    for i in range(len(ins)):
        for j in range(len(outs)):
            if ins[i] == outs[j]:
                break
        else:
            outs.append(ins[i])
