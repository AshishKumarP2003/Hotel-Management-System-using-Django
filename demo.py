x = [
    {
        "name": "id",
        "verbose_name": "ID",
        "_verbose_name": "ID",
        "primary_key": True,
        "max_length": None,
        "_unique": False,
        "blank": True,
        "null": False,
        "remote_field": None,
        "is_relation": False,
        "default": "django.db.models.fields.NOT_PROVIDED",
        "db_default": "django.db.models.fields.NOT_PROVIDED",
        "editable": True,
        "serialize": False,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
        "_choices": None,
        "help_text": "",
        "db_index": False,
        "db_column": None,
        "db_comment": None,
        "_db_tablespace": None,
        "auto_created": True,
        "creation_counter": -13,
        "_validators": [],
        "_error_messages": None,
        "attname": "id",
        "column": "id",
        "concrete": True,
        "model": "Room.models.Room",
        "cached_col": Col(room, Room.Room.id),
    },
    {
        "name": "room_number",
        "verbose_name": "room number",
        "_verbose_name": None,
        "primary_key": False,
        "max_length": 255,
        "_unique": False,
        "blank": False,
        "null": False,
        "remote_field": None,
        "is_relation": False,
        "default": "django.db.models.fields.NOT_PROVIDED",
        "db_default": "django.db.models.fields.NOT_PROVIDED",
        "editable": True,
        "serialize": True,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
        "_choices": None,
        "help_text": "",
        "db_index": False,
        "db_column": None,
        "db_comment": None,
        "_db_tablespace": None,
        "auto_created": False,
        "creation_counter": 72,
        "_validators": [],
        "_error_messages": None,
        "db_collation": None,
        "validators": [
            "django.core.validators.MaxLengthValidator object at 0x10256a260"
        ],
        "attname": "room_number",
        "column": "room_number",
        "concrete": True,
        "model": "Room.models.Room",
        "cached_col": Col(room, Room.Room.room_number),
    },
    {
        "name": "room_type",
        "verbose_name": "room type",
        "_verbose_name": None,
        "primary_key": False,
        "max_length": 255,
        "_unique": False,
        "blank": False,
        "null": False,
        "remote_field": None,
        "is_relation": False,
        "default": "django.db.models.fields.NOT_PROVIDED",
        "db_default": "django.db.models.fields.NOT_PROVIDED",
        "editable": True,
        "serialize": True,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
        "_choices": None,
        "help_text": "",
        "db_index": False,
        "db_column": None,
        "db_comment": None,
        "_db_tablespace": None,
        "auto_created": False,
        "creation_counter": 73,
        "_validators": [],
        "_error_messages": None,
        "db_collation": None,
        "validators": [
            "django.core.validators.MaxLengthValidator object at 0x10256a110"
        ],
        "attname": "room_type",
        "column": "room_type",
        "concrete": True,
        "model": "Room.models.Room",
        "cached_col": Col(room, Room.Room.room_type),
    },
    {
        "name": "price_per_night",
        "verbose_name": "price per night",
        "_verbose_name": None,
        "primary_key": False,
        "max_length": None,
        "_unique": False,
        "blank": False,
        "null": False,
        "remote_field": None,
        "is_relation": False,
        "default": "django.db.models.fields.NOT_PROVIDED",
        "db_default": "django.db.models.fields.NOT_PROVIDED",
        "editable": True,
        "serialize": True,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
        "_choices": None,
        "help_text": "",
        "db_index": False,
        "db_column": None,
        "db_comment": None,
        "_db_tablespace": None,
        "auto_created": False,
        "creation_counter": 74,
        "_validators": [],
        "_error_messages": None,
        "attname": "price_per_night",
        "column": "price_per_night",
        "concrete": True,
        "model": "Room.models.Room",
        "cached_col": Col(room, Room.Room.price_per_night),
    },
    {
        "name": "reserved",
        "verbose_name": "reserved",
        "_verbose_name": None,
        "primary_key": False,
        "max_length": None,
        "_unique": False,
        "blank": False,
        "null": False,
        "remote_field": None,
        "is_relation": False,
        "default": False,
        "db_default": "django.db.models.fields.NOT_PROVIDED",
        "editable": True,
        "serialize": True,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
        "_choices": None,
        "help_text": "",
        "db_index": False,
        "db_column": None,
        "db_comment": None,
        "_db_tablespace": None,
        "auto_created": False,
        "creation_counter": 75,
        "_validators": [],
        "_error_messages": None,
        "attname": "reserved",
        "column": "reserved",
        "concrete": True,
        "model": "Room.models.Room",
        "cached_col": Col(room, Room.Room.reserved),
    },
    {
        "_related_name": None,
        "_related_query_name": None,
        "_limit_choices_to": None,
        "name": "hotel_id",
        "verbose_name": "hotel id",
        "_verbose_name": None,
        "primary_key": False,
        "max_length": None,
        "_unique": False,
        "blank": False,
        "null": False,
        "remote_field": "ManyToOneRel: Room.room",
        "is_relation": True,
        "default": "django.db.models.fields.NOT_PROVIDED",
        "db_default": "django.db.models.fields.NOT_PROVIDED",
        "editable": True,
        "serialize": True,
        "unique_for_date": None,
        "unique_for_month": None,
        "unique_for_year": None,
        "_choices": None,
        "help_text": "",
        "db_index": True,
        "db_column": None,
        "db_comment": None,
        "_db_tablespace": None,
        "auto_created": False,
        "creation_counter": 76,
        "_validators": [],
        "_error_messages": None,
        "from_fields": ["self"],
        "to_fields": ["id"],
        "swappable": True,
        "db_constraint": True,
        "attname": "hotel_id_id",
        "column": "hotel_id_id",
        "concrete": True,
        "model": "Room.models.Room",
        "opts": "Options for Room",
        "related_fields": [
            (
                "<django.db.models.fields.related.ForeignKey: hotel_id>, <django.db.models.fields.BigAutoField: id>"
            )
        ],
        "foreign_related_fields": ("<django.db.models.fields.BigAutoField: id>",),
    },
]