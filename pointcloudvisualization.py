# -*- encoding: utf-8 -*-
import matplotlib.pyplot as plt
from ase.data.pubchem import pubchem_conformer_search
from sklearn.decomposition import PCA

colors = {1: (1,1,1), 6: (0.5,0.5,0.5), 7: (0,0,1), 8: (1,1,0), 16: (1,0,0)}


def gaussian():
    return


def smoothing(point):
    return


def draw(points: list):
    """
    draw 3-D picture using the positions of the molecule and the color of each atom
    :param points: a n*4 list, first three in an element present the position and the last presents the color
    """
    fig = plt.figure(facecolor='black')
    ax = fig.gca(projection='3d')
    x, y, z, c = [], [], [], []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
        z.append(points[i][2])
        c.append(points[i][3])
    ax.scatter(x, y, z, s=40, c=c)
    ax.set_axis_off()
    ax.patch.set_facecolor("#000000")
    plt.show()
    h = max(-min(x), -min(y), -min(z), max(x), max(y), max(z))
    print(h)


def main():
    try:
        compounds = pubchem_conformer_search(smiles='C=CC=C=CNO')
        for conformer in compounds:
            # print(conformer.data)
            atoms = conformer.atoms
            # print(points.symbols)
            # print(points.positions)
            # print(points.numbers)
            points = []
            for step, number in enumerate(atoms.numbers):
                point = list(atoms.positions[step]).copy()
                point.append(colors[number])
                points.append(point)
            # 平滑操作
            # smoothing(point)
            # print(points)
            draw(points)
    except ValueError as e:
        print(str(e))
        print('The compound is not found in PubChem!')


if __name__ == '__main__':
    main()
