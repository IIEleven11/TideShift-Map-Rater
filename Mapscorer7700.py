import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QLineEdit, QMessageBox, QGridLayout, QApplication

class MapScoring(QWidget):
    def __init__(self):
        super().__init__()
        self.cat_combos = [] 
        map_names = ["SideTracked", "HellScape", "Atlantis", "Alcyone", "Calliope", 
                     "Hecate", "Tango Terminal", "Virtual virtue", "Golden Virtue", 
                     "Ued Exploration", "Frozen Heart", "Whispers of Gold", 
                     "CobbleStone", "Flowering Night", "Sacred Isles", "Force of Nature", 
                     "Graviton", "Magannatha", "Pyrite", "Vertigo", "Ultralove"]
        
        categories = ["Aesthetics", "Pathing", "Base Layout", "Balance"]
        points = [1, 2, 3]

        grid = QGridLayout()
        self.setLayout(grid) 

            # Add map name combobox
        map_name_label = QLabel("Map Name:")
        map_name_combo = QComboBox()
        map_name_combo.addItems(map_names)
        grid.addWidget(map_name_label, 0, 0)
        grid.addWidget(map_name_combo, 0, 1)

        for i, category in enumerate(categories):
            cat_label = QLabel(category + ":")
            cat_combo = QComboBox()
            cat_combo.addItems([str(p) for p in points])
            self.cat_combos.append(cat_combo)
            grid.addWidget(cat_label, 1+i, 0)
            grid.addWidget(cat_combo, 1+i, 1)

               # Add category comboboxes and scoring buttons

        # Prompt for user name
        name_label = QLabel("Your name:")
        self.name_input = QLineEdit()
        grid.addWidget(name_label, 1, 0)
        grid.addWidget(self.name_input, 1, 1)
        
        # Rest of UI...
        
        # Add submit button
        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit_scores)
        grid.addWidget(submit_button, 6, 0, 1, 2)
        
    def submit_scores(self):
        name = self.name_input.text()
        self.map_name = self.map_name_combo.currentText()
        scores = [int(cat_combo.currentText()) for cat_combo in self.cat_combos]

        
        # Save to file
        with open("map_scores.txt", "a") as f:
            f.write(f"{name}'s scores for {self.map_name}: {scores}\n") 

            if not name:
                QMessageBox.warning(self, "No name entered", "Please enter your name.")
                return 
            # Get scores...
            QMessageBox.information(self, "Scores submitted!", "Your scores have been submitted. Thank you!")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapScoring()
    window.show()
    sys.exit(app.exec_())
