# -*- encoding: utf-8 -*-
import numpy as np
from mayavi import mlab
from mayavi.mlab import points3d


def test_molecule():
    """Generates and shows a Caffeine molecule."""
    o = [[30, 62, 19], [8, 21, 10]]
    ox, oy, oz = list(map(np.array, zip(*o)))
    n = [[31, 21, 11], [18, 42, 14], [55, 46, 17], [56, 25, 13]]
    nx, ny, nz = list(map(np.array, zip(*n)))
    c = [[5, 49, 15], [30, 50, 16], [42, 42, 15], [43, 29, 13], [18, 28, 12],
         [32, 6, 8], [63, 36, 15], [59, 60, 20]]
    cx, cy, cz = list(map(np.array, zip(*c)))
    h = [[23, 5, 7], [32, 0, 16], [37, 5, 0], [73, 36, 16], [69, 60, 20],
         [54, 62, 28], [57, 66, 12], [6, 59, 16], [1, 44, 22], [0, 49, 6]]
    hx, hy, hz = list(map(np.array, zip(*h)))

    oxygen = points3d(ox, oy, oz, scale_factor=16, scale_mode='none',
                                resolution=20, color=(1, 0, 0), name='Oxygen')
    nitrogen = points3d(nx, ny, nz, scale_factor=20, scale_mode='none',
                                resolution=20, color=(0, 0, 1),
                                name='Nitrogen')
    carbon = points3d(cx, cy, cz, scale_factor=20, scale_mode='none',
                                resolution=20, color=(0, 1, 0), name='Carbon')
    hydrogen = points3d(hx, hy, hz, scale_factor=10, scale_mode='none',
                                resolution=20, color=(1, 1, 1),
                                name='Hydrogen')

    # return oxygen, nitrogen, carbon, hydrogen



if __name__ == '__main__':
    test_molecule()
    mlab.show()
