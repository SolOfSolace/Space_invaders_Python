# Space_invaders_Python

This follows Tokyo ED Tech's youtube tutorial on creating a python version of Space invaders

I am using python version 3.7 and he is using version 2.7 so the code to exit the game
                    delay = raw_input("Press enter to exit")
needs to be replaced with 
                    wn.exitonclick()
                    turtle.done()
                    try:
                        turtle.bye()   
                    except turtle.Terminator:
                        pass
otherwise python will crash. 
