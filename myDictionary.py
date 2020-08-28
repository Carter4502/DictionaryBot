import tkinter as tk
import urllib.request, json, pyglet
from tkinter.messagebox import showerror

MERRIAMWEBSTER_API_KEY = "348681ad-c66a-4c9a-b106-c22418f83cfe"

def clear_entry(event, entry):
    entry.delete(0, tk.END)
def getDefinition(text, root):
	url = "https://www.dictionaryapi.com/api/v3/references/collegiate/json/" + text + "?key=" + MERRIAMWEBSTER_API_KEY
	fp = urllib.request.urlopen(url)
	mybytes = fp.read()
	myJson = json.loads(mybytes.decode("utf8"))
	fp.close()
	syllables = myJson[0]["hwi"]["hw"]
	definition = myJson[0]["shortdef"][0]
	wordLabel = tk.Label(root, fg="#35b999", bg="white", font=("Objektiv Mk1 W03 XBold", 30))
	wordLabel["text"] = text
	wordLabel.place(relx=0.2, rely=0.225, anchor="n")
	pronounceLabel = tk.Label(root, fg="#03363d", bg="white", font=("Objektiv Mk1 W03 Regular", 15))
	pronounceLabel["text"] ="(" + syllables.replace("*", "-") + ")"
	pronounceLabel.place(relx=0.2, rely=0.325, anchor="n")
	definitionLabel = tk.Label(root, fg="#03363d", bg="white", font=("Objektiv Mk1 W03 Regular", 18), wraplengt=500, justify="left")
	definitionLabel["text"] = "- " + definition + "."
	definitionLabel.place(relx=0.4, rely=0.48, relwidth=0.6, relheight=0.1, anchor="n")
	btnTText = tk.StringVar()
	btnTText.set("New Word!")
	newWordButton = tk.Button(root, fg="white", bg="#35b999", font=("Objektiv mk1 W03 Xbold", 15), textvariable=btnTText, borderwidth=0, highlightthickness=0, command=lambda:[root.destroy(), main()])
	newWordButton.place(relx=0.5, rely=0.8, anchor="n", relwidth=0.3, relheight=0.1)
def main():
	pyglet.font.add_file("Objektiv Mk1 W03 XBold.ttf")
	pyglet.font.add_file("Objektiv Mk1 W03 Regular.ttf")
	root = tk.Tk()
	root.geometry("900x700")
	root.title("Dictionary")
	root.resizable(False, False)
	bgLabel = tk.Label(root, bg="white")
	bgLabel.place(relheight=1, relwidth=1)
	titleLabel = tk.Label(root, fg="#03363d", bg="white", font=("Objektiv Mk1 W03 XBold", 30))
	titleLabel["text"] = "PyDictionary"
	titleLabel.place(relx=0.2, rely=0.05, anchor="n")
	mainEntry = tk.Entry(root, borderwidth = 0, highlightthickness = 0, font=("Objektiv Mk1 W03 Regular", 14), fg="grey", justify="center", bg="#f3f3f3")
	mainEntry.insert(0, "Type a word...")
	mainEntry.place(relheight=0.06, relwidth=0.5, relx = 0.5, rely=0.4, anchor="n")
	mainEntry.bind("<Button-1>", lambda event: clear_entry(event, mainEntry))
	butText = tk.StringVar()
	butText.set("Go")
	getDefButton = tk.Button(root, fg="white", bg="#35b999", font = ("Objektiv Mk1 W03 Xbold", 14), borderwidth=0, highlightthickness=0, textvariable=butText,
		command=lambda:[getDefinition(mainEntry.get(), root), mainEntry.destroy(), getDefButton.destroy()])
	getDefButton.place(relx=0.85, rely=0.4, anchor="n", relwidth=0.15, relheight=0.06)
	authorLabel = tk.Label(root, fg="#35b999", bg="white", font=("Objektiv Mk1 W03 Xbold", 10))
	authorLabel["text"] = "Created by Carter Belisle"
	authorLabel.place(relx=0.14, rely=0.92, anchor="n")

	tk.mainloop()


if __name__ == '__main__':
	main()
