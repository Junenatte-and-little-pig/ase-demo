# -*- encoding: utf-8 -*-
from ase import Atoms
from ase.calculators.emt import EMT


def main():
    n=Atoms('N')
    n.calc=EMT()
    e_n=n.get_potential_energy()
    mo=Atoms('N2')
    mo.calc=EMT()
    e_min=2*e_n
    d_final=0
    for d in range(1,10000):
        mo.positions[1]=[0,0,d/100]
        e_mo=mo.get_potential_energy()
        if e_mo<e_min:
            e_min=e_mo
            d_final=d/100
    print(mo.cell)
    print(mo.numbers)
    print(mo.positions)
    print(e_min)
    print(d_final)


if __name__ == '__main__':
    main()
