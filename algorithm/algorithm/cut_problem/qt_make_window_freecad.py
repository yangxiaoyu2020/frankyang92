
import sys
sys.path.append("D:/"
                "")

import FreeCAD as App
import Part

# 创建一个新的文档
doc = App.newDocument("MyDocument")

# 创建一个立方体
length = 10.0
width = 5.0
height = 3.0
box = Part.makeBox(length, width, height)

# 将立方体添加到文档中
doc.addObject("Part::Feature", "MyBox").Shape = box

# 保存文档
doc.saveAs("MyDocument.FCStd")

# 清空文档
App.closeDocument("MyDocument")
