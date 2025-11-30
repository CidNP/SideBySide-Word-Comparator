

# DocDiff Viewer

DocDiff Viewer is a Python-based GUI application that allows users to compare two Microsoft Word documents (`.docx`) side by side.  
It highlights differences at the **paragraph level** and provides synchronized scrolling for easy review.

---

##  Features

- **Step-by-step upload prompts**: Guided messages ensure you upload Document 1 (Original) first, then Document 2 (Comparison).
- **Paragraph-level comparison**: Detects differences at the paragraph level instead of line-by-line.
- **Color-coded highlights**:
  - Yellow → Paragraph missing in Document 2 (compared to Document 1).
  - Green → Paragraph extra in Document 2.
  - No highlight → Identical content.
- **Side-by-side view**: Displays both documents in separate panes with clear labels.
- **Scroll synchronization**: Scroll either pane and the other moves in sync.
- **Legend bar**: Explains highlight colors for quick reference.

---

## 🛠️ Installation

1. Clone or download this repository.
2. Install required dependencies:
   ```bash
   pip install python-docx

## Usuage
1. Launch the app.
2. Follow the prompts:
   Upload Document 1 (Original).
   Upload Document 2 (Comparison).
3. A new window opens showing both documents side by side.
4. Review differences using highlights and synchronized scrolling.



## Example Workflow
Document 1 (Original)
- **Agile improves productivity.
- **Scrum is widely adopted.

Document 2 (Comparison)
- **Agile improves productivity.
- **Scrum is widely adopted.
- **Kanban is also useful.


Result:
- **"Agile improves productivity." → identical
- **"Scrum is widely adopted." → identical
- **"Kanban is also useful." → highlighted green (extra in Document 2)


---

This README is structured, professional, and ready for GitHub or sharing with collaborators.  

Would you like me to also create a **short tagline** (like a one‑liner slogan) for the app that you can use in presentations or GitHub repo description?
