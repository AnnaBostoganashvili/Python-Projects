'''
A demo program to create a button which
causes a tree's burn staet to advance
'''

import tree
import button
import graphics

def main():
    win = graphics.GraphWin("Pretty fire", 200, 200)
    my_tree = tree.Tree(
        graphics.Point(100, 100))
    burn_button = button.Button(
        graphics.Point(50, 190),
        graphics.Point(150,150),
        "Burn!")

    my_tree.draw(win)
    burn_button.draw(win)

    click = win.getMouse()
    while not burn_button.point_is_inside(click): # while didn't click the buton keep loopig
        click = win.getMouse()
        
    my_tree.burn_more(win)


    click = win.getMouse()
    while my_tree.is_on_fire():
        # while out click not on the button, get another click 
        while not burn_button.point_is_inside(click):
            click = win.getMouse()
        
        my_tree.burn_more(win)
        click = win.getMouse()
        
    win.getMouse() # make the program wait for clicking
    win.close()
                    


if __name__ == "__main__":
    main()
