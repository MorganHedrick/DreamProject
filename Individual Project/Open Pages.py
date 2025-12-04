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
from kivy.uix.carousel import Carousel
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.behaviors import DragBehavior
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Line
#Import for Debug Circles
from kivy.graphics import Ellipse
from kivy.config import Config


class StaticPage(FloatLayout):
    def __init__(self, img_left, img_right, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source=img_left, size_hint=(0.5, 1), pos_hint={'x': 0, 'y': 0}, allow_stretch=True, keep_ratio=True))
        self.add_widget(Image(source=img_right, size_hint=(0.5, 1), pos_hint={'x': 0.5, 'y': 0}, allow_stretch=True, keep_ratio=True))

class ExplosionPage(FloatLayout):
    def __init__(self, img_left, img_right, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source=img_left, size_hint=(0.5, 1), pos_hint={'x': 0, 'y': 0}, allow_stretch=True, keep_ratio=True))
        self.add_widget(Image(source=img_right, size_hint=(0.5, 1), pos_hint={'x': 0.5, 'y': 0}, allow_stretch=True, keep_ratio=True))
    def trigger_explosion(self):
        self.explosion = Image(source="InteractiveFeatures/Animated_Explosion.gif", size_hint=(1, 1.05), pos_hint={'x': 0, 'y': 0.1}, anim_delay=0, anim_loop=1)
        self.add_widget(self.explosion)
        self.explosion.anim_delay = 0.04

class CircuitPage(FloatLayout):
    def __init__(self, img_left, img_right, **kwargs):
        super().__init__(**kwargs)
        # Background page (LED off)
        self.add_widget(Image(source=img_left, size_hint=(0.5, 1), pos_hint={'x': 0, 'y': 0}, allow_stretch=True, keep_ratio=True))
        self.page_bg = Image(source=img_right, size_hint=(0.5, 1), pos_hint={'x': 0.5, 'y': 0}, allow_stretch=True, keep_ratio=True)
        self.page_bg.touch_disabled = True
        self.add_widget(self.page_bg)
        
        # Wire endpoints
        self.wire1_end1 = WireEnd(pos=(825,300), color=(1,0.5,0,0.8))
        self.wire1_end2 = WireEnd(pos=(975,400), color=(1,0.5,0,0.8))
        self.add_widget(self.wire1_end1)
        self.add_widget(self.wire1_end2)
        self.wire2_end1 = WireEnd(pos=(800,400), color=(0,0,1,0.8))
        self.wire2_end2 = WireEnd(pos=(950,500), color=(0,0,1,0.8))
        self.add_widget(self.wire2_end1)
        self.add_widget(self.wire2_end2)

        # Draw wires
        with self.canvas:
            # Orange wire
            Color(1, 0.5, 0)
            self.wire1_line = Line(points=[0, 0, 0, 0], width=2)
            # Blue wire
            Color(0, 0, 1)
            self.wire2_line = Line(points=[0, 0, 0, 0], width=2)
        # Define battery and LED positions
        self.battery_pos = (806, 259)
        self.battery_neg = (806, 306)
        self.led_pos = (1013, 460)
        self.led_neg = (962, 561)

        # Update wires and check circuit
        Clock.schedule_interval(self.update, 0.05)
    def update(self, dt):
        self.wire1_line.points = [self.wire1_end1.center_x, self.wire1_end1.center_y, self.wire1_end2.center_x, self.wire1_end2.center_y]
        self.wire2_line.points = [self.wire2_end1.center_x, self.wire2_end1.center_y, self.wire2_end2.center_x, self.wire2_end2.center_y]
        
        wire1_pos_wire2_neg = (self._is_near(self.wire1_end1.center, self.battery_pos) and
        self._is_near(self.wire1_end2.center, self.led_pos) and
            self._is_near(self.wire2_end1.center, self.battery_neg) and
            self._is_near(self.wire2_end2.center, self.led_neg))
        wire1_neg_wire2_pos = (self._is_near(self.wire1_end1.center, self.battery_neg) and
        self._is_near(self.wire1_end2.center, self.led_neg) and
        self._is_near(self.wire2_end1.center, self.battery_pos) and
        self._is_near(self.wire2_end2.center, self.led_pos))
        
        if wire1_neg_wire2_pos:
            self.page_bg.source = "InteractiveFeatures/Circuit_LED_On.png"
        elif wire1_pos_wire2_neg:
            self.page_bg.source = "InteractiveFeatures/Circuit_LED_On.png"
        else:
            self.page_bg.source = "StemDayPages/StemDay_page14.png"
            
    def _is_near(self, wire_center, target_pos, tolerance=30):
        wx, wy = wire_center
        tx, ty = target_pos
        return abs(wx-tx) < tolerance and abs (wy-ty)< tolerance

