from tkinter import ttk, constants

from services.user_service import user_service
from services.workout_service import workout_service


class WorkoutsView:
    def __init__(self, root, handle_show_main_view, handle_show_create_workout):
        self._root = root
        self._current_user = user_service.current_user()
        self._all_workouts = workout_service.get_all_user_workouts(
            self._current_user.username)
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_create_workout = handle_show_create_workout
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_add_workout(self):
        self._handle_show_create_workout()

    def _handle_go_back_to_main_view(self):
        self._handle_show_main_view()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        title_label = ttk.Label(
            master=self._frame, text="Workouts", font=("", 11, "bold"))
        
        add_workout_button = ttk.Button(
            master=self._frame, text="Add Workout", command=self._handle_add_workout)
        
        back_button = ttk.Button(
            master=self._frame, text="Go Back", command=self._handle_go_back_to_main_view)

        title_label.grid(row=0, column=0, columnspan=3, sticky=constants.W,
                         padx=(10, 10), pady=5)
        back_button.grid(row=0, column=3, sticky=(constants.E, constants.W),
                         padx=(5, 10), pady=5)
        add_workout_button.grid(row=0, column=2, sticky=(constants.E, constants.W),
                                padx=(5, 10), pady=5)

        # generoitu koodi alkaa
        if not self._all_workouts:
            no_workouts_label = ttk.Label(
                master=self._frame, text="No workouts found", font=("", 10))
            no_workouts_label.grid(row=1, column=0, columnspan=3, padx=10, pady=5)
        else:
            header_type = ttk.Label(
                master=self._frame, text="Type", font=("", 10, "bold"))
            header_duration = ttk.Label(
                master=self._frame, text="Duration", font=("", 10, "bold"))
            header_date = ttk.Label(
                master=self._frame, text="Date", font=("", 10, "bold"))

            header_type.grid(row=1, column=0, padx=10, pady=2)
            header_duration.grid(row=1, column=1, padx=10, pady=2)
            header_date.grid(row=1, column=2, padx=10, pady=2)

            for idx, workout in enumerate(self._all_workouts, start=2):
                label_type = ttk.Label(master=self._frame, text=workout.type)
                label_duration = ttk.Label(
                    self._frame, text=f"{workout.duration} minutes")
                label_date = ttk.Label(master=self._frame, text=workout.created_at)

                label_type.grid(row=idx, column=0, padx=10, pady=2, sticky=constants.E)
                label_duration.grid(row=idx, column=1, padx=10, pady=2, sticky=constants.E)
                label_date.grid(row=idx, column=2, padx=10, pady=2, sticky=constants.E)

        self._frame.grid_columnconfigure(0, weight=1, minsize=100)
        self._frame.grid_columnconfigure(1, weight=1, minsize=100)
        self._frame.grid_columnconfigure(2, weight=1, minsize=100)
        self._frame.grid_columnconfigure(3, weight=0)
        # generoitu koodi päättyy
