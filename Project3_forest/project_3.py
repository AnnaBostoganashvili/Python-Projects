'''
Anna Bostoganashvili -- Dr. Bailey, CSC170.
Project 3 - Forest Fire Simulation
'''
# import functions 
import tree
import button
import graphics
import random

# set tree size as global variable 
TREE_SIZE = 29

# function to make a tree 
def make_a_tree(win, x, y):         
    # make a tree at a point(x,y)
    one_tree = tree.Tree(
        graphics.Point(x,y))

    one_tree.draw(win) # draw tree to window

    return one_tree # return tree

# function to make a forest 
def make_forest(treeGrid, win):
    # distance between the trees 
    x = TREE_SIZE/2
    y = TREE_SIZE/2
    # looping through each row and then col within row
    for row in range(len(treeGrid)):
        for col in range(len(treeGrid[row])):
            # call make_a_tree at this point on grid
            treeGrid[row][col] = make_a_tree(win, x, y) 
            x = x + TREE_SIZE
        y = y + TREE_SIZE
        x = TREE_SIZE/2

# function to set the fire
def random_burn(win, inputBox, treeGrid):
    # get the user input 
    user_input = inputBox.getText()
    # while they don't input a valid number
    # keep asking for input 
    while not(0 < float(user_input) < 1):
        user_input = inputBox.getText()

    row_location = random.randint(0, 9)
    col_location = random.randint(0, 14)
    tree_location = treeGrid[row_location][col_location]

     
    probability = float(user_input) * 100

    # number of fires that were spread 
    count = do_fire_spread(win, treeGrid, probability, tree_location)

    return count


def do_fire_spread(win, treeGrid, probability, tree_location):  
    # we set the tree on fire 
    tree_location.burn_more(win)

    # Continue the simulation
    # count of fires 
    count = 0 
    while fire_on_tree(treeGrid):
        row_count = 0
        for row in treeGrid:
            col_count = 0 
            for tree in row:
                if tree.is_on_fire():
                    does_tree_catch(win, tree, treeGrid,
                                    row_count, col_count, probability)
                    
                col_count += 1
            row_count += 1
        count += 1

    return count

# function to check if tree is on fire
def fire_on_tree(treeGrid):
    for row in treeGrid:
        for tree in row:
            if tree.is_on_fire():
                return True
    return False 
            

# function to check if a tree catches fire
def does_tree_catch(win, tree, treeGrid, row_count, col_count, probability):
    # if the tree is not on fire then just return,
    # because there is no tree on fire. 
    if not(tree.is_on_fire()):
        return
    # looping over the rows around the tree
    # lopping over the columns in rows around the tree 
    for i_row in range(row_count-1, row_count+2):
        for i_col in range(col_count-1, col_count+2):
            # checking that the tree is withing the grid
            if 0 <= i_row <= 9 and 0 <= i_col <= 14:
                # this is where we need to roll the dice to
                # see if the tree is on fire
                chance_of_fire = random.randint(0, 100)
                if chance_of_fire < float(probability):
                    # if the chance of fire is less that the
                    # probeblity, the tree will burn. 
                    treeGrid[i_row][i_col].burn_more(win)        


# function to click on a tree and burn from there. - second button 
def click_burn(win, treeGrid, inputBox, my_tree):
    click = win.getMouse()

    # click coordinates should be grid indicies
    col_location = int(click.getX() // TREE_SIZE)
    row_location = int(click.getY() // TREE_SIZE)

    tree_location = None
    
    # check if the click is within the grid
    if 0 <= row_location < len(treeGrid) and 0 <= col_location < len(treeGrid[0]):
        tree_location = treeGrid[row_location][col_location]

    if tree_location:
        user_input = inputBox.getText()
        while not(0 < float(user_input) < 1):
            user_input = inputBox.getText()
         
        probability = float(user_input) * 100

        count = do_fire_spread(win, treeGrid, probability, tree_location)

    return count 

# function to make burn buttons 
def burn_button(win, inputBox, treeGrid, my_tree):
    # create the "Run (Random Start)" button 
    random_start_button = button.Button(
        graphics.Point(515, 130),
        graphics.Point(625, 110),
        "Run (Random Start)")

    # create the "Run (click to start)" button 
    click_start_button = button.Button(
        graphics.Point(515, 160),
        graphics.Point(625, 140),
        "Run (Click to Start)")

    # create a "Reset simulation" button 
    reset_button = button.Button(
        graphics.Point(515, 190),
        graphics.Point(625, 170),
        "Reset Simulation")

    # create exit button 
    exit_button = button.Button(
        graphics.Point(700, 0),
        graphics.Point(680, 20),
        "X",
        box_fill = 'red')

    # draw buttons to the window 
    random_start_button.draw(win)
    click_start_button.draw(win)
    reset_button.draw(win)
    exit_button.draw(win)
    
    # get a click
    click = win.getMouse()
    # while there is no click on the exit_button
    # click within other buttons should work
    while not exit_button.point_is_inside(click):  
        if random_start_button.point_is_inside(click):
            # when click first button you get the result of
            # count of trees burned to subside the fire 
            count = random_burn(win, inputBox, treeGrid)
            end_button = button.Button(
        graphics.Point(29, 116),
        graphics.Point(406, 145),
        "Fire subsided in " + str(count) + " steps. Click anywhere to close")
            end_button.draw(win)
            new_click = win.getMouse()
            end_button.undraw()
        elif click_start_button.point_is_inside(click):
            # when you click the second button you get the
            # results of trees burned to subside fire 
            count = click_burn(win, treeGrid, inputBox, my_tree)
            end_button = button.Button(
        graphics.Point(29, 116),
        graphics.Point(406, 145),
        "Fire subsided in " + str(count) + " steps. Click anywhere to close")
            end_button.draw(win)
            new_click = win.getMouse()
            end_button.undraw()
        elif reset_button.point_is_inside(click):
            # looping through each tree on gird
            for row in treeGrid:
                for tree in row:
                    # undrawing the trees
                    tree.undraw()
                # drawing the grid again
            make_forest(treeGrid, win)
        click = win.getMouse()

    win.close()
 
def main():
    # create the windown 
    win = graphics.GraphWin("Forest Fire Simulation", 700, 290)
    my_tree = tree.Tree(
        graphics.Point(100, 100))

    # create the grid of trees 
    treeGrid = []
    for row in range(10):
        new_list = []
        for col in range(15):
            new_list.append(0)
        treeGrid.append(new_list)

    # call the funciton of make_forest
    make_forest(treeGrid, win)

    # to write "Burn Probability:"
    text = graphics.Text(graphics.Point(570,70), "Burn Probability:")
    text.draw(win)
    
    #create the probability box for use input 
    inputBox = graphics.Entry(graphics.Point(570, 90), 20)
    inputBox.draw(win)

    # call the function to implement the burning 
    burn_button(win, inputBox, treeGrid, my_tree)
    
if __name__ == "__main__":
    main()
