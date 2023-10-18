import curses
import time
import random

# Load words from parole.txt file
with open("parole.txt", "r") as f:
    words = f.readlines()


def get_next_word():
    while words:
        yield random.choice(words)


word_generator = get_next_word()
current_word = next(word_generator)

def get_new_word():
    try:
        return next(word_generator)
    except StopIteration:
        return "No more words"


def main(screen):
    # Setting this to True makes getch() non-blocking
    screen.nodelay(True)
    global current_word
    punteggio = 0
    duration = 100
    skips = 3
    for i in range(duration):
        pressed = screen.getch()
        if pressed == ord(" "):  # Check if space is pressed
            if skips > 0:
                skips -= 1
                current_word = get_new_word()
        elif pressed == ord("\n"):
            punteggio += 1
            current_word = get_new_word()
        elif pressed == ord("ù"):
            punteggio -= 1
            current_word = get_new_word()

        screen.clear()
        screen.addstr(0, 0, f"Parola: {current_word}")
        screen.addstr(1, 0, f"Tempo: {duration - i}s")
        screen.addstr(2, 0, f"Punteggio: {punteggio}")
        screen.addstr(3, 0, f"Skips: {skips}")
        screen.refresh()
        time.sleep(1)


curses.wrapper(main)
