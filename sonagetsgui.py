#!/bin/python3
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import os
import math

IMAGE_FORMATS = (".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")
SONASIGNATURE = "\nSonaGets GUI v1.1 • zinclinux 2025"

class SonaGetsGUI(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title(SONASIGNATURE)

		# Button frame
		self.button_frame = tk.Frame(self,borderwidth=1, relief="flat", bg="white")
		self.button_frame.pack(side="top", fill="x", padx=1, pady=1)

		self.select_button = tk.Button(self.button_frame, text="SELECT", command=self.select_image,borderwidth=1, relief="solid")
		self.select_button.pack(side=tk.LEFT, padx=2, pady=2)

		self.inject_button = tk.Button(self.button_frame, text="INJECT", command=self.inject_data, state=tk.DISABLED,borderwidth=1, relief="solid")
		self.inject_button.pack(side=tk.LEFT, padx=2, pady=2)

		self.extract_button = tk.Button(self.button_frame, text="EXTRACT", command=self.extract_data, state=tk.DISABLED,borderwidth=1, relief="solid")
		self.extract_button.pack(side=tk.LEFT, padx=2, pady=2)

		self.xor_button = tk.Button(self.button_frame, text="XORCYST", command=self.xor_data, state=tk.DISABLED,borderwidth=1, relief="solid")
		self.xor_button.pack(side=tk.LEFT, padx=2, pady=2)

		self.help_button = tk.Button(self.button_frame, text="?", command=self.show_help,borderwidth=1, relief="solid")
		self.help_button.pack(side=tk.LEFT, padx=2, pady=2)

		# Image frame
		self.image_frame = tk.Frame(self)
		self.image_frame.pack(fill="both", expand=True)

		self.image_label = tk.Label(self.image_frame,relief="flat")
		self.image_label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

		# Status bar
		self.status_bar = tk.Label(self, text=SONASIGNATURE, anchor="center", borderwidth=1, relief="flat", bg="white")
		self.status_bar.pack(side="bottom", fill="x", pady=2, padx=1)

		# save Image details
		self.image_path = None
		self.image_width = 0
		self.image_height = 0
		self.image_format = None
		self.image_aspect_ratio = 0

	def select_image(self):
		filetypes = [(f"Image Files ({','.join(IMAGE_FORMATS[1:])})", IMAGE_FORMATS)]
		file_path = filedialog.askopenfilename(filetypes=filetypes)
		self.load_image(file_path)

	def load_image(self, file_path):
		if file_path:
			self.image_path = file_path
			image = Image.open(file_path)
			self.image_format = image.format

			# Resize image to available window space, preserving a minimum height & correct aspect ratio
			width, height = image.size
			aspect_ratio = width / height
			self.image_aspect_ratio = aspect_ratio

			available_height = self.winfo_height() - (self.button_frame.winfo_height() + self.status_bar.winfo_height()*2)
			resize_height = int(max(240, available_height))
			resize_width = int(resize_height * aspect_ratio)

			image = image.resize((resize_width, resize_height), Image.LANCZOS)
			photo = ImageTk.PhotoImage(image)

			self.image_label.config(image=photo)
			self.image_label.image = photo  # Reference to prevent garbage collection

			self.image_width, self.image_height = image.size  # Store image dimensions

			# Update select button text and status bar
			file_extension = file_path.split(".")[-1].upper()
			pixels = width * height
			self.select_button.config(text=f"{width}×{height} {file_extension} • {pixels}px")
			self.status_bar.config(text=f"\nImage loaded: {file_path}")

			# Enable buttons if image format is PNG 
			self.extract_button['state'] = tk.NORMAL if (self.image_format == "PNG") else tk.DISABLED
			self.xor_button['state'] = tk.NORMAL if (self.image_format == "PNG") else tk.DISABLED
			self.inject_button['state'] = tk.NORMAL  # Enable for all images

	def process_image(self, mode):
		if self.image_path:
			try:
				if mode == "inject":
					filetypes = (
						("Text Files", "*.txt"),
						("Compressed Files", "*.zip"),
					)
					file_path = filedialog.askopenfilename(filetypes=filetypes)
					if file_path:
						image_size = self.image_width * self.image_height
						file_size = os.path.getsize(file_path)

						if file_size <= image_size:
							result = subprocess.run(["sonagets", "-i", self.image_path, file_path], capture_output=True, text=True)
							last_line = result.stdout.splitlines()[-1]
							self.status_bar.config(text=f"{file_path}\n{last_line}")
						else:
							messagebox.showerror("Error", "Inject file is larger than image.")

				elif mode == "extract" or mode == "xor":
					if self.image_path.endswith(".png"):
						if mode == "extract":
							result = subprocess.run(["sonagets", "-e", self.image_path], capture_output=True, text=True)
							if result.returncode != 0:
								self.status_bar.config(text=f"Extraction from {self.image_path} failed")
							else:
								last_line = result.stdout.splitlines()[-1]
								self.status_bar.config(text=f"{self.image_path}\n{last_line}")
						elif mode == "xor":
							file_path = filedialog.askopenfilename()
							if file_path:
								result = subprocess.run(["sonagets", "-x", self.image_path, file_path], capture_output=True, text=True)
								if result.returncode != 0:
									self.status_bar.config(text=f"XOR operation on {self.image_path} failed")
								else:
									last_line = result.stdout.splitlines()[-1]
									self.status_bar.config(text=f"{self.image_path}\n{last_line}")
			except Exception as e:
				messagebox.showerror("Error", str(e))

	def inject_data(self):
		self.process_image("inject")

	def extract_data(self):
		self.process_image("extract")

	def xor_data(self):
		self.process_image("xor")

	def show_help(self):
		help_text = "Select an image, then:\nInject TXT or ZIP file into new PNG,\nExtract data from PNG,\nor XOR file w/ PNG cipher."
		messagebox.showinfo("2LSB Steganos & 6MSB XOR", help_text)

	@staticmethod
	def perfect_fit(package_size, aspect_ratio):
		"""Returns (width, height) of proportionate rectangle to fit package."""
		package_size += 4  # plaintext files may be padded
		height = math.ceil(math.sqrt(package_size / aspect_ratio))
		width = round(aspect_ratio * height)

		if width * height < package_size: height += 1
		
		return width, height


if __name__ == "__main__":
	app = SonaGetsGUI()
	#print(app.perfect_fit(3730,1.0))
	app.mainloop()
