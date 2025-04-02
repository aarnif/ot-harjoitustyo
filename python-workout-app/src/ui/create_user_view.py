from tkinter import ttk, constants

class CreateUserView:
    def __init__(self, root, handle_show_login):
        self._root = root
        self._handle_show_login = handle_show_login
        self._frame = None

        self._initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header_label = ttk.Label(master=self._frame, text="Create User", font=("", 12, "bold"))

        username_label = ttk.Label(master=self._frame, text="Username", anchor="w")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password", anchor="w")
        password_entry = ttk.Entry(master=self._frame)

        confirm_password_label = ttk.Label(master=self._frame, text="Confirm Password", anchor="w")
        confirm_password_entry = ttk.Entry(master=self._frame)

        go_back_button = ttk.Button(master=self._frame, text="Go Back", command=self._handle_show_login)
        create_button = ttk.Button(master=self._frame, text="Create")

        header_label.grid(columnspan=2, sticky=constants.W, padx=(10, 0), pady=5)
        username_label.grid(row=1, column=0, sticky=constants.W, padx=(10, 0), pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=(5, 10), pady=5)

        password_label.grid(row=2, column=0, sticky=constants.W, padx=(10, 0), pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=(5, 10), pady=5)

        confirm_password_label.grid(row=3, column=0, sticky=constants.W, padx=(10, 0), pady=5)
        confirm_password_entry.grid(row=3, column=1, sticky=(constants.E, constants.W), padx=(5, 10), pady=5)

        create_button.grid(row=4, column=1, sticky=(constants.E, constants.W), padx=(5, 10), pady=5)
        go_back_button.grid(row=5, column=1, sticky=(constants.E, constants.W), padx=(5, 10), pady=5)

        self._frame.grid_columnconfigure(1, weight=1, minsize=300)



