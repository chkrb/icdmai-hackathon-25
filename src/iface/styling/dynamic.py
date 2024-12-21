class DynamicColor:
    def __init__(self, label):
        self.label = label  # Now, we accept the label to which the color will be applied

    def update_color(self, value):
        self.label.setText(f"Value: {value}")

        # Set the color based on the value
        if value > 8:
            color = "#00ff00"  # Green
        elif 4 <= value <= 8:
            color = "#ffa500"  # Orange
        else:
            color = "#ff0000"  # Red
        
        # Update the label color dynamically
        self.label.setStyleSheet(f"color: {color};")
