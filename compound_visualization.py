from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit.Chem import rdDepictor

rdDepictor.SetPreferCoordGen(True)
import rdkit
print(rdkit.__version__)

mol = Chem.MolFromSmiles('c1(C=O)cc(OC)c(O)cc1')
Draw.MolToImage(mol, size=(500,500), kekulize=True)
Draw.ShowMol(mol, size=(500,500), kekulize=True)

Draw.MolToFile(mol, '论文/图片/compound1.png', size=(500, 500))