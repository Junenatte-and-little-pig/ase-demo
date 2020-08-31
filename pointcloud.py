# -*- encoding: utf-8 -*-
from ase.data.pubchem import pubchem_atoms_conformer_search


def main():
    try:
        compounds = pubchem_atoms_conformer_search(cid='31525001')
        for conformer in compounds:
            print(conformer.symbols)
            print(conformer.positions)
            print(conformer.numbers)
            points = []
            for step, id in enumerate(conformer.numbers):
                point = {id: conformer.positions[step]}
                points.append(point)
            print(points)
    except ValueError:
        print('The compound is not found in PubChem!')


if __name__ == '__main__':
    main()
