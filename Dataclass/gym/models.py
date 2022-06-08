from dataclasses import dataclass, field
from typing import List, Iterable

def calc_bmi(height: float, weight: float) -> float:
    return round(weight/(height/100)**2, 2)

@dataclass
class Lifter:
    age: int
    bmi: float = field(default=None)
    height: float = field(default=170.0, metadata={'units': 'cm'})
    weight: float = field(default=80.0, metadata={'units': 'Kg'})
    # fitness: float = field(default_factory=)   potential field like an elo?

    def __post_init__(self):
        self.bmi = calc_bmi(self.height, self.weight)


print(calc_bmi(165, 60))
jason = Lifter(age=19, height=165, weight=60)
print(jason)