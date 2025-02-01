# Sorting Algorithm Visualizer 🎯

A Python-based GUI application that visually demonstrates how various sorting algorithms work in real-time. Built with Tkinter, this tool helps users understand algorithmic complexity through dynamic visualization and Big O notation displays.

## Overview
The Sorting Algorithm Visualizer is a desktop application that demonstrates how various sorting algorithms work through real-time graphical visualizations. Built using Python’s Tkinter library, the application features multiple sorting algorithms including:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Quick Sort
- Merge Sort

Users can adjust parameters such as the number of elements to sort and the speed of the visualization using an intuitive GUI. In addition, the tool displays the Big O notation of the selected algorithm, offering both an educational and interactive way to learn about sorting methods and algorithm efficiency.

## Features ✨
- **Visualize 5+ Algorithms**: Bubble Sort, Selection Sort, Insertion Sort, Quick Sort, Merge Sort
- **Interactive Controls**:
  - Adjustable speed control (1ms-100ms delay)
  - Dynamic element count adjustment (1-1000 elements)
  - Instant shuffle functionality
- **Educational Components**:
  - Real-time Big O complexity display
  - Responsive canvas visualization
  - Algorithm comparison capabilities
- **Responsive Design**: Auto-scales to 80% of screen size

## Technologies Used 💻
- **Python 3.9+**
- **Tkinter** (GUI Framework)
- **Object-Oriented Programming** principles
- **Modular Architecture** for easy algorithm additions

## Dynamic Configuration:
Users can specify the number of elements (between 1 and 1000) and shuffle the dataset at any time.

## Real-Time Updates:
The GUI updates the visualization in real time as the sorting algorithm progresses.

## Educational Insights:
Displays Big O notation for the chosen sorting algorithm to help users understand the computational complexity.

## Getting Started

Prerequisites
- Python 3.x
- Tkinter (usually included with standard Python installations)
- Installation
- Clone the Repository:


``` bash
git clone https://github.com/yourusername/sorting-algorithm-visualizer.git
cd sorting-algorithm-visualizer
```

(Optional) Create a Virtual Environment:
``` bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
``` 
Run the Application:
``` bash
python sorting_visualizer.py
``` 

## How It Works
User Interface:
The application launches a window where the canvas displays the current list of numbers as vertical bars. A control panel below the canvas includes buttons for shuffling the numbers, updating the number of elements, and selecting the sorting algorithm.

## Visualization:
The bars’ heights represent the numeric values. As the sorting algorithm proceeds, the positions of these bars are updated in real time to show the algorithm’s progress.

## Algorithm Selection:
Each sorting algorithm is implemented as a separate method. Upon selecting an algorithm, the program executes the method and uses tkinter's update and delay functions to animate the process.

## Performance Insights:
After sorting, the Big O notation of the algorithm is displayed, providing educational insights into the algorithm’s efficiency.

## Code Structure
SortingVisualizer Class:
Encapsulates the main logic of the visualizer including the GUI components, event handling, and sorting algorithm implementations.

## Sorting Algorithm Methods:
Each algorithm (Bubble, Selection, Insertion, Quick, Merge) is implemented with appropriate visualization updates.

## GUI Components:
Utilizes Tkinter’s Canvas, Scale, Button, and Text widgets to create an interactive interface.

## Contributing
Contributions are welcome! If you have ideas for new features or improvements, please open an issue or submit a pull request.
