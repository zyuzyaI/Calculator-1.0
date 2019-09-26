from tkinter import *

def frame(root, side=TOP, **extras):
	widget = Frame(root)
	widget.pack(side=side, expand=YES, fill=BOTH)
	if extras:
		widget.config(**extras)
	return widget

def button(root, side, text, command, **extras):
	widget = Button(root, text=text, command=command)
	widget.pack(side=side, expand=YES, fill=BOTH)
	if extras:
		widget.config(**extras)
	return widget

def entry(root, side, linkvar, **extras):
	widget = Entry(root, relief=SUNKEN, textvariable=linkvar)
	widget.pack(side=side, expand=YES, fill=BOTH)
	if extras:
		widget.config(**extras)
	return widget

class Calculator_gui(Frame):
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack(expand=YES, fill=BOTH)
		self.master.title('Python GUI calculator ')
		self.master.iconname('pcalc1')

		self.names = {}
		text = StringVar()
		entry(self, TOP, text)

		rows = ['0123', '4567', '89()']
		for row in rows:
			frm = frame(self, TOP)
			for char in row:
				button(frm, LEFT, char, lambda char=char: text.set(text.get()+char))

		frm = frame(self, TOP)
		for char in '+-*/=':
			button(frm, LEFT, char, lambda char=char: text.set(text.get()+' '+char+' '))

		frm = frame(self, BOTTOM)
		button(frm, LEFT, 'eval', lambda: self.result(text))
		button(frm, LEFT, 'clear', lambda: text.set(''))

	def result(self, text):
		try:
			text.set(str(eval(text.get(), self.names, self.names)))

		except SyntaxError:
			try:
				exec(text.get(), self.names, self.names)
			except:
				text.set('ERROR')
			else:
				text.set('')
		except:
			text.set('er')
if __name__ == '__main__':
	Calculator_gui().mainloop()
