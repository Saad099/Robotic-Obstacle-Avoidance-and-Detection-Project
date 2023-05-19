from controller import Robot, Camera

SPEED = 5.5
TIME_STEP = 64

# Initialize the robot
robot = Robot()

# Enable the camera and recognition
camera = robot.getDevice("camera")
camera.enable(TIME_STEP)
camera.recognitionEnable(TIME_STEP)




# Get the motor devices
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Flag to indicate if the robot is currently moving anywhere
move_anywhere = False

while robot.step(TIME_STEP) != -1:
    #object recoganized 
    number_of_objects = camera.getRecognitionNumberOfObjects()
    print("\nRecognized", number_of_objects, "objects.")

    #display the object detail
    objects = camera.getRecognitionObjects()
    for i in range(number_of_objects):
        print("Model of object", i, ":", objects[i].model)
        print("Id of object", i, ":", objects[i].id)
        print("Relative position of object", i, ":", objects[i].position)

        if objects[i].position[0] < 0.30 or objects[i].position[1] < 0.30:
            # Move the robot anywhere
            left_motor.setVelocity(-SPEED/ 2)
            right_motor.setVelocity(SPEED)
        else:      
                left_motor.setVelocity(SPEED)
                right_motor.setVelocity(SPEED)
           

        print("Relative orientation of object", i, ":", objects[i].orientation)
        print("Size of object", i, ":", objects[i].size)
        print("Position of the object", i, "on the camera image:", objects[i].position_on_image)
        print("Size of the object", i, "on the camera image:", objects[i].size_on_image)

        for j in range(objects[i].number_of_colors):
            color_index = j * 3
            print("- Color", j + 1, "/", objects[i].number_of_colors, ":", objects[i].colors[color_index : color_index + 3])
