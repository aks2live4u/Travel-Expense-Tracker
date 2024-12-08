#pylint:disable= 'invalid syntax (<unknown>, line 391)'
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, NumericProperty

# Global Variables
people = {}
expenses = []

# KV Language Code
KV = '''
ScreenManager:
    MainScreen:
    PeopleScreen:
    ExpenseScreen:
    DetailsScreen:

<MainScreen>:
    name: "main"
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 20
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Expense Tracker"
            font_size: "50sp"
            bold: True
            color: (0, 1, 0, 1)
            size_hint_y: 0.2
        Label:
            id: total_expense
            text: "Total Expenses: ₹0"
            font_size: "20sp"
            color: (0, 1, 0, 1)
        Button:
            text: "Go to People"
            background_color: (0, 0.8, 0, 1)
            size_hint_y: 0.1
            on_press: root.manager.current = "people"
        Button:
            text: "Go to Expenses"
            background_color: (0, 0.8, 0, 1)
            size_hint_y: 0.1
            on_press: root.manager.current = "expenses"
        Button:
            text: "Go to Details"
            background_color: (0, 0.8, 0, 1)
            size_hint_y: 0.1
            on_press: root.manager.current = "details"
        Button:
            text: "Reset"
            background_color: (0.8, 0, 0, 1)
            size_hint_y: 0.1
            on_press: app.show_reset_warning()

<PeopleScreen>:
    name: "people"
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Add People"
            font_size: "30sp"
            color: (0, 1, 0, 1)
        TextInput:
            id: person_name
            hint_text: "Enter person's name"
            size_hint_y: 0.2
            background_color: (0.2, 0.8, 0.2, 1)
            foreground_color: (0, 0, 0, 1)  # Text color
        Button:
            text: "Add Person"
            size_hint_y: 0.2
            background_color: (0, 0.8, 0, 1)
            on_press: app.add_person(person_name.text)
        ScrollView:
            size_hint_y: 0.4
            BoxLayout:
                id: people_list
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1
                    Line:
                        width: 2
                        rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "Back to Main"
            size_hint_y: 0.2
            background_color: (0, 0.8, 0, 1)
            on_press: root.manager.current = "main"

<ExpenseScreen>:
    name: "expenses"
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Add Expenses"
            font_size: "30sp"
            color: (0, 1, 0, 1)
        Spinner:
            id: person_selector
            text: "Select a person"
            size_hint_y: 0.2
            background_color: (0.2, 0.8, 0.2, 1)
        TextInput:
            id: expense_amount
            hint_text: "Enter amount"
            size_hint_y: 0.2
            background_color: (0.2, 0.8, 0.2, 1)
        TextInput:
            id: expense_detail
            hint_text: "Enter expense detail"
            size_hint_y: 0.2
            background_color: (0.2, 0.8, 0.2, 1)
        Button:
            text: "Add Expense"
            size_hint_y: 0.2
            background_color: (0, 0.8, 0, 1)
            on_press: app.add_expense(person_selector.text, expense_amount.text, expense_detail.text)
        Button:
            text: "Back to Main"
            size_hint_y: 0.2
            background_color: (0, 0.8, 0, 1)
            on_press: root.manager.current = "main"

<DetailsScreen>:
    name: "details"
    BoxLayout:
        orientation: 'vertical'
        padding: 10
        spacing: 10
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        Label:
            text: "Expense Details"
            font_size: "30sp"
            color: (0, 1, 0, 1)
        ScrollView:
            size_hint_y: 0.8
            BoxLayout:
                id: expense_list
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                canvas.before:
                    Color:
                        rgba: 0, 1, 0, 1
                    Line:
                        width: 2
                        rectangle: self.x, self.y, self.width, self.height
        Button:
            text: "Back to Main"
            size_hint_y: 0.2
            background_color: (0, 0.8, 0, 1)
            on_press: root.manager.current = "main"
'''

class MainScreen(Screen):
    pass

class PeopleScreen(Screen):
    pass

