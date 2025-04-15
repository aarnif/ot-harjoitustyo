from tkinter import ttk, constants

from services.user_service import user_service
from services.workout_service import workout_service


class MainView:
    def __init__(self, root, handle_show_login, handle_show_update_workout_goal):
        self._root = root
        self._current_user = user_service.current_user()
        self._workout_goal = self._current_user.weekly_training_goal_in_minutes
        self._total_training_time = workout_service.get_weeks_workout_total(
            self._current_user.username)
        self._handle_show_login = handle_show_login
        self._handle_show_update_workout_goal = handle_show_update_workout_goal
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout_user(self):
        user_service.logout_user()
        self._handle_show_login()

    def _handle_update_goal(self):
        self._handle_show_update_workout_goal()

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    # generoitu koodi alkaa
    def _calculate_progress_color_and_message(self):
        if self._workout_goal == 0:
            return "orange", "Set a weekly workout goal to track your progress!"

        percentage = (self._total_training_time / self._workout_goal) * 100
        percentage = min(100.0, percentage)

        if percentage < 25:
            color = "red"
            message = "Just getting started! Keep up the good work!"
        elif percentage < 50:
            color = "red"
            message = "Making progress! Keep pushing forward!"
        elif percentage < 75:
            color = "orange"
            message = "You're doing great! More than halfway there!"
        elif percentage < 100:
            color = "orange"
            message = "Almost there! Final push to reach your goal!"
        else:
            color = "green"
            message = "Goal achieved! Outstanding work this week!"

        return color, message
    # generoitu koodi päättyy

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._frame, text=f"Hi, {self._current_user.username}!", font=("", 11, "bold"))

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_logout_user)

        header_label.grid(columnspan=2, sticky=constants.W,
                          padx=(10, 0), pady=5)

        logout_button.grid(row=0, column=3, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        # generoitu koodi alkaa
        progress_title = ttk.Label(
            master=self._frame,
            text="Weekly Training Progress",
            font=('', 12, 'bold'))

        progress_title.grid(row=1, column=0, columnspan=4, sticky=constants.W,
                            padx=10, pady=(10, 5))

        progress_label = ttk.Label(
            master=self._frame,
            text=f"Current Progress: {self._total_training_time} minutes",
            font=("", 10))

        progress_label.grid(
            row=2, column=0, sticky=constants.W, padx=10, pady=5)

        goal_label = ttk.Label(
            master=self._frame,
            text=f"Weekly Goal: {self._workout_goal} minutes",
            font=("", 10))

        goal_label.grid(row=3, column=0, sticky=constants.W, padx=10, pady=5)

        update_button = ttk.Button(
            master=self._frame, text="Update", command=self._handle_update_goal)

        update_button.grid(
            row=3, column=3, sticky=constants.E, padx=10, pady=5)

        color, message = self._calculate_progress_color_and_message()

        percentage_label = ttk.Label(
            master=self._frame,
            text=f"{message}",
            font=("", 10),
            foreground=color)

        percentage_label.grid(
            row=4, column=0, sticky=constants.W, padx=10, pady=5)
        # generoitu koodi päättyy

        self._frame.grid_columnconfigure(1, weight=1, minsize=100)