class WireEnd(DragBehavior, Widget):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (40, 40)
        with self.canvas:
            Color(*color)
            self.dot = Ellipse(pos=self.pos, size=self.size)
        self.drag_rectangle = (*self.pos, self.width, self.height)
        self.drag_timeout = 100000000000
        self.drag_distance = 0
        self.bind(pos=self._update_dot)

    def _update_dot(self, *args):
        self.dot.pos = self.pos
        self.drag_rectangle = (*self.pos, self.width, self.height)

class BridgePage(FloatLayout):
    def __init__(self, img_left, img_right, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source=img_left, size_hint=(0.5, 1), pos_hint={'x': 0, 'y': 0}, allow_stretch=True, keep_ratio=True))
        self.add_widget(Image(source=img_right, size_hint=(0.5, 1), pos_hint={'x': 0.5, 'y': 0}, allow_stretch=True, keep_ratio=True))

class ScalePage(FloatLayout):
    def __init__(self, img_left, img_right, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Image(source=img_left, size_hint=(0.5, 1), pos_hint={'x': 0, 'y': 0}, allow_stretch=True, keep_ratio=True))
        self.add_widget(Image(source=img_right, size_hint=(0.5, 1), pos_hint={'x': 0.5, 'y': 0}, allow_stretch=True, keep_ratio=True))

class BookApp(App):
    def build(self):
        return CircuitPage("StemDayPages/StemDay_page13.png", "StemDayPages/StemDay_page14.png")

class BookApp(App):
    def build(self):
        self.carousel = Carousel(direction='right')
        self.pages = []
        page_types = [("StemDayPages/StemDay_page1.png", "StemDayPages/StemDay_page2.png", "static"), ("StemDayPages/StemDay_page3.png", "StemDayPages/StemDay_page4.png", "static"), ("StemDayPages/StemDay_page5.png", "StemDayPages/StemDay_page6.png", "static"), ("StemDayPages/StemDay_page7.png", "StemDayPages/StemDay_page8.png", "static"), ("StemDayPages/StemDay_page9.png", "StemDayPages/StemDay_page10.png", "static"), ("StemDayPages/StemDay_page11.png", "StemDayPages/StemDay_page12.png", "explosion"), ("StemDayPages/StemDay_page13.png", "StemDayPages/StemDay_page14.png", "circuit"), ("StemDayPages/StemDay_page15.png", "StemDayPages/StemDay_page16.png", "bridge"), ("StemDayPages/StemDay_page17.png","StemDayPages/StemDay_page18.png", "scale"), ("StemDayPages/StemDay_page19.png", "StemDayPages/StemDay_page20.png", "static"), ("StemDayPages/StemDay_page21.png", "StemDayPages/StemDay_page22.png", "static")]
        for img_left, img_right, ptype in page_types:
            if ptype == "static":
                page = StaticPage(img_left, img_right)
            if ptype == "explosion":
                page = ExplosionPage(img_left, img_right)
            if ptype == "circuit":
                page = CircuitPage(img_left, img_right)
            if ptype == "bridge":
                page = BridgePage(img_left, img_right)
            if ptype == "scale":
                page = ScalePage(img_left, img_right)
            self.pages.append(page)
            self.carousel.add_widget(page)
        self.carousel.bind(index=self.on_slide_change)
        return self.carousel
    def on_slide_change(self, carousel, index):
        try:
            current_page = self.pages[index]
            if isinstance(current_page, ExplosionPage):
                current_page.trigger_explosion()
        except IndexError:
            pass


if __name__ == "__main__":
    BookApp().run()