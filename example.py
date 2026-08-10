import time
import cflib, cflib.crtp, cflib.crazyflie, cflib.utils.reset_estimator
import cflib.positioning.position_hl_commander

# Address of the drone. Change the xx below to reflect the tag underneath it.
URI = 'radio://0/80/2M/E7E7E7E7xx'

if __name__ == '__main__':
    # Initialize the Crazyradio low-level drivers
    cflib.crtp.init_drivers() 

    # Create the Crazyflie object
    cf = cflib.crazyflie.Crazyflie(rw_cache='./cache')

    # Connect to the drone at the URI
    cf.open_link(URI)

    # Reset the drone's state estimator 
    cflib.utils.reset_estimator.reset_estimator(cf)

    # Create the object used to send position commands to the drone
    with cflib.positioning.position_hl_commander.PositionHlCommander(cf) as cmd:
        # Hover for one second
        time.sleep(1)

        # Each go_to command will move to a given position relative to takeoff
        cmd.go_to(x=0.5, y=0.0, z=0.5, velocity=0.5)
        time.sleep(1)

        cmd.go_to(x=0.5, y=0.5, z=0.5, velocity=0.5)
        time.sleep(1)

        cmd.go_to(x=0.0, y=0.5, z=0.5, velocity=0.5)
        time.sleep(1)

        cmd.go_to(x=0.0, y=0.0, z=0.5, velocity=0.5)
        time.sleep(1)

        # Land the drone
        cmd.land(velocity=0.2)
    
    cf.close_link()
