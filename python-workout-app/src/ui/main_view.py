from tkinter import ttk, constants

from services.user_service import user_service


class MainView:
    def __init__(self, root, handle_show_login):
        self._root = root
        self._current_user = user_service.current_user()
        self._handle_show_login = handle_show_login
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_logout_user(self):
        user_service.logout_user()
        self._handle_show_login()

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._frame, text=f"Hi, {self._current_user.username}!", font=("", 12, "bold"))

        logout_button = ttk.Button(
            master=self._frame, text="Logout", command=self._handle_logout_user)

        header_label.grid(columnspan=2, sticky=constants.W,
                          padx=(10, 0), pady=5)

        logout_button.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
