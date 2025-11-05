# main2.py
# ===============================================
# The second/alternate main game loop
# ===============================================

import drone
import database
import static

#spread out randomly
while num_drones() <= static.max_available_drones:
    if drone.run(database.num_drone_spawned):
        print("START")

print("FINISH")
