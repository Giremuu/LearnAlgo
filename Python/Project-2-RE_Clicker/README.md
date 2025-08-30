### RE:Clicker – Mini Clicker RPG in Python  

A small project developed in Python with the Tkinter module as part of my Codedex journey.  
The goal was to create a project from scratch after completing the Python learning path on Codedex.  

---

## Features:  

- Graphical interface made with Tkinter  
- A player with nickname, XP, levels, and attack power  
- Three randomly chosen enemies with fixed stats and a sprite  
- "Attack" button → Deals damage (removes HP) to the enemy  
- Each defeated enemy grants XP to the player  
- Leveling up increases the player’s attack power  
- "Reset" button → Resets XP to 0 and allows choosing a new nickname  

---

## Tech Stack:  

- Python 3  
- Tkinter and random modules  

---

## Issues encountered:  

1) **Tkinter and keyboard shortcuts**: at first, the "Attack" button also worked with the Space key, which would crash the app if it was held down.  
   - Solution: force mouse click only  

2) **Sprite handling**: needed to zoom in on the images to make them visible at the right size  

3) **Player reset**: resetting XP to 0 and allowing nickname change required reworking the initialization logic  

---

## Possible improvements:

- Add sound effects or background music
- Item or upgrade system
- More enemies and animations
- Reward system

---

## Feel free to share feedback if you’d like (Or if you’re a slime fan like me..)
