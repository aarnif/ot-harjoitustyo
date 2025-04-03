from tkinter import ttk, constants, StringVar

from services.user_service import user_service, InvalidCredentialsError


class LoginView:
    def __init__(self, root, handle_show_main_view, handle_show_create_user):
        self._root = root
        self._handle_show_main_view = handle_show_main_view
        self._handle_show_create_user = handle_show_create_user
        self._frame = None
        self._username_entry = None
        self._password_entry = None
        self._error_message = None
        self._error_label = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_login_user(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        try:
            user_service.login_user(
                username_value, password_value)
            self._handle_show_main_view()
        except InvalidCredentialsError as error:
            self._show_error_message(error.message)

    def _show_error_message(self, message):
        self._error_message.set(message)
        self._error_label.grid()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        header_label = ttk.Label(
            master=self._frame, text="Login", font=("", 12, "bold"))

        self._error_message = StringVar(self._frame)

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="red"
        )

        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame, show="*")

        self._username_entry = username_entry
        self._password_entry = password_entry

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_login_user)
        create_user_button = ttk.Button(
            master=self._frame, text="Create User", command=self._handle_show_create_user)

        header_label.grid(columnspan=2, sticky=constants.W,
                          padx=(10, 0), pady=5)

        self._error_label.grid(
            row=0, column=1, sticky=constants.W, padx=(10, 0), pady=5)

        username_label.grid(row=1, column=0, padx=(10, 0), pady=5)
        username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        password_label.grid(row=2, column=0, padx=(10, 0), pady=5)
        password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        login_button.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)
        create_user_button.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=(5, 10), pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)
