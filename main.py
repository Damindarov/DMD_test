import open3d as o3d
import numpy as np
ply_point_cloud = o3d.data.PLYPointCloud()

num_points = 1000
points = np.random.rand(num_points, 3)

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_plotly([pcd])