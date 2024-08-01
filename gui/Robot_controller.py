import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *
from struct import *
import datetime

import rclpy as rp
from rclpy.node import Node
from robot_msgs.msg import GoalPose
from threading import Thread


positions = {
    "o": (0., 0., 0.),
    "Shelf1": (1.5546208449304282, -0.4596189342427643, -1.437230999624169),
    "Shelf2": (1.0402942456593676, -0.40828154538591077, -1.6386375833115416),
    "Shelf3": (0.4565105916649657, -0.3396688475363866, -1.5449646256794836),
    "Shelf4": (1.5976331803669466, 0.5327394950611359, -1.615602490631877),
    "Shelf5": (1.0402942456593676, 0.5327394950611359, -1.615602490631877),
    "Shelf6": (0.4565105916649657, 0.5327394950611359, -1.5449646256794836),
    "A1": (1.811784145, -0.4596189342427643, 0),
    "A2": (1.5546208449304282, -0.4596189342427643, 0),
    "A3": (1.297457545, -0.4596189342427643, 0),
    "A4": (1.0402942456593676, -0.40828154538591077, 0),
    "A5": (0.748402419, -0.40828154538591077, 0),
    "A6": (0.4565105916649657, -0.3396688475363866, 0),
    "A7": (0.228255296, -0.3396688475363866, 0),
    "B1": (1.811784145, 0.5327394950611359, 0),
    "B2": (1.5976331803669466, 0.5327394950611359, 0),
    "B3": (1.297457545, 0.5327394950611359, 0),
    "B4": (1.0402942456593676, 0.5327394950611359, 0),
    "B5": (0.748402419, 0.5327394950611359, 0),
    "B6": (0.4565105916649657, 0.5327394950611359, 0),
    "B7": (0.228255296, 0.5327394950611359, 0),
}


class GoalLauncher(Node):
    def __init__(self):
        super().__init__('gui_goal_publiser')
        self.goal_publisher = self.create_publisher(GoalPose, '/set_goal', 10)
    
    def publish_goal(self, key):
        msg = GoalPose()
        msg.move_flag = True
        msg.rotate_flag = True
        msg.x = positions[key][0]
        msg.y = positions[key][1]
        msg.theta = positions[key][2]

        self.goal_publisher.publish(msg)
        print(msg)

from_class = uic.loadUiType("/home/hj/ros-repo-1/gui/Robot_controller.ui")[0]

class WindowClass(QMainWindow, from_class) :
    def __init__(self, goal_publisher):
        super().__init__()
        self.setupUi(self)
        self.goal_publisher = goal_publisher

        self.Shelf1.clicked.connect(lambda: self.set_goal("Shelf1"))
        self.Shelf2.clicked.connect(lambda: self.set_goal("Shelf2"))
        self.Shelf3.clicked.connect(lambda: self.set_goal("Shelf3"))
        self.Shelf4.clicked.connect(lambda: self.set_goal("Shelf4"))
        self.Shelf5.clicked.connect(lambda: self.set_goal("Shelf5"))
        self.Shelf6.clicked.connect(lambda: self.set_goal("Shelf6"))

    def set_goal(self, key):
        self.goal_publisher.publish_goal(key)
        
    def __del__(self):
        self.sock.close()
        self.connected = False

def main(args=None):
    rp.init(args=args)
    goal_publisher = GoalLauncher()

    app = QApplication(sys.argv)
    myWindows = WindowClass(goal_publisher)
    myWindows.show()

    def spin():
        rp.spin(goal_publisher)

    spin_thread = Thread(target=spin)
    spin_thread.start()


    sys.exit(app.exec_())

    goal_publisher.destroy_node()
    rp.shutdown()



if __name__ == "__main__":
    main()
    
    
    
    