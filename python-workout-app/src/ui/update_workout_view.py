from tkinter import ttk, constants, StringVar
from entities.workout import Workout

from services.user_service import user_service
from services.workout_service import workout_service, WorkOutDurationError


class UpdateWorkoutView:
    """Näkymä, joka vastaa treenin muokkaamisesta ja sen poistamisesta sovelluksesta."""

    def __init__(self, root, workout_id, handle_show_workouts_view, handle_show_confirm_delete_view):
        """Luokka konstruktori, joka luo uuden treenin luontinäkymän.

        Args:
            root (tkinter.Tk): Tkinter-elementti, joka toimii näkymän juurena.
            workout_id (int): Yksittäisen treenin id.
            handle_show_workouts_view (callable): Käsittelijäfunktio, joka näyttää viikon treenien näkymän.
            handle_show_confirm_delete_view (callable): Käsittelijäfunktio, joka näyttää treenin poiston vahvistusnäkymän.
        """
        self._root = root
        self._current_user = user_service.current_user()
        self._selected_workout = workout_service.get_workout_by_id(workout_id)
        self._handle_show_workouts_view = handle_show_workouts_view
        self._handle_show_confirm_delete_view = handle_show_confirm_delete_view
        self._frame = None
        self._workout_type_entry = None
        self._workout_duration_entry = None
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän käyttöliittymässä."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Poistaa näkymän käyttöliittymästä."""
        self._frame.destroy()

    def _handle_update_workout(self):
        workout_type = self._workout_type_entry.get()
        workout_duration = self._workout_duration_entry.get()
        try:
            workout_service.update_workout(
                Workout(
                    self._current_user.username,
                    workout_type,
                    workout_duration,
                    self._selected_workout.created_at,
                    self._selected_workout.id
                )
            )
            self._handle_show_workouts_view()
        except WorkOutDurationError as error:
            self._show_error_message(error.message)

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _handle_cancel(self):
        self._handle_show_workouts_view()

    def _handle_delete_workout(self):
        self._handle_show_confirm_delete_view(self._selected_workout.id)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._frame, text="Update Workout", font=("", 12, "bold"))

        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="red"
        )

        new_workout_type_label = ttk.Label(
            master=self._frame, text="Type of Workout")
        self._workout_type_entry = StringVar(self._frame)
        self._workout_type_entry.set(self._selected_workout.type)
        new_workout_type_entry = ttk.OptionMenu(
            self._frame,
            self._workout_type_entry,
            self._selected_workout.type,
            "Cardio",
            "Strength"
        )

        new_workout_duration_label = ttk.Label(
            master=self._frame, text="Workout Duration")
        new_workout_duration_entry = ttk.Entry(master=self._frame)
        new_workout_duration_entry.insert(
            0, str(self._selected_workout.duration))

        self._workout_duration_entry = new_workout_duration_entry

        update_button = ttk.Button(
            master=self._frame, text="Update", command=self._handle_update_workout)
        delete_button = ttk.Button(
            master=self._frame, text="Delete", command=self._handle_delete_workout)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._handle_cancel)

        header_label.grid(columnspan=2, sticky=constants.W,
                          padx=(10, 0), pady=5)

        self._error_label.grid(
            row=0, column=1, sticky=constants.W, padx=(10, 0), pady=5)

        new_workout_type_label.grid(row=1, column=0, padx=(10, 0), pady=5)
        new_workout_type_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        new_workout_duration_label.grid(row=2, column=0, padx=(10, 0), pady=5)
        new_workout_duration_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        update_button.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)
        delete_button.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)
        cancel_button.grid(row=5, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
