import tkinter as tk
from tkinter import messagebox
import random

class SortingVisualizer:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Algorithm Visualizer")
        self.screen_width = self.master.winfo_screenwidth()
        self.screen_height = self.master.winfo_screenheight()
        self.width = int(self.screen_width * 0.8)  # 80% of the screen width
        self.height = int(self.screen_height * .7)  # 70% of the screen height
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)  # Expand canvas to fill window
        
        self.numbers = []  # List of numbers to be sorted
        self.num_count = tk.IntVar(value=100)  # Default number of numbers
        self.shuffle_numbers()  # Initialize and shuffle numbers
        
        self.bar_width = self.width / self.num_count.get()
        self.bars = []
        self.draw_numbers()
        
        # Default delay time in milliseconds
        self.delay = tk.DoubleVar(value=1)
        
        # Create speed control slider
        self.speed_scale = tk.Scale(self.master, from_=1.0, to=100.0, length=int(self.width*0.7), orient=tk.HORIZONTAL,
                                    variable=self.delay, command=self.update_delay)
        self.speed_scale.pack(pady=10, padx=int(self.width*0.15))

        # Create buttons frame
        self.btn_frame = tk.Frame(self.master)
        self.btn_frame.pack(expand=True, fill=tk.BOTH, padx=int(self.width*0.1))

        # Create buttons
        tk.Button(self.btn_frame, text="Shuffle", command=self.shuffle_numbers).pack(side=tk.LEFT, padx=10)
        tk.Label(self.btn_frame, text="Number of Elements:").pack(side=tk.LEFT, padx=10)
        self.num_count_entry = tk.Entry(self.btn_frame, textvariable=self.num_count, width=10)
        self.num_count_entry.pack(side=tk.LEFT, padx=10)
        tk.Button(self.btn_frame, text="Update Numbers", command=self.update_numbers).pack(side=tk.LEFT, padx=10)
        
        # Create sorting algorithm buttons
        tk.Button(self.btn_frame, text="Bubble Sort", command=lambda: self.sort_algorithm(self._bubble_sort)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.btn_frame, text="Selection Sort", command=lambda: self.sort_algorithm(self._selection_sort)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.btn_frame, text="Insertion Sort", command=lambda: self.sort_algorithm(self._insertion_sort)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.btn_frame, text="Quick Sort", command=lambda: self.sort_algorithm(self._quick_sort, 0, len(self.numbers) - 1)).pack(side=tk.LEFT, padx=10)
        tk.Button(self.btn_frame, text="Merge Sort", command=lambda: self.sort_algorithm(self._merge_sort, 0, len(self.numbers) - 1)).pack(side=tk.LEFT, padx=10)
        
        # Create text box for Big O notation
        self.big_o_box = tk.Text(self.master, width=40, height=10, wrap=tk.WORD)
        self.big_o_box.pack(pady=20, padx=int(self.width*0.1))

    def draw_numbers(self):
        self.canvas.delete("numbers")  # Clear previous numbers
        self.bars = []
        for i, num in enumerate(self.numbers):
            x0 = i * self.bar_width
            y0 = self.height
            x1 = (i + 1) * self.bar_width
            y1 = self.height - (num * (self.height / max(self.numbers)))
            bar = self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue", tags="numbers")
            self.bars.append(bar)
    
    def update_bars(self):
        for i, num in enumerate(self.numbers):
            x0 = i * self.bar_width
            y0 = self.height
            x1 = (i + 1) * self.bar_width
            y1 = self.height - (num * (self.height / max(self.numbers)))
            self.canvas.coords(self.bars[i], x0, y0, x1, y1)
    
    def update_delay(self, value):
        # Update delay time based on slider value
        self.delay.set(float(value))
    
    def shuffle_numbers(self):
        self.numbers = [random.randint(1, 100) for _ in range(self.num_count.get())]
        self.bar_width = self.width / self.num_count.get()
        self.draw_numbers()

    def update_numbers(self):
        try:
            new_count = self.num_count.get()
            if new_count < 1 or new_count > 1000:
                messagebox.showerror("Error", "Please enter a number between 1 and 1000.")
                return
            self.shuffle_numbers()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def sort_algorithm(self, algorithm, *args):
        algorithm(*args)
        self.update_bars()
        self.display_big_o(algorithm)

    def display_big_o(self, algorithm):
        if algorithm == self._bubble_sort:
            big_o = "O(n^2) - Bubble Sort"
        elif algorithm == self._selection_sort:
            big_o = "O(n^2) - Selection Sort"
        elif algorithm == self._insertion_sort:
            big_o = "O(n^2) - Insertion Sort"
        elif algorithm == self._quick_sort:
            big_o = "O(n log n) - Quick Sort"
        elif algorithm == self._merge_sort:
            big_o = "O(n log n) - Merge Sort"
        else:
            big_o = "Unknown"
        
        self.big_o_box.delete(1.0, tk.END)
        self.big_o_box.insert(tk.END, big_o)

    def _bubble_sort(self):
        n = len(self.numbers)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.numbers[j] > self.numbers[j+1]:
                    self.numbers[j], self.numbers[j+1] = self.numbers[j+1], self.numbers[j]
                    self.update_bars()
                    self.master.update()
                    self.master.after(int(self.delay.get()))  # Use delay set by the slider

    def _selection_sort(self):
        n = len(self.numbers)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if self.numbers[j] < self.numbers[min_idx]:
                    min_idx = j
            self.numbers[i], self.numbers[min_idx] = self.numbers[min_idx], self.numbers[i]
            self.update_bars()
            self.master.update()
            self.master.after(int(self.delay.get()))  # Use delay set by the slider

    def _insertion_sort(self):
        n = len(self.numbers)
        for i in range(1, n):
            key = self.numbers[i]
            j = i - 1
            while j >= 0 and self.numbers[j] > key:
                self.numbers[j + 1] = self.numbers[j]
                j -= 1
            self.numbers[j + 1] = key
            self.update_bars()
            self.master.update()
            self.master.after(int(self.delay.get()))  # Use delay set by the slider

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def _partition(self, low, high):
        pivot = self.numbers[high]
        i = low - 1
        for j in range(low, high):
            if self.numbers[j] <= pivot:
                i += 1
                self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]
                self.update_bars()
                self.master.update()
                self.master.after(int(self.delay.get()))
        self.numbers[i + 1], self.numbers[high] = self.numbers[high], self.numbers[i + 1]
        return i + 1

    def _merge_sort(self, l, r):
        if l < r:
            mid = (l + r) // 2
            self._merge_sort(l, mid)
            self._merge_sort(mid + 1, r)
            self._merge(l, mid, r)

    def _merge(self, l, mid, r):
        temp = []
        i = l
        j = mid + 1
        
        while i <= mid and j <= r:
            if self.numbers[i] <= self.numbers[j]:
                temp.append(self.numbers[i])
                i += 1
            else:
                temp.append(self.numbers[j])
                j += 1
        
        while i <= mid:
            temp.append(self.numbers[i])
            i += 1
        
        while j <= r:
            temp.append(self.numbers[j])
            j += 1
        
        for k in range(len(temp)):
            self.numbers[l + k] = temp[k]
        
        self.update_bars()
        self.master.update()
        self.master.after(int(self.delay.get()))

def main():
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
