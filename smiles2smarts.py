import rdkit
from rdkit import Chem

s = '[NH2:1]-[C:2](=[O:3])-[c:4]1:[cH:5]:[cH:6]:[cH:7]:[n+:8](-[C@@H:10]2-[O:11]-[C@H:12](-[CH2:13]-[O:14]-[P:15](-[O:16])(=[O:17])-[O:18]-[P:19](-[O:20])(=[O:21])-[O:22]-[CH2:23]-[C@H:24]3-[O:25]-[C@@H:26](-[n:31]4:[cH:32]:[n:33]:[c:34]5:[c:35](-[NH2:36]):[n:37]:[cH:38]:[n:39]:[c:40]:4:5)-[C@H:27](-[OH:28])-[C@@H:29]-3-[OH:30])-[C@@H:41](-[OH:42])-[C@H:43]-2-[OH:44]):[cH:9]:1'

s = 'c1ccccc1'

print()
print(rdkit.__version__)
print(s)
m = Chem.MolFromSmiles(s)
sma = Chem.MolToSmarts(m, isomericSmiles=True)
# makes easier comparison to smiles by eye only - aromatic atoms are ignored
print(sma.replace('#6', 'C').replace('#8', 'O').replace('#15', 'P').replace('#7', 'N'))
#print(sma)
