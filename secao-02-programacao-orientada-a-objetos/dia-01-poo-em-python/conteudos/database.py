class Database:
    def __init__(
        self,
        dialect: str,
        user: str,
        host: str,
        password: str,
        database: str,
        port="",
    ) -> None:
        """
        Creates a Database instance

        Parameters
        ----------
        dialect : str
        user : str
        host : str
        password : str
        database : str
        port : str | int, optional, by default ""

        >>> Database(
        ...     dialect = "",
        ...     user = "",
        ...     host = "",
        ...     password = "",
        ...     database = "",
        ...     port = "a",
        ... )
        Traceback (most recent call last):
        ...
        ValueError: `port` must have a numeric value

        >>> Database(
        ...     dialect = "",
        ...     user = "",
        ...     host = "",
        ...     password = "",
        ...     database = "",
        ... )
        Traceback (most recent call last):
        ...
        ValueError: invalid default `port` for unrecognized `dialect`

        >>> print(Database(
        ...     dialect = "postgres",
        ...     user = "tryber",
        ...     host = "trybe",
        ...     password = "i_love_python",
        ...     database = "computer_science",
        ... ).connection_url)
        postgres://tryber:i_love_python@trybe:5432/computer_science
        """

        if not port:
            if dialect == "mysql":
                port = 3306
            elif dialect == "postgres":
                port = 5432
            else:
                raise ValueError(
                    "invalid default `port` for unrecognized `dialect`"
                )
        if type(port) == str and not port.isnumeric():
            raise ValueError("`port` must have a numeric value")

        self.connection_url = (
            f"{dialect}://{user}:{password}@{host}:{port}/{database}"
        )
