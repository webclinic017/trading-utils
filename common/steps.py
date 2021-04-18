import logging
import os

import dataset


class SetupDatabase(object):
    def run(self, context):
        home_dir = os.getenv("HOME")
        table_name = context["args"].table_name
        db_file = context["args"].db_file
        db = dataset.connect(f"sqlite:///{home_dir}/{db_file}")
        context["db_table"] = db.create_table(table_name)


class PrintContext(object):
    def run(self, context):
        logging.info(context)
