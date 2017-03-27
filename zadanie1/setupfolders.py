"""
This script prepares test files to work on.

Usage:
    setupfolders.py [root_folder]

root_folder - folder where all test folders and files are going to be created. Defaults to c:\temp if ommited.
"""

import os.path
import random
import shutil
import sys
from datetime import datetime
from datetime import timedelta
from zipfile import ZipFile


class SetupFolders(object):
    test_folder = "/input/PL"
    number_of_files = 444
    initial_date = datetime(year=2016, month=1, day=1)
    zip_filename_pattern = "EXTERNAL_SALES_DATA_{timestamp}_Poland.zip"
    file_list = [
        "exp_product_md.csv"
        , "exp_location_md.csv"
        , "exp_territory_md.csv"
        , "exp_user_md.csv"
        , "exp_order.csv"
        , "exp_visit.csv"
        , "exp_audit.csv"
        , "exp_task_md.csv"
        , "exp_display.csv"
    ]

    def __init__(self, root_folder):
        self.root_folder = root_folder
        self.target_folder = self.root_folder + self.test_folder

    def prepare(self):
        self.cleanup()
        self.create_folders()

    def cleanup(self):
        if os.path.exists(self.target_folder) and os.path.isdir(self.target_folder):
            shutil.rmtree(self.target_folder)

    def create_folders(self):
        os.makedirs(self.target_folder, True)
        for i in range(0, self.number_of_files):
            td = timedelta(days=i, hours=5, seconds=random.randrange(0, 60 * 60 * 2))
            ts = self.initial_date + td
            file = self.zip_filename_pattern.format(**{
                "timestamp": ts.strftime("%Y%m%d%H%M%S")})
            zf = ZipFile(self.target_folder + os.path.sep + file, "x")
            for arch_file in self.file_list:
                record = "{},{},{}".format(i, arch_file, "hello python!\r\n")
                zf.writestr(arch_file, record)
            zf.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.argv.append("c:\\temp")
    setup = SetupFolders(sys.argv[1])
    setup.prepare()
