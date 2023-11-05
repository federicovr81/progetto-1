from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        # Imposta lo sfondo iniziale nero
        Window.clearcolor = (0, 0, 0, 1)

        # Crea un layout fluttuante
        self.layout = FloatLayout(size=(300, 300))
        
        # Crea un pulsante
        self.button = Button(
            text='Ciao',
            size_hint=(.5, .1),
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        
        # Associa l'evento on_press del pulsante alla funzione on_button_press
        self.button.bind(on_press=self.on_button_press)
        
        # Aggiungi il pulsante al layout
        self.layout.add_widget(self.button)
        
        return self.layout

    def on_button_press(self, instance):
        # Cambia il colore dello sfondo in giallo
        Window.clearcolor = (1, 1, 0, 1)
        
        # Rimuove il pulsante
        self.layout.remove_widget(self.button)
        
        # Aggiunge un'etichetta con la scritta "Buona giornata"
        self.label = Label(
            text='Buona giornata',
            font_size='20sp',
            pos_hint={'center_x': .5, 'center_y': .5}
        )
        
        # Aggiungi l'etichetta al layout
        self.layout.add_widget(self.label)
        
        # Disegna un arcobaleno
        with self.layout.canvas:
            Color(1, 0, 0, 1)  # Rosso
            Rectangle(pos=(100, 100), size=(100, 50))
            Color(0, 1, 0, 1)  # Verde
            Rectangle(pos=(100, 150), size=(100, 50))
            Color(0, 0, 1, 1)  # Blu
            Rectangle(pos=(100, 200), size=(100, 50))

if __name__ == '__main__':
    MainApp().run()
