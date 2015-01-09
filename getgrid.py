import pybel
import numpy as np
def getgrid(coord):
    """Find grid center and size on the basis of co-crystallized ligand coordinates"""
    xyz = np.asarray(coord)
    center_x = round(xyz[:,0].mean(),2)
    center_y = round(xyz[:,1].mean(),2)
    center_z = round(xyz[:,2].mean(),2)
    size_x = round(xyz[:,0].max()-xyz[:,0].min())
    size_y = round(xyz[:,1].max()-xyz[:,1].min())
    size_z = round(xyz[:,2].max()-xyz[:,2].min())
    return center_x, center_y, center_z, size_x, size_y, size_z
    
if __name__ == "__main__":
    crystal = next(pybel.readfile("pdbqt", "dockingIN/1ddg-ligand.pdbqt"))
    xtalcoords = [atom.coords for atom in crystal]
    print getgrid(xtalcoords)
