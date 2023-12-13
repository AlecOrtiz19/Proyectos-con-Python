from anytree import Node, RenderTree


pablo = Node("Pablo")
pedro = Node("Pedro", parent=pablo)
ramon = Node("Ramon", parent=pablo)
carlos = Node("Carlos", parent=pedro)
pepe = Node("Pepe", parent=pedro)
anibal = Node("Aníbal", parent=ramon)
sandra = Node("Sandra", parent=ramon)
lady = Node("Lady", parent=carlos)
luis = Node("Luis", parent=carlos)
juan = Node("Juan", parent=sandra)
clara = Node("Clara", parent=pepe)
pamela = Node("Pamela", parent=pepe )
ines = Node("Ines", parent=anibal)


for pre, fill, node in RenderTree(pablo):
    print("%s%s" % (pre, node.name))

#RECORDAR TENER INSTALADA LA LIBRERIA ANYTREE
# PARA RELIZAR SU DESCARGA SE LO REALIZA DE LA SIGUIENTE MANERA pip install anytree en la consola

