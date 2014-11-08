class Solid:
	def __init__(self):
		self.triangles = []
	def addCubeWithDimensions(self,x,y,z,width,height,depth):
		bottomTriangles = [[(0,0,0), (0,1,0), (1,0,0)], [(1,1,0), (0,1,0), (1,0,0)]]
		topTriangles    = [[(0,0,1), (0,1,1), (1,0,1)], [(1,1,1), (0,1,1), (1,0,1)]]

		leftTriangles   = [[(0,0,0), (0,0,1), (1,0,0)], [(1,0,0), (1,0,1), (0,0,1)]]
		rightTriangles  = [[(0,1,0), (0,1,1), (1,1,0)], [(1,1,0), (1,1,1), (0,1,1)]]

		frontTriangles  = [[(0,0,0), (0,0,1), (0,1,0)], [(0,0,1), (0,1,0), (0,1,1)]]
		backTriangles   = [[(1,0,0), (1,0,1), (1,1,0)], [(1,0,1), (1,1,0), (1,1,1)]]

		cubeTriangles = bottomTriangles + topTriangles + leftTriangles + rightTriangles + frontTriangles + backTriangles
		lines = []
		for triangle in cubeTriangles:
			translatedAndScaledTriangle = []
			for coordinates in triangle:

				triX, triY, triZ = coordinates;
				triX = x + triX * width
				triY = y + triY * height
				triZ = z + triZ * depth
				translatedAndScaledTriangle.append((triX,triY,triZ))

			self.triangles.append(translatedAndScaledTriangle)
	def string(self):
		lines = ["solid object"] 
		for triangle in self.triangles:
			lines.append("  facet normal 0.000000e+000 0.000000e+000 0.000000e+000")
			lines.append("    outer loop")
			lines.append("      vertex %e %e %e" % triangle[0])
			lines.append("      vertex %e %e %e" % triangle[1])
			lines.append("      vertex %e %e %e" % triangle[2])
			lines.append("    endloop")
			lines.append("  endfacet")

		lines.append("endsolid")
		return "\n".join(lines)
