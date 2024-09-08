username_helper = """

FloatLayout:

    MDTopAppBar:
        title: "My App"
        right_action_items: [["account-circle-outline", lambda x: app.on_account()]]
        elevation: 3
        pos_hint: {"top": 1}  # Position the app bar at the top
        size_hint_y: None
        height: "56dp" 

    MDRaisedButton:
        text: "Start"
        style: "elevated"
        icon: "plus"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release:app.on_button_press()
            
"""