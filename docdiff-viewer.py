import tkinter as tk
from tkinter import filedialog, messagebox
from docx import Document
import difflib

def read_docx(file_path):
    doc = Document(file_path)
    text = []
    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text.strip())
    return text

def show_side_by_side(doc1_path, doc2_path):
    text1 = read_docx(doc1_path)
    text2 = read_docx(doc2_path)

    diff = list(difflib.ndiff(text1, text2))

    # Create new window for side-by-side view
    compare_win = tk.Toplevel()
    compare_win.title("Side-by-Side Comparison (Document 1 = Original)")

    # Legend
    legend = tk.Label(compare_win, text="Legend: Yellow = Missing in Document 2 | Green = Extra in Document 2")
    legend.pack(pady=5)

    # Frame for side-by-side panes
    frame = tk.Frame(compare_win)
    frame.pack(fill="both", expand=True)

    # Left pane with label
    left_frame = tk.Frame(frame)
    left_frame.pack(side="left", fill="both", expand=True)

    left_label = tk.Label(left_frame, text="Document 1 (Original)", bg="lightgray")
    left_label.pack(fill="x")

    left_text = tk.Text(left_frame, wrap="word", width=60, height=30)
    left_scroll = tk.Scrollbar(left_frame, command=left_text.yview)
    left_text.configure(yscrollcommand=left_scroll.set)
    left_scroll.pack(side="right", fill="y")
    left_text.pack(fill="both", expand=True)

    # Right pane with label
    right_frame = tk.Frame(frame)
    right_frame.pack(side="right", fill="both", expand=True)

    right_label = tk.Label(right_frame, text="Document 2 (Comparison)", bg="lightgray")
    right_label.pack(fill="x")

    right_text = tk.Text(right_frame, wrap="word", width=60, height=30)
    right_scroll = tk.Scrollbar(right_frame, command=right_text.yview)
    right_text.configure(yscrollcommand=right_scroll.set)
    right_scroll.pack(side="right", fill="y")
    right_text.pack(fill="both", expand=True)

    # Define tags for highlighting
    left_text.tag_config("missing", background="yellow")
    right_text.tag_config("extra", background="lightgreen")

    # Populate text areas with highlights
    for line in diff:
        if line.startswith("  "):  # same
            left_text.insert("end", line[2:] + "\n")
            right_text.insert("end", line[2:] + "\n")
        elif line.startswith("- "):  # missing in doc2
            left_text.insert("end", line[2:] + "\n", "missing")
        elif line.startswith("+ "):  # extra in doc2
            right_text.insert("end", line[2:] + "\n", "extra")

    # --- Scroll synchronization ---
        # --- Scroll synchronization ---
    def sync_scroll_left(*args):
        # args[0] is the fraction string like "0.2284"
        fraction = float(args[0])
        right_text.yview_moveto(fraction)
        left_scroll.set(*args)

    def sync_scroll_right(*args):
        fraction = float(args[0])
        left_text.yview_moveto(fraction)
        right_scroll.set(*args)

    left_text.configure(yscrollcommand=sync_scroll_left)
    right_text.configure(yscrollcommand=sync_scroll_right)


def select_files():
    # Step 1: Upload Document 1
    messagebox.showinfo("Upload", "Please upload Document 1 (Original)")
    file1 = filedialog.askopenfilename(title="Select Original Document (Doc1)", filetypes=[("Word files", "*.docx")])

    if not file1:
        messagebox.showwarning("Warning", "No Document 1 selected. Process stopped.")
        return

    # Step 2: Upload Document 2
    messagebox.showinfo("Upload", "Please upload Document 2 (Comparison)")
    file2 = filedialog.askopenfilename(title="Select Comparison Document (Doc2)", filetypes=[("Word files", "*.docx")])

    if not file2:
        messagebox.showwarning("Warning", "No Document 2 selected. Process stopped.")
        return

    # Step 3: Show comparison
    show_side_by_side(file1, file2)

# GUI setup
root = tk.Tk()
root.title("Word Document Comparator")

label = tk.Label(root, text="Step-by-step: Upload Original, then Comparison Document")
label.pack(pady=10)

btn = tk.Button(root, text="Start Upload", command=select_files)
btn.pack(pady=20)

root.mainloop()
