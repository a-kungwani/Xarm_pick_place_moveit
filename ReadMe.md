# xarm_pick_place_moveit
The Repository is a modified version of [xarm_ros2](https://github.com/xArm-Developer/xarm_ros2) to add a pick and place simulation of a cylinder object from one table to another table.

## 1. Preparation

- ### 1.1 Install [ROS2](https://docs.ros.org/) 
  - [Foxy](https://docs.ros.org/en/ros2_documentation/foxy/Installation.html)
  - [Galactic](https://docs.ros.org/en/ros2_documentation/galactic/Installation.html)
  - [Humble](https://docs.ros.org/en/ros2_documentation/humble/Installation.html)
  - [Jazzy](https://docs.ros.org/en/ros2_documentation/jazzy/Installation.html)

- ### 1.2 Install [Moveit2](https://moveit.ros.org/install-moveit2/binary/)  

- ### 1.3 Install [Gazebo](https://classic.gazebosim.org/tutorials?tut=install_ubuntu)  

## 2. How To Use

- ### 2.1 Create a workspace
    ```bash
    # Skip this step if you already have a target workspace
    $ cd ~
    $ mkdir -p dev_ws/src
    ```

- ### 2.2 Obtain source code of "xarm_ros2" repository
    ```bash
    # Remember to source ros2 environment settings first
    $ cd ~/dev_ws/src
    # DO NOT omit "--recursive"，or the source code of dependent submodule will not be downloaded.
    # Pay attention to the use of the -b parameter command branch, $ROS_DISTRO indicates the currently activated ROS version, if the ROS environment is not activated, you need to customize the specified branch (foxy/galactic/humble)
    $ git clone https://github.com/xArm-Developer/xarm_ros2.git --recursive -b $ROS_DISTRO
    ```

- ### 2.3 Update "xarm_ros2" repository 
    ```bash
    $ cd ~/dev_ws/src/xarm_ros2
    $ git pull
    $ git submodule sync
    $ git submodule update --init --remote
    ```

- ### 2.4 Install dependencies
    ```bash
    # Remember to source ros2 environment settings first
    $ cd ~/dev_ws/src/
    $ rosdep update
    $ rosdep install --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
    ```

- ### 2.5 Build xarm_ros2
    ```bash
    # Remember to source ros2 and moveit2 environment settings first
    $ cd ~/dev_ws/
    # build all packages
    $ colcon build
    
    # build selected packages
    $ colcon build --packages-select xarm_api
    ```
## 3 Execution
- ### 3.1 Executing launch file for Moveit + Gazebo
```bash
  $ ros2 launch xarm_moveit_config xarm6_moveit_gazebo.launch.py
```
- ### 3.2 Moveit Planning launch file
```bash
  $ ros2 launch xarm_moveit_config pp.launch.py
```
## 4 Acknowledgement

Developed using the [xarm_ros2](https://github.com/xArm-Developer/xarm_ros2) repository
