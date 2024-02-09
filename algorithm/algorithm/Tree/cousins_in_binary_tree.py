import time
import tkinter as tk
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.finial_color = None


class SolutionVisualization:
    def __init__(self, root, x, y):
        self.root = root
        self.x = x
        self.y = y
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()
        self.node_radius = 20
        self.level_height = 80
        self.node_positions = {}  # Store positions of visited nodes
        self.animation_speed = 1

    def draw_tree(self, node, x, y, level):
        if node:
            self.node_positions[node.val] = (x, y)  # Store position of current node
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    fill="white", outline="black")
            self.canvas.create_text(x, y, text=str(node.val))
            if node.left:
                self.draw_tree(node.left, x - 100, y + self.level_height, level + 1)
                self.canvas.create_line(x, y + self.node_radius, x - 100, y + self.level_height - self.node_radius,
                                        width=2)
            if node.right:
                self.draw_tree(node.right, x + 100, y + self.level_height, level + 1)
                self.canvas.create_line(x, y + self.node_radius, x + 100, y + self.level_height - self.node_radius,
                                        width=2)

    def highlight_node(self, node, color):
        if color is None:
            return  # Skip highlighting if color is not provided
        x, y = self.node_positions[node.val]
        self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                x + self.node_radius, y + self.node_radius,
                                outline=color, width=2)
        self.window.update()
        time.sleep(self.animation_speed)
        if node.finial_color:
            self.canvas.create_oval(x - self.node_radius, y - self.node_radius,
                                    x + self.node_radius, y + self.node_radius,
                                    outline=node.finial_color, width=2)
            self.window.update()
            time.sleep(self.animation_speed)

    def draw_parents_and_levels(self, x_parent, y_parent, x_level, y_level):
        self.canvas.create_text(400, 500, text=f"Parent of X: {x_parent}")
        self.canvas.create_text(400, 530, text=f"Parent of Y: {y_parent}")
        self.canvas.create_text(400, 560, text=f"Level of X: {x_level}")
        self.canvas.create_text(400, 590, text=f"Level of Y: {y_level}")

    def visualize(self):
        self.draw_tree(self.root, 400, 50, 1)
        self.helper(self.root, None, 0, self.x, "red")
        self.helper(self.root, None, 0, self.y, "blue")
        self.window.mainloop()

    def helper(self, node, parent, level, val, color):
        if not node:
            return
        self.highlight_node(node, "yellow")  # Highlight the current node with the specified color
        if node.val == val:
            node.finial_color = color
            self.highlight_node(node, color)  # Stop traversing further if the node is found
            return
        self.helper(node.left, node, level + 1, val, color)
        self.helper(node.right, node, level + 1, val, color)


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def helper(node, parent, level, val):
            if not node:
                return None
            if node.val == val:
                return parent, level
            return (helper(node.left, node, level + 1, val) or
                    helper(node.right, node, level + 1, val))

        # Initialize the visualization class
        solution_vis = SolutionVisualization(root, x, y)

        # Perform the tree traversal and visualization
        x_parent, x_level = helper(root, None, 0, x)
        y_parent, y_level = helper(root, None, 0, y)

        # Return the result of the comparison
        return x_level == y_level and x_parent != y_parent
# Example usage:
# Define the binary tree

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)

    # Define the nodes x and y
    x = 4
    y = 5

    solution_vis = SolutionVisualization(root, x, y)

    # Visualize the binary tree traversal and the result
    solution_vis.visualize()
    # Instantiate the solution class
    solution = Solution()

    # Output the result
    print("Are x and y cousins?", solution.isCousins(root, x, y))