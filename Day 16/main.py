# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('coral')
# timmy.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

my_table = PrettyTable()
my_table.add_column("Pokemon Type", ["Pikachu", "Squirtle", "Charmander"])
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align = 'l'
print(my_table.align)
print(my_table)