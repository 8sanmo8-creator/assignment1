import turtle
import colorsys
import random

screen = turtle.Screen()
screen.setup(width=900, height=800)
screen.bgcolor("black")
screen.title("Colourful Geometric Pattern Generator")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

# Drawing
def get_colour(index, total):
    hue = (index / total) % 1.0
    red, green, blue = colorsys.hsv_to_rgb(hue, 0.9, 1.0)
    return red, green, blue


def draw_square(length):
    for side in range(4):
        pen.forward(length)
        pen.right(90)


def draw_triangle(length):
    for side in range(3):
        pen.forward(length)
        pen.right(120)


def draw_star(length):
    for point in range(5):
        pen.forward(length)
        pen.right(144)


def draw_shape(shape, length):
    if shape == "square":
        draw_square(length)
    elif shape == "triangle":
        draw_triangle(length)
    elif shape == "star":
        draw_star(length)


def draw_pattern(shape, number_of_shapes, start_length):
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    pen.pendown()

    length = start_length

    for i in range(number_of_shapes):
        colour = get_colour(i, number_of_shapes)
        pen.pencolor(colour)

        draw_shape(shape, length)

        pen.right(360 / number_of_shapes)

        length += 3

        if length > start_length + 120:
            length = start_length


def draw_random_pattern(number_of_shapes, start_length):
    pen.clear()

    length = start_length

    for i in range(number_of_shapes):
        pen.penup()
        pen.goto(
            random.randint(-300, 300),
            random.randint(-250, 250)
        )
        pen.setheading(random.randint(0, 360))
        pen.pendown()

        colour = get_colour(i, number_of_shapes)
        pen.pencolor(colour)

        shape = random.choice(["square", "triangle", "star"])
        draw_shape(shape, length)

        length += 2

        if length > start_length + 100:
            length = start_length

def drawing_menu():
    while True:
        print("\n------ Drawing System ------")
        print("1. Square pattern")
        print("2. Triangle pattern")
        print("3. Star pattern")
        print("4. Random colourful pattern")
        print("5. Return to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Returning to the main menu...")
            break

        elif choice not in ["1", "2", "3", "4"]:
            print("Please enter a number from 1 to 5.")
            continue

        try:
            number_of_shapes = int(
                input("How many shapes should be drawn? ")
            )

            start_length = int(
                input("Enter the starting length: ")
            )

            if number_of_shapes <= 0 or start_length <= 0:
                print("Please enter positive numbers.")
                continue

        except ValueError:
            print("Please enter numbers only.")
            continue

        if choice == "1":
            draw_pattern("square", number_of_shapes, start_length)

        elif choice == "2":
            draw_pattern("triangle", number_of_shapes, start_length)

        elif choice == "3":
            draw_pattern("star", number_of_shapes, start_length)

        elif choice == "4":
            draw_random_pattern(number_of_shapes, start_length)

        print("Pattern complete.")

# QA bot
def qa_bot():
    print("\n------ Welcome to the QA Bot ------")
    print("Ask about HKU, robots, Jetson, AI, or humans.")
    print("Type 'back' to return to the main menu.")

    while True:
        question = input("\nYour question: ").strip().lower()

        if question == "back":
            print("Returning to the main menu...")
            break

        elif "hku" in question:
            print("Bot: HKU stands for The University of Hong Kong.")

        elif "robot" in question or "robots" in question:
            print("Bot: A robot is a machine that can sense its environment and perform tasks.")

        elif "jetson" in question:
            print("Bot: NVIDIA Jetson is used for AI and robotics projects.")

        elif "ai" in question or "artificial intelligence" in question:
            print("Bot: AI allows computers to perform intelligent tasks.")

        elif "human" in question or "humans" in question:
            print("Bot: Humans can think, learn, communicate, and solve problems.")

        else:
            print("Bot: I do not understand.")
            print("Try asking about HKU, robot, Jetson, AI, or human.")


def main_menu():
    while True:
        print("\n======================================")
        print("     Drawing and QA Bot System")
        print("======================================")
        print("1. Drawing system")
        print("2. QA bot")
        print("3. Exit")

        choice = input("Please choose an option: ").strip()
        if choice == "1":
            drawing_menu()
        elif choice == "2":
            qa_bot()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main_menu()
turtle.done()
