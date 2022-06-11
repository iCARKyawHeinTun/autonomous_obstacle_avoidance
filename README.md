# autonomous_obstacle_avoidance
ROS / Python / MoveBase 

--> change to your catkin source directory <--

cd catkin_ws/src  

<br/>

--> download the code <--

git clone https://github.com/iCARKyawHeinTun/autonomous_obstacle_avoidance.git

--> compile your code <--

cd ..

catkin_make

--> source your work environment <--

source devel/setup.bash

--> launch the turtlebot3_gazebo standard world <--

roslaunch turtlebot3_gazebo turtlebot3_world.launch

--> open up second terminal,move to your catkin_ws, source the environment <--

cd catkin_ws

source devel/setup.bash

--> launch navigation_stack <--

roslaunch turtlebot3_navigation turtlebot3_navigation.launch

!! Define the approximate position of the turtlebot in RViz using 2D Pose Estimate !!

--> open up third terminal, move to your catkin_ws, source the environment <--

cd catkin_ws

source devel/setup.bash

--> launch the MoveBase python file <--

roslaunch autonomous_obstacle_avoidance my_launch.launch

# OR
--> if you can promptly define the position of the turtlebot in RViz, launch all the nodes at once <--

roslaunch autonomous_obstacle_avoidance my_launch_all.launch