class ExpenseScreen(Screen):
    pass

class DetailsScreen(Screen):
    pass

class ExpenseTrackerApp(App):
    def build(self):
        return Builder.load_string(KV)

    def show_reset_warning(self):
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text="Are you sure you want to reset everything?"))
        button_layout = BoxLayout(size_hint_y=0.2)
        button_layout.add_widget(Button(text="Proceed", on_press=lambda x: self.reset_data(popup)))
        button_layout.add_widget(Button(text="Cancel", on_press=lambda x: popup.dismiss()))
        content.add_widget(button_layout)

        popup = Popup(title="Warning", content=content, size_hint=(0.8, 0.4))
        popup.open()

    def reset_data(self, popup):
        global people, expenses
        people = {}
        expenses = []
        self.update_total_expenses()  # Recalculate total expenses
        self.root.get_screen('people').ids.people_list.clear_widgets()
        self.root.get_screen('details').ids.expense_list.clear_widgets()
        self.root.get_screen('people').ids.person_name.text = ""  # Clear the person name input field
        self.root.get_screen('expenses').ids.person_selector.text = "Select a person"  # Clear the dropdown
        self.root.get_screen('expenses').ids.expense_amount.text = ""  # Clear amount input
        self.root.get_screen('expenses').ids.expense_detail.text = ""  # Clear expense detail input
        popup.dismiss()  # Dismiss the reset warning popup
        self.root.current = "main"  # Go back to the main screen

    def add_person(self, name):
        if name:
            if name not in people:
                people[name] = {"spent": 0, "owed": 0}
                self.update_people_display()
                self.update_spinner()
            self.root.get_screen('people').ids.person_name.text = ""  # Clear input field

    def update_spinner(self):
        spinner = self.root.get_screen('expenses').ids.person_selector
        spinner.values = list(people.keys())

    def add_expense(self, person, amount, detail):
        if person != "Select a person" and amount.isdigit():
            amount = float(amount)  # Convert to float to support decimals
            expenses.append({"person": person, "amount": amount, "detail": detail})
            people[person]["spent"] += amount  # Add the expense to the person's total spent
            self.update_total_expenses()  # Recalculate the total expenses after adding the new expense
            self.update_people_display()  # Update the people list to show the new balances
            self.update_expense_list()  # Update the expenses list in the details screen
            self.root.get_screen('expenses').ids.expense_amount.text = ""  # Clear input field for amount
            self.root.get_screen('expenses').ids.expense_detail.text = ""  # Clear input field for detail

    def update_total_expenses(self):
        total_expenses = sum(expense["amount"] for expense in expenses)
        self.root.get_screen('main').ids.total_expense.text = f"Total Expenses: ₹{total_expenses:.2f}"

        # Update total owed for each person
        num_people = len(people)
        if num_people > 0:
            total_owed = total_expenses / num_people
            for person in people:
                people[person]["owed"] = total_owed

    def update_people_display(self):
        # Clear existing widgets
        people_list = self.root.get_screen('people').ids.people_list
        people_list.clear_widgets()

        # Add table headings for People tab
        header = BoxLayout(size_hint_y=None, height=40)
        header.add_widget(Label(text="Name", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Spent", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Owed", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Balance", bold=True, color=(0, 1, 0, 1)))
        people_list.add_widget(header)

        # Add updated information
        for person, data in people.items():
            total_spent = data["spent"]
            total_owed = data["owed"]
            balance = total_owed - total_spent
            row = BoxLayout(size_hint_y=None, height=40)
            row.add_widget(Label(text=person, color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{total_spent:.2f}", color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{total_owed:.2f}", color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{balance:.2f}", color=(0, 1, 0, 1)))
            people_list.add_widget(row)

    def update_expense_list(self):
        expense_list = self.root.get_screen('details').ids.expense_list
        expense_list.clear_widgets()

        # Add table headings for Expense Details tab
        header = BoxLayout(size_hint_y=None, height=40)
        header.add_widget(Label(text="Person", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Amount", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Detail", bold=True, color=(0, 1, 0, 1)))
        expense_list.add_widget(header)

        # Add updated expense entries
        for expense in expenses:
            row = BoxLayout(size_hint_y=None, height=40)
            row.add_widget(Label(text=expense["person"], color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{expense['amount']:.2f}", color=(0, 1, 0, 1)))
            row.add_widget(Label(text=expense["detail"], color=(0, 1, 0, 1)))
            expense_list.add_widget(row)

    def update_total_expenses(self):
        total_expenses = sum(expense["amount"] for expense in expenses)
        self.root.get_screen('main').ids.total_expense.text = f"Total Expenses: ₹{total_expenses:.2f}"

        # Update total owed for each person
        num_people = len(people)
        if num_people > 0:
            total_owed = total_expenses / num_people
            for person in people:
                people[person]["owed"] = total_owed

    def update_people_display(self):
        # Clear existing widgets
        people_list = self.root.get_screen('people').ids.people_list
        people_list.clear_widgets()

        # Add table headings for People tab
        header = BoxLayout(size_hint_y=None, height=40)
        header.add_widget(Label(text="Name", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Spent", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Owed", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Balance", bold=True, color=(0, 1, 0, 1)))
        people_list.add_widget(header)

        # Add updated information
        for person, data in people.items():
            total_spent = data["spent"]
            total_owed = data["owed"]
            balance = total_owed - total_spent
            row = BoxLayout(size_hint_y=None, height=40)
            row.add_widget(Label(text=person, color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{total_spent:.2f}", color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{total_owed:.2f}", color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{balance:.2f}", color=(0, 1, 0, 1)))
            people_list.add_widget(row)

    def update_expense_list(self):
        expense_list = self.root.get_screen('details').ids.expense_list
        expense_list.clear_widgets()

        # Add table headings for Expense Details tab
        header = BoxLayout(size_hint_y=None, height=40)
        header.add_widget(Label(text="Person", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Amount", bold=True, color=(0, 1, 0, 1)))
        header.add_widget(Label(text="Detail", bold=True, color=(0, 1, 0, 1)))
        expense_list.add_widget(header)

        # Add updated expense entries
        for expense in expenses:
            row = BoxLayout(size_hint_y=None, height=40)
            row.add_widget(Label(text=expense["person"], color=(0, 1, 0, 1)))
            row.add_widget(Label(text=f"₹{expense['amount']:.2f}", color=(0, 1, 0, 1)))
            row.add_widget(Label(text=expense["detail"], color=(0, 1, 0, 1)))
            expense_list.add_widget(row)

    def reset_data(self, popup):
        global people, expenses
        people = {}
        expenses = []
        self.update_total_expenses()  # Recalculate total expenses
        self.root.get_screen('people').ids.people_list.clear_widgets()
        self.root.get_screen('details').ids.expense_list.clear_widgets()
        self.root.get_screen('people').ids.person_name.text = ""  # Clear the person name input field
        self.root.get_screen('expenses').ids.person_selector.text = "Select a person"  # Clear the dropdown
        self.root.get_screen('expenses').ids.expense_amount.text = ""  # Clear amount input
        self.root.get_screen('expenses').ids.expense_detail.text = ""  # Clear expense detail input
        popup.dismiss()  # Dismiss the reset warning popup
        self.root.current = "main"  # Go back to the main screen

    def show_reset_warning(self):
        content = BoxLayout(orientation='vertical', spacing=10)
        content.add_widget(Label(text="Are you sure you want to reset everything?"))
        button_layout = BoxLayout(size_hint_y=0.2)
        button_layout.add_widget(Button(text="Proceed", on_press=lambda x: self.reset_data(popup)))
        button_layout.add_widget(Button(text="Cancel", on_press=lambda x: popup.dismiss()))
        content.add_widget(button_layout)

        popup = Popup(title="Warning", content=content, size_hint=(0.8, 0.4))
        popup.open()

if __name__ == '__main__':
    ExpenseTrackerApp().run()