import os

# Directory containing the meme images
folder_path = "."

# LaTeX code template for including an image
latex_template = "\\begin{{figure}}[htbp]\n\\centering\n\\includegraphics[width=0.8\\textwidth]{{{}}}\n\\caption{{Your caption here.}}\n\\label{{fig:{}}}\n\\end{{figure}}\n\n"

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
  # Check if the file is an image
  if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
    # Generate the LaTeX code for including the image
    latex_code = latex_template.format(filename, os.path.splitext(filename)[0])
    # Append the LaTeX code to your report.tex file or store it for further processing
# Optionally, you can write the full LaTeX code to a .tex file
with open("memes.tex", "w") as file:
  # Write your preamble and any necessary LaTeX code
  file.write("\\documentclass{article}\n")
  file.write("\\usepackage{graphicx}\n\n")
  # Write the LaTeX code for each image
  for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
      latex_code = latex_template.format(filename, os.path.splitext(filename)[0])
      file.write(latex_code)
  # Write your postamble and close the file
  file.write("\\end{document}")
