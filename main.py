import time
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
from rich.progress import track
from rich.console import Console
def main():
for _ in track(range(20), description="Loading..."):
time.sleep(0.03)
while True:
Console().clear() # this will clear the screen
message = "[b]Egg Farm Inventory System[/b]\n" \
"-------------------------\n" \
"🌧 | 28°C | 89% RH"
print(Panel(message, expand=False))
choices = ["1", "2", "3", "4"]
print("[1] Add new batch")
print("[2] Add new sales")
print("[3] View Reports")
print("[4] Exit")
selected = Prompt.ask("SELECT", choices=choices, show_choices=False)
if selected == "4":
Console().clear()
print("[red]\nClosing the program... Goodbye!")
break
if __name__ == "__main__":
Console().clear()
main()
