local robot = require("robot")
local component = require("component")
NumberOfBlocks=8--number of farmland blckt to move
 
loop = 1
 
repeat
    while robot.detectDown() do--wait until first crop is broken
        
    end
 
    robot.turnLeft()--take from chset
    robot.forward()--take from chset
    robot.suckDown(NumberOfBlocks*2)--number of crop sticks to take *2
    component.inventory_controller.equip()--equip crop sticks
    robot.back()--return to previous direction
    robot.turnRight()--return to previous direction
    for i = 1, NumberOfBlocks do--loop to put crop sticks

        robot.useDown()
        robot.useDown()
        robot.forward()
    end
    robot.turnAround()--turn around
    for i = 1, NumberOfBlocks do--loop to turn to original place
        robot.forward()
    end
    robot.turnAround()--turn around to face farmland dirction
    
 
until loop >1