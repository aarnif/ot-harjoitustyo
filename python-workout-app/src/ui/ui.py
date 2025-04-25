from ui.main_view import MainView
from ui.login_view import LoginView
from ui.update_workout_goal_view import UpdateWorkoutGoalView
from ui.create_user_view import CreateUserView
from ui.workouts_view import WorkoutsView
from ui.create_workout_view import CreateWorkoutView
from ui.update_workout_view import UpdateWorkoutView
from ui.confirm_delete_view import ConfirmDeleteView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._selected_workout_id = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_show_main_view(self):
        self._show_main_view()

    def _handle_show_login_view(self):
        self._show_login_view()

    def _handle_show_create_user_view(self):
        self._show_create_user_view()

    def _handle_update_workout_goal(self):
        self._show_update_workout_goal_view()

    def _handle_show_workouts_view(self):
        self._show_workouts_view()

    def _handle_show_create_workout_view(self):
        self._show_create_workout_view()

    def _handle_show_update_workout_view(self, workout_id):
        self._selected_workout_id = workout_id
        self._show_update_workout_view()

    def _handle_show_confirm_delete_view(self, workout_id):
        self._selected_workout_id = workout_id
        self._show_confirm_delete_view()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_show_login_view,
            self._show_update_workout_goal_view,
            self._handle_show_workouts_view,
        )

        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_show_main_view,
            self._handle_show_create_user_view,
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = CreateUserView(
            self._root,
            self._handle_show_main_view,
            self._handle_show_login_view,
        )

        self._current_view.pack()

    def _show_update_workout_goal_view(self):
        self._hide_current_view()

        self._current_view = UpdateWorkoutGoalView(
            self._root,
            self._handle_show_main_view,
        )

        self._current_view.pack()

    def _show_workouts_view(self):
        self._hide_current_view()

        self._current_view = WorkoutsView(
            self._root,
            self._handle_show_main_view,
            self._handle_show_create_workout_view,
            self._handle_show_update_workout_view,
        )

        self._current_view.pack()

    def _show_create_workout_view(self):
        self._hide_current_view()

        self._current_view = CreateWorkoutView(
            self._root,
            self._handle_show_workouts_view,
        )

        self._current_view.pack()

    def _show_update_workout_view(self):
        self._hide_current_view()

        self._current_view = UpdateWorkoutView(
            self._root,
            self._selected_workout_id,
            self._handle_show_workouts_view,
            self._handle_show_confirm_delete_view
        )

        self._current_view.pack()

    def _show_confirm_delete_view(self):
        self._hide_current_view()

        self._current_view = ConfirmDeleteView(
            self._root,
            self._selected_workout_id,
            self._handle_show_update_workout_view,
            self._handle_show_workouts_view
        )

        self._current_view.pack()

