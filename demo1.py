# -*- encoding: utf-8 -*-
from ase import Atoms
from ase.calculators.emt import EMT


def main():
    atom = Atoms('N')
    atom.calc = EMT()
    e_atom = atom.get_potential_energy()
    d = 1.1
    molecule = Atoms('2N', [(0, 0, 0), (0, 0, d)])
    molecule.calc = EMT()
    e_molecule = molecule.get_potential_energy()
    e_atomization = e_molecule - 2 * e_atom

    print('Nitrogen atom energy: %5.2f eV' % e_atom)
    print('Nitrogen molecule energy: %5.2f eV' % e_molecule)
    print('Atomization energy: %5.2f eV' % -e_atomization)


if __name__ == '__main__':
    main()
