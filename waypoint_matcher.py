import numpy as np

# Aから見たBを基に → Cから見たDの座標を求める
# [x, y, yaw]
A = np.array([-88.9282,-244.8,43.2632])
B = np.array([-88.1616,-241.2992,146.7907])

C = np.array([-229.781, 66.4963, 94.7945])
D = np.zeros(3)

A[2] = np.deg2rad(A[2])
B[2] = np.deg2rad(B[2])
C[2] = np.deg2rad(C[2])

delta_theta = C[2] - A[2]
cos_theta = np.cos(delta_theta)
sin_theta = np.sin(delta_theta)

dx = C[0] - (cos_theta * A[0] - sin_theta * A[1])
dy = C[1] - (sin_theta * A[0] + cos_theta * A[1])

D[2] = np.rad2deg(B[2] + delta_theta)
D[0] = cos_theta * B[0] - sin_theta * B[1] + dx
D[1] = sin_theta * B[0] + cos_theta * B[1] + dy

print(D)