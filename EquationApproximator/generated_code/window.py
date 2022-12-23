import tkinter
from tkinter import *
from EO.EquationOptimizer import *
import tkinter.scrolledtext as st
import tkinter as tk


# Takes console output and displays it on the scrollable text box
def redirector(inputStr):
    outputText.insert(INSERT, inputStr)
    outputText.see(tkinter.END)
    canvas.update()


sys.stdout.write = redirector  # Whenever sys.stdout.write is called, redirector is called.


# Executes the genetic algorithm to find a solution to a given equation with (x, y, z) variables
def executeAlgo(inputEq):
    global string

    string = geneticAlgo(inputEq)


# Approximate Button event handler, executes algorithm and changes labels/text accordingly
def approx_btn_clicked():
    global string
    global done

    try:
        inputEq = entry0.get()  # Taking the input equation from the Equation text box

        canvas.itemconfig(statusText, text="Loading...")
        canvas.update()

        executeAlgo(inputEq)

        canvas.itemconfig(statusText, text=f"Solution approximated as {string}")
        canvas.update()
    except:
        canvas.itemconfig(statusText, text="Error occurred, please fix the input.")


window = Tk()

window.title("Genetic Approximator by Mohammad Baqer")
window.geometry("1104x402")
window.configure(bg="#1a1a1a")
windowWidth = 1104
inputWidth = 738
canvas = Canvas(
    window,
    bg="#1a1a1a",
    height=402,
    width=windowWidth,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

canvas.create_text(
    369.5, 50.0,
    text="Genetic Approximator",
    fill="#c0f1f4",
    font=("SecularOne-Regular", int(36.0)))

canvas.create_text(
    inputWidth / 2, 120.0,
    text="Enter an equation with the three variables x, y, and z.",
    fill="#ffffff",
    font=("SecularOne-Regular", int(14.0)))

canvas.create_text(
    inputWidth / 2, 160.0,
    text="The program utilizes a Genetic Algorithm to approximate",
    fill="#ffffff",
    font=("SecularOne-Regular", int(14.0)))

canvas.create_text(
    inputWidth / 2, 190.0,
    text="a solution to the given equation.",
    fill="#ffffff",
    font=("SecularOne-Regular", int(14.0)))

canvas.create_text(
    inputWidth / 2, 220.0,
    text="Trigonometric and logarithmic functions are not supported.",
    fill="#ffffff",
    font=("SecularOne-Regular", int(14.0)))

statusText = canvas.create_text(
    inputWidth / 2, 260.0,
    text="To use powers, use Python format (Ex. x^2 would be x**2)",
    fill="#ffffff",
    font=("SecularOne-Regular", int(14.0)))

canvas.create_text(
    130, 296.5,
    text="Equation:",
    fill="#c0f1f4",
    font=("SecularOne-Regular", int(18.0)))

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    text="Approximate",
    font=("SecularOne-Regular", int(13.0)),
    compound="center",
    borderwidth=0,
    highlightthickness=0,
    command=approx_btn_clicked,
    relief="flat")

b0.place(
    x=299, y=329,
    width=141,
    height=37)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    414.0, 296.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    font=("SecularOne-Regular", int(13.0)),
    bg="#c4c4c4",
    highlightthickness=0)

entry0.insert(-1, "x**2 + 5*y - z")

entry0.place(
    x=188, y=281,
    width=458,
    height=29)

"""
canvas.create_rectangle(
    738, 0, 738+366, 0+402,
    fill = "#c4c4c4",
    outline = "")
"""

outputText = st.ScrolledText(canvas,
                             width=39,
                             height=21,
                             font=("SecularOne-Regular", 13))

outputText.place(
    x=730,
    y=0
)

outputText.insert(tk.INSERT,
                  "                                Output:\n\n")

window.resizable(False, False)
window.mainloop()
