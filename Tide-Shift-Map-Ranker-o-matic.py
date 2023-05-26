import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QGridLayout, QLineEdit, QMessageBox, QApplication

class MapScoring(QWidget):
    def __init__(self):
        super().__init__()
        self.map_names = ["SideTracked", "HellScape", "Atlantis", "Alcyone", "Calliope",
                          "Hecate", "Tango Terminal", "Virtual virtue", "Golden Virtue",
                          "Ued Exploration", "Frozen Heart", "Whispers of Gold",
                          "CobbleStone", "Flowering Night", "Sacred Isles", "Force of Nature",
                          "Graviton", "Magannatha", "Pyrite", "Vertigo", "Ultralove"]

        categories = ["Aesthetics", "Pathing", "Base Layout", "Balance"]
        points = [1, 2, 3]

        grid = QGridLayout()
        self.setLayout(grid)

        # Add name input
        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_input, 0, 1)

        # Initialize map name combobox
        self.map_name_combo = QComboBox()
        self.map_name_combo.addItems(self.map_names)
        grid.addWidget(QLabel("Map Name:"), 1, 0)
        grid.addWidget(self.map_name_combo, 1, 1)

        self.cat_combos = []  # List to store category comboboxes

        for i, category in enumerate(categories):
            cat_label = QLabel(category + ":")
            cat_combo = QComboBox()
            cat_combo.addItems([str(p) for p in points])
            grid.addWidget(cat_label, i + 2, 0)
            grid.addWidget(cat_combo, i + 2, 1)
            self.cat_combos.append(cat_combo)

        # Add submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_scores)
        grid.addWidget(self.submit_button, len(categories) + 2, 0, 1, 2)

        self.user_name = ""  # Variable to store user's name
        self.scored_maps = set()  # Set to store scored maps

    def submit_scores(self):
        name = self.name_input.text()

        if not name:
            QMessageBox.warning(self, "No name entered", "Please enter your name.")
            return

        self.user_name = name  # Update user's name

        map_name = self.map_name_combo.currentText()
        scores = [int(cat_combo.currentText()) for cat_combo in self.cat_combos]

        # Save to file
        with open("map_scores.txt", "a") as f:
            f.write(f"{self.user_name}'s scores for {map_name}: {scores}\n")

        self.scored_maps.add(map_name)  # Add the scored map to the set

        if len(self.scored_maps) == len(self.map_names):
            QMessageBox.information(self, "All maps scored", "You have scored all available maps.")
        else:
            current_index = self.map_name_combo.currentIndex()
            self.map_name_combo.removeItem(current_index)

        if len(self.scored_maps) < len(self.map_names):
            self.map_name_combo.setCurrentIndex(0)

        # Clear category comboboxes for the next map
        for cat_combo in self.cat_combos:
            cat_combo.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapScoring()
    window.show()
    sys.exit(app.exec_())
