from tkinter import ttk, constants, StringVar

from services.user_service import user_service, WorkoutGoalError


class UpdateWorkoutGoalView:
    """Näkymä, joka vastaa treenin tavoitteen päivittämisestä sovelluksessa."""

    def __init__(self, root, handle_show_main_view):
        """Luokka konstruktori, joka luo uuden treenin luontinäkymän.

        Args:
            root (tkinter.Tk): Tkinter-elementti, joka toimii näkymän juurena.
            handle_show_main_view (callable): Käsittelijäfunktio, joka näyttää päänäkymän.
        """
        self._root = root
        self._current_user = user_service.current_user()
        self._workout_goal = self._current_user.weekly_training_goal_in_minutes
        self._handle_show_main_view = handle_show_main_view
        self._frame = None
        self._workout_goal_entry = None
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän käyttöliittymässä."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa näkymän käyttöliittymästä."""
        self._frame.destroy()

    def _handle_update_goal(self):
        new_workout_goal_value = self._workout_goal_entry.get()
        try:
            user_service.update_workout_goal(
                new_workout_goal_value)
            self._handle_show_main_view()
        except WorkoutGoalError as error:
            self._show_error_message(error.message)

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _handle_cancel(self):
        self._handle_show_main_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._frame, text="Update Workout Goal", font=("", 12, "bold"))

        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="red"
        )

        new_workout_goal_label = ttk.Label(
            master=self._frame, text="New Workout Goal")
        new_workout_goal_entry = ttk.Entry(master=self._frame)

        new_workout_goal_entry.insert(0, str(self._workout_goal))

        self._workout_goal_entry = new_workout_goal_entry

        update_button = ttk.Button(
            master=self._frame, text="Update", command=self._handle_update_goal)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._handle_cancel)

        header_label.grid(columnspan=2, sticky=constants.W,
                          padx=(10, 0), pady=5)

        self._error_label.grid(
            row=0, column=1, sticky=constants.W, padx=(10, 0), pady=5)

        new_workout_goal_label.grid(row=1, column=0, padx=(10, 0), pady=5)
        new_workout_goal_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        update_button.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)
        cancel_button.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
