import configparser
import os
class Config():
    def __init__(self):
        conf = configparser.ConfigParser()
        curpath = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(curpath,'config.ini')
        conf.read(path,encoding="utf-8")
        self.next_button_relx=float(conf['UI']['next_button_relx'])
        self.next_button_rely=float(conf['UI']['next_button_rely'])
        self.next_button_relwidth=float(conf['UI']['next_button_relwidth'])
        self.next_button_relheight=float(conf['UI']['next_button_relheight'])
        self.instruction_relx=float(conf['UI']['instruction_relx'])
        self.instruction_rely=float(conf['UI']['instruction_rely'])
        self.instruction_relwidth=float(conf['UI']['instruction_relwidth'])
        self.instruction_relheight=float(conf['UI']['instruction_relheight'])
        self.pixels_between_dash=int(conf['UI']['pixels_between_dash'])
        self.scale=float(conf['UI']['scale'])
        self.ms_to_wait=int(conf['Experiment']['ms_to_wait'])
        self.n_test_set_single_line=int(conf['Experiment']['n_test_set_single_line'])
        self.minimum_x_diff=int(conf['Experiment']['minimum_x_diff'])
        self.csv_filename=conf['Data']['csv_filename']
        self.canvas_color = conf['UI']['canvas_color']
        self.text_color = conf['UI']['text_color']
conf = Config()