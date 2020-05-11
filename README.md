# ME477_ROS
Robotics with ROS mini-course for ME 477.

## INTRO
The packages included in this repository serve simply to provide some experience and familiarity with some underlying topics and concepts needed for future study and experience in using the ROS framework. This will eventually allow for the use of more advanced concepts and implementation, with the end goal of simluating robotic systems. These packages are of beginner level and are meant to provide experience in the concepts of nodes, the "big Other" roscore, ROS packages, workspaces, publishing/subscribing, services, and actions. Additionally, these packages provide some early familiarity in object-oriented-programming (OOP) with Python and in some of the command-line functions of the ROS framework.

Such frameworks are invaluable to developing robotics as it provides simulation capabilities for variables devices and systems and, in the case of ROS, is quite effective and convenient in its modularity.

## REQUIREMENTS
This reposotory and its constituent packages were made using the Ubuntu Linux OS (version Bionic 18.04.4) with optional use of a virtual machine to create an instance of the OS on another (This repository was made using VirtualBox 6.1 + Extension Pack to run Ubuntu)

As for the ROS framework, ROS Melodic Morena was used (recent version). To write the ROS code, the Python language was used, but not using the installation that come with Ubuntu.

Optionally, for editing text files and code, the Jupyter IDE may be used or Sublime Text.

## INSTALLATION

An installation procedure for the requirements mentioned above may be found here: http://ricopic.one/robotics/robotics_partial.pdf (Resource 1 link in the ToC).

To copy this repository locally, use the 'Fork' button in GitHub and in a terminal window, type: git clone [forked repo URL here w/o brackets]

## GETTING STARTED
A user should begin using the packages included in this repository by starting with my_topics. Already you might familiarize your self with nagigating filepaths and use of cd and ls, and some ros functions such as roslaunch, rosrun, roscd, and rosls (the last two of which are similar to regular cd and ls, but specific to ROS).

To run the .py files used for the topics packages, one would type within a terminal:

(AFTER ENTERING catkin_make AND source devel/setup.bash IN THE CONSOLE FIRST)

roslaunch my_topics fancy_topics.launch

## USAGE
To use the other two packages, a similar command-line entry to that shown previously can be used:

roslaunch package_name(my_topics, my_services, etc.) launch_file (fancy_topic, fancy_service)

Since all launch files start a roscore, in order to end them, press ctrl-C.

For the first and last of these packages (topics and actions), their launch files can simply be executed and they will run. The second package (services), however, requires an additional argument to function. The part of the command is similar to the other two and is as follows:

roslaunch my_services fancy_service.launch

At the end of this line (before executing) a user would put in the following:

text:="SOME SENTENCE HERE"

This package will then return the number of words input to the "text" argument.

The other two packages, topics and actions, will do the following, respectively: print random numbers and assign them to variables Real and Imaginary until stopped, and will start a time which lasts for 5 seconds, printing values of time elapsed and time remaining about every second.