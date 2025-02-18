import tkinter as tk
from tkinter import messagebox
import time

class TowerOfHanoiGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tower of Hanoi")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')

        self.num_disks = 3
        self.towers = [[], [], []]
        self.selected_tower = None
        self.moves = 0
        self.solving = False

        # Create frames
        self.top_frame = tk.Frame(root, bg='#f0f0f0')
        self.top_frame.pack(pady=10)

        self.canvas_frame = tk.Frame(root, bg='#f0f0f0')
        self.canvas_frame.pack(expand=True, fill='both', padx=20)

        self.bottom_frame = tk.Frame(root, bg='#f0f0f0')
        self.bottom_frame.pack(pady=10)

        # Create canvas
        self.canvas = tk.Canvas(self.canvas_frame, width=700, height=400, bg='white')
        self.canvas.pack(expand=True)

        # Create controls
        tk.Label(self.top_frame, text="Number of disks:", bg='#f0f0f0').pack(side=tk.LEFT, padx=5)
        self.disk_var = tk.StringVar(value='3')
        self.disk_entry = tk.Spinbox(self.top_frame, from_=3, to=8, width=5, textvariable=self.disk_var)
        self.disk_entry.pack(side=tk.LEFT, padx=5)

        self.new_game_btn = tk.Button(self.top_frame, text="New Game", command=self.new_game)
        self.new_game_btn.pack(side=tk.LEFT, padx=5)

        self.solve_btn = tk.Button(self.top_frame, text="Show Solution", command=self.solve)
        self.solve_btn.pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_label = tk.Label(self.bottom_frame, text="Moves: 0", bg='#f0f0f0')
        self.status_label.pack()

        # Bind canvas clicks
        self.canvas.bind('<Button-1>', self.on_tower_click)

        # Initialize game
        self.new_game()

    def draw_towers(self):
        self.canvas.delete('all')
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        # Draw poles
        pole_width = 20
        pole_height = height * 0.6
        base_y = height * 0.8
        spacing = width / 4

        for i in range(3):
            x = spacing * (i + 1)
            # Draw base
            self.canvas.create_rectangle(x - 60, base_y, x + 60, base_y + 20, fill='brown')
            # Draw pole
            self.canvas.create_rectangle(x - pole_width/2, base_y - pole_height,
                                      x + pole_width/2, base_y, fill='brown')

        # Draw disks
        max_disk_width = 100
        disk_height = 30
        for i, tower in enumerate(self.towers):
            x = spacing * (i + 1)
            for j, disk in enumerate(tower):
                disk_width = max_disk_width * (disk / self.num_disks)
                y = base_y - (j + 1) * disk_height
                color = f'#{disk*2:02x}8080'
                self.canvas.create_rectangle(x - disk_width/2, y,
                                          x + disk_width/2, y + disk_height - 2,
                                          fill=color, outline='black')

    def on_tower_click(self, event):
        if self.solving:
            return

        width = self.canvas.winfo_width()
        spacing = width / 4

        # Determine which tower was clicked
        tower_clicked = None
        for i in range(3):
            x = spacing * (i + 1)
            if abs(event.x - x) < 60:
                tower_clicked = i
                break

        if tower_clicked is not None:
            if self.selected_tower is None:
                if self.towers[tower_clicked]:  # If tower has disks
                    self.selected_tower = tower_clicked
                    self.status_label.config(text=f"Selected tower {chr(65+tower_clicked)}")
            else:
                source = self.selected_tower
                target = tower_clicked
                if self.move_disk(source, target):
                    self.moves += 1
                    self.status_label.config(text=f"Moves: {self.moves}")
                    if self.check_win():
                        messagebox.showinfo("Congratulations!",
                                          f"You solved the puzzle in {self.moves} moves!\n"
                                          f"Minimum possible moves: {2**self.num_disks - 1}")
                self.selected_tower = None

        self.draw_towers()

    def move_disk(self, source, target):
        if not self.towers[source]:
            return False
        
        if self.towers[target] and self.towers[source][-1] > self.towers[target][-1]:
            return False
            
        disk = self.towers[source].pop()
        self.towers[target].append(disk)
        return True

    def check_win(self):
        return len(self.towers[2]) == self.num_disks

    def new_game(self):
        try:
            self.num_disks = int(self.disk_var.get())
            if not 3 <= self.num_disks <= 8:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Please enter a number between 3 and 8")
            return

        self.towers = [[], [], []]
        self.towers[0] = list(range(self.num_disks, 0, -1))
        self.selected_tower = None
        self.moves = 0
        self.solving = False
        self.status_label.config(text="Moves: 0")
        self.draw_towers()

    def solve(self):
        self.solving = True
        self.new_game()
        self.solve_hanoi(self.num_disks, 0, 1, 2)
        self.solving = False

    def solve_hanoi(self, n, source, auxiliary, target):
        if n == 1:
            self.move_disk(source, target)
            self.draw_towers()
            self.root.update()
            time.sleep(0.5)
            return

        self.solve_hanoi(n-1, source, target, auxiliary)
        self.move_disk(source, target)
        self.draw_towers()
        self.root.update()
        time.sleep(0.5)
        self.solve_hanoi(n-1, auxiliary, source, target)

def main():
    root = tk.Tk()
    app = TowerOfHanoiGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()