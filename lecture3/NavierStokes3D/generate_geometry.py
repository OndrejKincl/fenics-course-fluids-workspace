import gmsh
import meshio

radius1 = 0.15
radius2 = 0.119
len1 = 0.9
len2 = 0.4
conelen = 0.2
edgelen = 0.02

gmsh.initialize()
engine = gmsh.model.occ
cyl1 = engine.addCylinder(-len1, 0.0, 0.0, len1, 0.0, 0.0, radius1)
cyl2 = engine.addCylinder(conelen, 0.0, conelen, len2, 0.0, len2, radius2)
cyl3 = engine.addCylinder(conelen, 0.0, -conelen, len2, 0.0, -len2, radius2)
cone1 = engine.addCone(0.0, 0.0, 0.0, conelen, 0.0, conelen, radius1, radius2)
cone2 = engine.addCone(0.0, 0.0, 0.0, conelen, 0.0, -conelen, radius1, radius2)
fuse_dimtags = engine.fuse([(3, cyl1), (3,cyl2), (3, cyl3)], [(3, cone1), (3,cone2)], removeObject=True, removeTool=True)
gmsh.option.setNumber("Mesh.MeshSizeExtendFromBoundary", 0)
gmsh.option.setNumber("Mesh.MeshSizeMax", edgelen)
gmsh.option.setNumber("Mesh.MeshSizeMin", edgelen)
gmsh.option.setNumber("Mesh.Optimize", 1)
engine.synchronize()
gmsh.model.mesh.generate(3)
gmsh.write(f"bifurcation.msh")
gmsh.finalize()

# convert to xml
mesh = meshio.read("bifurcation.msh")
mesh.write("bifurcation.xml")