
from csp import Constraint, CSP
from typing import Dict, List, Optional


class MapColoringConstraint(Constraint[str, str]):
    def __init__(self, place1: str, place2: str) -> None:
        super().__init__([place1, place2])
        self.place1: str = place1
        self.place2: str = place2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either place is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        # check the color assigned to place1 is not the same as the
        # color assigned to place2
        return assignment[self.place1] != assignment[self.place2]


if __name__ == "__main__":
    variables: List[str] = ["Ciudad de Mexico", "Monterrey", "Pachuca",
                            "Quintana Roo", "Nayarit", "Veracruz", "Sinaloa"]
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ["rojo", "verde", "azul"]
    csp: CSP[str, str] = CSP(variables, domains)
    csp.add_constraint(MapColoringConstraint("Ciudad de Mexico", "Monterrey"))
    csp.add_constraint(MapColoringConstraint("Ciudad de Mexico", "Pachuca"))
    csp.add_constraint(MapColoringConstraint("Pachuca", "Monterrey"))
    csp.add_constraint(MapColoringConstraint("Quintana Roo", "Monterrey"))
    csp.add_constraint(MapColoringConstraint("Quintana Roo", "Pachuca"))
    csp.add_constraint(MapColoringConstraint("Quintana Roo", "Nayarit"))
    csp.add_constraint(MapColoringConstraint("Nayarit", "Pachuca"))
    csp.add_constraint(MapColoringConstraint("Veracruz", "Pachuca"))
    csp.add_constraint(MapColoringConstraint("Veracruz", "Nayarit"))
    csp.add_constraint(MapColoringConstraint("Veracruz", "Sinaloa"))
    solution: Optional[Dict[str, str]] = csp.backtracking_search()
    if solution is None:
        print("No se encontro una solucion!")
    else:
        print(solution)