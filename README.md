# SideBySide-Word-Comparator

# DocDiff Viewer

DocDiff Viewer is a Python-based GUI application that allows users to compare two Microsoft Word documents (`.docx`) side by side.  
It highlights differences at the **paragraph level** and provides synchronized scrolling for easy review.

---

## ✨ Features

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
