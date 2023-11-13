import tkinter

class Calculator:
  def __init__(self):
    self.root = tkinter.Tk()
    self.root.title("Calculator")
    self.n1_entry = tkinter.Entry(self.root)
    self.n1_entry.pack()
    self.n2_entry = tkinter.Entry(self.root)
    self.n2_entry.pack()
    self.add_button = tkinter.Button(self.root, text="+", command=self.add)
    self.add_button.pack()
    self.subtract_button = tkinter.Button(self.root, text="-", command=self.subtract)
    self.subtract_button.pack()
    self.multiply_button = tkinter.Button(self.root, text="*", command=self.multiply)
    self.multiply_button.pack()
    self.divide_button = tkinter.Button(self.root, text="/", command=self.divide)
    self.divide_button.pack()
    self.result_label = tkinter.Label(self.root)
    self.result_label.pack()
    self.root.mainloop()

  def add(self):
    n1 = float(self.n1_entry.get())
    n2 = float(self.n2_entry.get())
    result = n1 + n2
    self.result_label.config(text=str(result))

  def subtract(self):
    n1 = float(self.n1_entry.get())
    n2 = float(self.n2_entry.get())
    result = n1 - n2
    self.result_label.config(text=str(result))

  def multiply(self):
    n1 = float(self.n1_entry.get())
    n2 = float(self.n2_entry.get())
    result = n1 * n2
    self.result_label.config(text=str(result))

  def divide(self):
    n1 = float(self.n1_entry.get())
    n2 = float(self.n2_entry.get())
    result = n1 / n2
    self.result_label.config(text=str(result))

if __name__ == "__main__":
  calculator = Calculator()
