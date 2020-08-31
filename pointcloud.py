# -*- encoding: utf-8 -*-
from ase.data.pubchem import pubchem_conformer_search


def main():
    try:
        compounds = pubchem_conformer_search(cid=31525001)
        for conformer in compounds:
            # print(conformer.data)
            atoms = conformer.atoms
            print(atoms.symbols)
            print(atoms.positions)
            print(atoms.numbers)
            points = []
            for step, number in enumerate(atoms.numbers):
                point = {number: atoms.positions[step]}
                points.append(point)
            print(points)
    except ValueError:
        print('The compound is not found in PubChem!')


if __name__ == '__main__':
    main()
