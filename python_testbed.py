import tkinter as tk
from tkinter import ttk
import time
from enum import Enum

class TimerState(Enum):
    IDLE = 1
    RUNNING = 2
    RESET = 3

class TickingTimer:
    def __init__(self, root, duration=10):
        self.root = root
        self.duration = duration
        self.state = TimerState.IDLE
        self.start_time = None
        self.tick_interval = 1.0
        self.min_interval = 0.1
        
        # GUI setup
        self.root.title("Ticking Timer")
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        ttk.Button(button_frame, text="Start", command=self.start_timer).pack(pady=5, fill=tk.BOTH, expand=True)
        ttk.Button(button_frame, text="Reset", command=self.reset_timer).pack(pady=5, fill=tk.BOTH, expand=True)
        ttk.Button(button_frame, text="Stop", command=self.stop_timer).pack(pady=5, fill=tk.BOTH, expand=True)

        for button in button_frame.winfo_children():
            button.bind(
                "<Configure>",
                lambda e, b=button: b.configure(font=("Arial", max(10, int(e.width / 10)))))  # Changed from config to configure
            self.label = ttk.Label(root, text="Ready", font=("Arial", 14))
        self.label.pack(pady=10)

        # Flashing background setup
        self.original_bg = self.root.cget("bg")
        self.flash_color = "#222222"
        self.flash_duration_ms = 35  # milliseconds
        self._flash_revert_after_id = None
        
    def start_timer(self):
        if self.state != TimerState.RUNNING:
            self.state = TimerState.RUNNING
            self.start_time = time.time()
            self.tick_interval = 1.0
            self.update()
    
    def reset_timer(self):
        self.state = TimerState.RESET
        self.start_time = time.time()
        self.tick_interval = 1.0
        self.label.config(text="Reset!")
        # Restore background in case a flash was active
        self._restore_bg_immediate()
        if self.state == TimerState.RESET:
            self.state = TimerState.RUNNING
            self.update()
    
    def stop_timer(self):
        self.state = TimerState.IDLE
        self.label.config(text="Ready")
        # Ensure background restored when stopping
        self._restore_bg_immediate()
    
    def _restore_bg_immediate(self):
        # Cancel any pending revert and restore immediately
        if self._flash_revert_after_id is not None:
            try:
                self.root.after_cancel(self._flash_revert_after_id)
            except Exception:
                pass
            self._flash_revert_after_id = None
        self.root.configure(bg=self.original_bg)
    
    def flash(self):
        # Cancel a pending revert so flashes don't overlap weirdly
        if self._flash_revert_after_id is not None:
            try:
                self.root.after_cancel(self._flash_revert_after_id)
            except Exception:
                pass
            self._flash_revert_after_id = None
        # Set dark background briefly and schedule restore
        self.root.configure(bg=self.flash_color)
        self._flash_revert_after_id = self.root.after(self.flash_duration_ms, self._restore_bg)
    
    def _restore_bg(self):
        self.root.configure(bg=self.original_bg)
        self._flash_revert_after_id = None
    
    def update(self):
        if self.state == TimerState.RUNNING:
            elapsed = time.time() - self.start_time
            
            if elapsed >= self.duration:
                self.state = TimerState.IDLE
                self.label.config(text="Timer expired!")
                return
            
            # Decrease interval as time progresses (increasing frequency)
            self.tick_interval = max(self.min_interval, 1.0 - (elapsed / self.duration) * 0.9)
            self.label.config(text=f"Tick! ({elapsed:.1f}s)")
            print(f"Tick! Elapsed: {elapsed:.2f}s, Interval: {self.tick_interval:.2f}s")
            # Non-blocking quick flash to indicate tick
            self.flash()
            
            self.root.after(int(self.tick_interval * 1000), self.update)

if __name__ == "__main__":
    root = tk.Tk()
    timer = TickingTimer(root, duration=10)
    root.mainloop()