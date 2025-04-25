from tkinter import ttk, constants, StringVar

from services.user_service import user_service
from services.workout_service import workout_service


class ConfirmDeleteView:
    def __init__(self, root, workout_id, handle_show_update_workout, handle_show_workouts_view):
        self._root = root
        self._current_user = user_service.current_user()
        self._selected_workout = workout_service.get_workout_by_id(workout_id)
        self._handle_show_update_workout = handle_show_update_workout
        self._handle_show_workouts_view = handle_show_workouts_view
        self._frame = None
        self._workout_type_entry = None
        self._workout_duration_entry = None
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _handle_cancel(self):
        self._handle_show_update_workout(self._selected_workout.id)

    def _handle_delete_workout(self):
        if workout_service.delete_workout(self._selected_workout.id):
            self._handle_show_workouts_view()
        else:
            self._show_error_message("Failed to delete workout.")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._frame, text="Delete Workout?", font=("", 12, "bold"))

        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="red"
        )

        delete_button = ttk.Button(
            master=self._frame, text="Delete", command=self._handle_delete_workout)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._handle_cancel)

        header_label.grid(columnspan=2, sticky=constants.W,
                          padx=(10, 0), pady=5)

        self._error_label.grid(
            row=0, column=1, sticky=constants.W, padx=(10, 0), pady=5)

        delete_button.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)
        cancel_button.grid(row=5, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
