from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner


class MyApp(App):
    def build(self):

        def on_spinner_click(instance, text):
            if instance.text == 'type':
                print('instance=', instance, 'value = ', text)

        layout = FloatLayout(size_hint_y=None,
                             height=1000,
                             )

        scrollview = ScrollView(bar_color=(.5, .1, .9, 1),
                                bar_width=20,
                                # bar_inactive_color=(.5, .1, .19, 1),
                                bar_margin=10,
                                bar_pos_y='right',
                                scroll_type=['content', 'bars'],
                                smooth_scroll_end=0,
                                scroll_timeout=100,
                                scroll_distance=20)
        spinner = Spinner(text='spinner',
                          values=('home', 'menu', 'option', 'type'),
                          size_hint=(.3, None),
                          height=100,
                          pos_hint={'center_x': .756, 'center_y': .8}
                          )
        spinner.bind(text=on_spinner_click)

        self.label = Label(
            text='label',
            size_hint=(1, None),
            height=60,
            pos_hint={'center_x': .5, 'center_y': .97}
        )

        self.textinput = TextInput(hint_text='enter name',
                                   size_hint=(.3, None),
                                   height=100,
                                   pos_hint={'center_x': .152, 'center_y': .8}
                                   )

        button1 = Button(text='Enter',
                         background_normal='enter2.png',
                         size_hint=(.3, None),
                         height=100,
                         pos_hint={'center_x': .454, 'center_y': .8},
                         )

        button1.bind(on_press=self.on_click)

        #  dropdown
        dropdown = DropDown()
        for i in range(1, 4):
            self.option = Button(text=f'option{i}',
                                 size_hint_y=None,
                                 height=40
                                 )

            self.option.bind(on_release=lambda option: dropdown.select(option.text))
            self.option.bind(on_release=lambda option: self.on_option_select(option.text))
            dropdown.add_widget(self.option)

        # for dynamically update dropdown option you have to declare that button separately
        self.option4 = Button(text='option4',
                              size_hint_y=None,
                              height=40
                              )
        # for closing dropdown after select this option
        self.option4.bind(on_release=lambda option: dropdown.select(self.option4.text))
        dropdown.add_widget(self.option4)

        main_trigger = Button(text='dropdown trigger',
                              size_hint=(.3, None),
                              height=100,
                              text_size=(70, None),
                              pos_hint={'center_x': .152, 'center_y': .698}
                              )
        main_trigger.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(main_trigger, 'text', x))
        layout.add_widget(main_trigger)

        layout.add_widget(self.label)
        layout.add_widget(self.textinput)
        layout.add_widget(button1)
        layout.add_widget(spinner)

        scrollview.add_widget(layout)

        return scrollview

    def on_option_select(self, value):
        self.label.text = value
        print(value)

    def on_click(self, instance):
        self.label.text = self.textinput.text
        self.option4.text = self.textinput.text  # dynamically update dropdown option text
        # self.option4.text = self.label.text  # also dynamically update by this statement
        self.textinput.text = ''


MyApp().run()
