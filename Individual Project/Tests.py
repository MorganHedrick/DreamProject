"""
Course Number: ENGR 13300
Semester: e.g. Spring 2025

Description:
    Replace this line with a description of your program.

Assignment Information:
    Assignment:     e.g. 7.2.1 Py1 Team 1 (for Python 1 Team task 1)
    Team ID:        ### - ## (e.g. LC1 - 01; for section LC1, team 01)
    Author:         Name, login@purdue.edu
    Date:           e.g. 01/23/2025

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

""" Write any import statements here (and delete this line)."""


from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class BookPage(FloatLayout):
    def __init__(self, page_number, **kwargs):
        super().__init__(**kwargs)
        self.page_number = page_number
        self.add_widget(Label(text=f"Page {page_number}", size_hint=(.2, .1), pos_hint={'x':.4, 'y':.9}))
        next_btn = Button(text = "Next Page", size_hint = (.2, .1), pos_hint={'x':.7, 'y':.05})
        next_btn.bind(on_press=self.next_page)
        self.add_widget(next_btn)

    def next_page(self, instance):
        self.clear_widgets()
        self.__init__(self.page_number+1)

class BookApp(App):
    def build(self):
        return BookPage(page_number=1)

BookApp().run()

def main():

if __name__ == "__main__":
    main()
