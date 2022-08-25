# region <<<<=====================================[Application Information]======================================>>>>

# APP NAME:
# ProbeProgramMakerDB

# APP USAGE:
# Used to Update the Existing ProbePrograms using the new-updated Template and accessing the DataBase.

# VERSION:
# ProbeProgramMakerDBVersion1.0.1

# LANGUAGE:
# Python 3.7

# FRAME WORKS:
# Kivy and Kivymd to build the App and design the Layout.

# CREATED BY:
# Moemen Alatweh
# EMAIL:
# malatweh@rwbteam.com
# moemenatweh@hotmail.com

# endregion <<<<==================================[Application Information]======================================>>>>


# region <<<<=====================================[Application Requirements]=====================================>>>>

# =======================================================|
#  Import (Config) to control APP Configuration Settings.|
# =======================================================|
from kivy.config import Config

# =============================================================================================================|
# Setting the APP to have Fixed Configuration (by putting False) which makes the user can't change Screen Size,|
# to keep the APP Organized.                                                                                   |
# =============================================================================================================|
Config.set('graphics', 'resizable', False)

# ================================|
# Import (MDApp) to Build the APP.|
# ================================|
from kivymd.app import MDApp

# ==================================================|
# Import (Window) to control the APP Window Setting.|
# ==================================================|
from kivy.core.window import Window

# ==================================================|
# Import (AsyncImage) to set APP Image from Website.|
# ==================================================|
from kivy.uix.image import AsyncImage, Image

# =============================================================|
# Import (Builder) to create the KV file (APP Elements Layout).|
# =============================================================|
from kivy.lang.builder import Builder

# ==========================================================================|
# Import (ScreenManager) and (Screen) to create APP Screens and Manege them.|
# ==========================================================================|
from kivy.uix.screenmanager import ScreenManager, Screen

# ==========================================|
# Import (MDLabel) to Show some APP's texts.|
# ==========================================|
from kivymd.uix.label import MDLabel

# ===============================================================|
# Import (MDRaisedButton) as a button to execute the APP's actions.|
# ===============================================================|
from kivymd.uix.button import MDRaisedButton

# ===================================================|
# Import (MDBoxLayout) to contain all APP's Elements.|
# ===================================================|
from kivymd.uix.boxlayout import MDBoxLayout

# ==================================================|
# Import (BoxLayout) to contain some APP's Elements.|
# ==================================================|
from kivy.uix.boxlayout import BoxLayout

# ====================================================================|
# Import (MDTextField) and (TextInput) to Enter an Inputs for the APP.|
# ====================================================================|
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput

# ======================================================================================|
# Import (MDDialog) as a Dialog window to inform the user about tasks and takes decisions.|
# ======================================================================================|
from kivymd.uix.dialog import MDDialog

# ================================================================|
# Import (OneLineAvatarListItem) to Create some APP's Lists Items.|
# ================================================================|
from kivymd.uix.list import OneLineAvatarListItem

# ====================================================================================|
# Import (glob) <built_in function in python> to search and find files inside folders.|
# ====================================================================================|
import glob

# ========================================================================================|
# Import (subprocess) <built_in function in python> to start and open an Application in__ |
# __Windows Operative System (Ex: CIMCO, Microsoft Word...Etc)                            |
# ========================================================================================|
import subprocess

# ===============================================================|
# Import (pandas) Library to Read and Write data of Excel Sheets.|
# ===============================================================|
import pandas as pd

# ======================================================|
# Import (date) Library to set and Manege Date and time.|
# ======================================================|
from datetime import date

today = date.today()
today_date = today.strftime("%m/%d/%Y")

# =============================================================================|
# Import (pyodbc) Library to connect the APP with the DataBase and Manege Data.|
# =============================================================================|
import pyodbc

# endregion <<<<====================================[Application Requirements]====================================>>>>


# region <<<<========================================[Screen Builder KV]=========================================>>>>
Screens_Builder = """
ScreenManager:
    HomeScreen:
    SettingScreen:

<HomeScreen>:
    name: 'HomeScreen'
    MDLabel:
        text: 'Probe Programs Maker'
        pos_hint: {'center_x':0.81,'center_y':0.85}
        font_size: '32sp'
        bold: True
        italic: True
        theme_text_color: "Primary"
        tooltip_text: self.text

    MDLabel:
        text: 'Enter Forging Number'
        pos_hint: {'center_x':0.90,'center_y':0.63}
        font_size: '18sp'
        bold: True
        italic: True
        theme_text_color: "Secondary"                 

    MDTextField:
        id: ForgingNumber
        text: self.text.upper() if self.text is not None else ''
        hint_text: "                           Forging Number"
        helper_text: "Forging Number MUST match with the number in the DatBase."
        helper_text_mode: "on_focus"
        required: True
        halign: "auto"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.50}
        size_hint_x:None
        width:340
        height:10        

    MDRaisedButton:                                                                         
        text: 'SUBMIT'
        md_bg_color: 120/255, 0/255, 0/255, 1
        font_size: "15sp"
        pos_hint: {'center_x':0.4,'center_y':0.25}
        on_press : 
            root.database_connect()   
        on_release :    
            root.create_probe_program() 

    MDRaisedButton:                                                                         
        text: 'RESET'
        md_bg_color: 120/255, 0/255, 0/255, 1
        font_size: "15sp"
        pos_hint: {'center_x':0.6,'center_y':0.25}  
        on_press : 
            root.reset_fields()  

    MDRaisedButton:
        text: 'Setting'
        halign:'left'
        md_bg_color: 120/255, 0/255, 0/255, 1
        font_size: "15sp"
        on_press: root.manager.current = 'SettingScreen'        

    MDLabel:
        text: '             Version 1.0.1'
        pos_hint: {'center_x':1.32,'center_y':0.07}
        font_style: 'Caption'
        theme_text_color: "Custom"
        text_color: 175/255.0, 0/255.0, 0/255.0, 1 

    MDLabel:
        text: 'Created by: Moemen Alatweh'
        pos_hint: {'center_x':1.32,'center_y':0.04}
        font_style: 'Caption'
        theme_text_color: "Custom"
        text_color: 175/255.0, 0/255.0, 0/255.0, 1

    MDLabel:
        text: 'malatweh@rwbteam.com'
        pos_hint: {'center_x':1.33,'center_y':0.01}
        font_style: 'Caption'
        theme_text_color: "Custom"
        text_color: 175/255.0, 0/255.0, 0/255.0, 1         

<SettingScreen>:
    name: 'SettingScreen'

    MDLabel:
        text: 'Setting'
        pos_hint: {'center_x':0.93,'center_y':0.9}
        font_size: '36sp'
        bold: True
        italic: True
        theme_text_color: "Primary"

    MDTextField:
        id: ProbeProgramsPath
        text: "H:\CNCProgs\HOREBORE\Probe Programs"         
        hint_text: "Probe Programs File Path"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.75}
        size_hint_x:None
        width:800
        height:50        

    MDTextField:
        id: RunningFolderPathOfUpdatedProbePrograms
        hint_text: "Updated Probe Programs (Running Folder) Path"
        text: "H:\CNCProgs\HOREBORE\ProbePrograms_Updated"
        helper_text: "Folder that Use on Machine to Load the Probe Programs."
        helper_text_mode: "on_focus"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.63}
        size_hint_x:None
        width:800
        height:50        

    MDTextField:
        id: OriginalFolderPathOfUpdatedProbePrograms
        hint_text: "Updated Probe Programs (Original Folder) Path"
        text: "H:\CNCProgs\HOREBORE ORIGINAL\ProbePrograms_Updated"
        helper_text: "Folder that Use as Backup For Programs."
        helper_text_mode: "on_focus"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.51}
        size_hint_x:None
        width:800
        height:50                        

    MDTextField:
        id: ProbeTemplate
        hint_text: "Probe Template Path"
        text: "H:\CNCProgs\HOREBORE\Probe Programs\FutureProbeTemplate\FUTUREPROBETEMPLATE.SSB"
        helper_text: "The New Template For Probe Programs."
        helper_text_mode: "on_focus"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.39}
        size_hint_x:None
        width:800
        height:50     

    MDTextField:
        id: CimcoEditorPath
        hint_text: "CIMCO Editor Path"
        text: "C:\CIMCO\CIMCOEdit8\CIMCOEdit.EXE"
        helper_text: ""
        helper_text_mode: "on_focus"
        color_mode: 'custom'
        line_color_focus: 1, 1, 1, 1
        pos_hint: {'center_x': 0.50, 'center_y': 0.27}
        size_hint_x:None
        width:800
        height:50

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        md_bg_color: 120/255, 0/255, 0/255, 1
        font_size: "15sp"
        on_press: root.manager.current = 'HomeScreen'                       

"""


# endregion <<<<=======================================[Screen Builder KV]========================================>>>>


# region <<<<===========================================[Home Screen]============================================>>>>

class HomeScreen(Screen):

    # ============================================================================================|
    # [#] Create Function to Connect the APP with the DataBase.                                   |
    # [#] Use (try/except) Blocks to Handle any Error may occur when connecting with the DataBase.|
    # ============================================================================================|
    def database_connect(self):
        print("(database_connect) Function >> called")

        try:
            # ===================================================================================================|
            # [#] Use (pyodbc) Library to connect the APP with the DataBase and Manege Data.                     |
            # [#] To be Able to access the DataBase, Needs permission and DataBase info From IT Department.      |
            # [#] Information needed to connect with the DateBase:                                               |
            #     - Type of Driver which is : {SQL Server}                                                       |
            #     - Name of Server which is : us-men-app-sql1                                                    |
            #     - Name of DataBase which is : EngineWorx                                                       |
            #     - User Authentication : Set it as 'Yes' while Authentication Information are Same as UserLogin |
            #                             Info for the Computer (Windows Authentication), If They are different  |
            #                             or set it to use (SQL Authentication) needs to add:                    |
            #                             ('Uid=WISECOMANF\\DomainUser;') and ('Pwd='UserPasswordToSQL;') with   |
            #                             ('Trusted_Connection=No;').                                            |
            # [#] Define Variable to create connection with DataBase by using DataBase Info.                     |
            # ===================================================================================================|
            global engine_worx_database_connect
            engine_worx_database_connect = pyodbc.connect('Driver={SQL Server};'
                                                          'Server=us-men-app-sql1;'
                                                          'Database=EngineWorx;'
                                                          'Trusted_Connection=Yes;')

            # ================================================================================|
            # Define Variable to Create 'Cursor' to point and locate the data inside DataBase.|
            # ================================================================================|
            global engine_worx_database_cursor
            engine_worx_database_cursor = engine_worx_database_connect.cursor()

        # =====================================================================================================|
        # [#] Use (except) block to Handle any Error may occur when accessing the DataBase and avoid APP crash.|
        # [#] Use (return) to stop the function (APP as a result) from executing the rest of the code.         |
        # =====================================================================================================|
        except Exception as error:
            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_database, font_size=16)
            self.home_screen_window_database = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                    "[color=ffffff]Failed to Connect or Access" + '[b][u][color=ffffff] EngineWorx [/color][/u][/b]'
                    + "DataBase." + "\n" + "An Error has occurred :[/color]" + "\n" + '[color=ff1a1a]' + str(error) +
                    '[/color]' + "\n" + "[color=ffffff]Double Check Network and your DataBase Authentication.[/color]"),
                                                        size_hint=(0.7, 1.0), buttons=[close_button],
                                                        auto_dismiss=False)
            self.home_screen_window_database.open()
            return

    # ===========================================================================|
    # [#] Create Function to Update Probe Programs for Existing Probe programs.  |
    # ===========================================================================|
    def create_probe_program(self):
        print("(create_probe_program) Function >> called")

        # =========================================================================================|
        # [#]  Define a Variable to set path of the Probe Program Folder.                          |
        # [#] Access MDTextField of (id: ProbeProgramsPath) in (SettingScreen) from Screens_Builder|
        # =========================================================================================|
        global probe_programs_folder_path
        probe_programs_folder_path = self.manager.get_screen('SettingScreen').ids["ProbeProgramsPath"].text
        print("probe_programs_folder_path: ", probe_programs_folder_path)

        # ==========================================================================|
        # [#]  Define a Variable to set path of the Running Folder.                 |
        # [#] Access MDTextField of (id: RunningFolderPathOfUpdatedProbePrograms) in|
        #     (SettingScreen) from Screens_Builder                                  |
        # ==========================================================================|
        global running_folder_path_of_probe_programs
        running_folder_path_of_probe_programs = self.manager.get_screen('SettingScreen').ids[
            "RunningFolderPathOfUpdatedProbePrograms"].text
        print("running_folder_path_of_probe_programs: ", running_folder_path_of_probe_programs)

        # ===========================================================================|
        # [#]  Define a Variable to set path of the Original Folder.                 |
        # [#] Access MDTextField of (id: OriginalFolderPathOfUpdatedProbePrograms) in|
        #     (SettingScreen) from Screens_Builder                                   |
        # ===========================================================================|
        global original_folder_path_of_probe_programs
        original_folder_path_of_probe_programs = self.manager.get_screen('SettingScreen').ids[
            "OriginalFolderPathOfUpdatedProbePrograms"].text
        print("original_folder_path_of_probe_programs: ", original_folder_path_of_probe_programs)

        # =========================================================|
        # [#]  Define a Variable to set path of the Probe Template.|
        # [#] Access MDTextField of (id: ProbeTemplate) in         |
        #     (SettingScreen) from Screens_Builder                 |
        # =========================================================|
        global probe_programs_template
        probe_programs_template = self.manager.get_screen('SettingScreen').ids[
            "ProbeTemplate"].text
        print("probe_programs_template: ", probe_programs_template)

        # ===================================================|
        # [#]  Define a Variable to set path of Cimco Editor.|
        # [#] Access MDTextField of (id: CimcoEditorPath) in |
        #     (SettingScreen) from Screens_Builder           |
        # ===================================================|
        global cimco_editor_path
        cimco_editor_path = self.manager.get_screen('SettingScreen').ids[
            "CimcoEditorPath"].text
        print("cimco_editor_path: ", cimco_editor_path)

        # =================================================================================================|
        # [#] Define a Variable to get the Forging Number that user input.                                 |
        # [#] Get the text of the MDTextField of id ["ForgingNumber"] in (HomeScreen) from Screens_Builder.|
        # =================================================================================================|
        global forging_number
        forging_number = self.manager.get_screen('HomeScreen').ids["ForgingNumber"].text
        print()
        print("Forging Number:", forging_number)

        # ==================================================================================|
        # [#] If the user doesn't enter the Forging Number, the App will ask for user input.|
        # ==================================================================================|
        if (self.manager.get_screen('HomeScreen').ids["ForgingNumber"].text == "" or
                self.manager.get_screen('HomeScreen').ids["ForgingNumber"].text == " "):
            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program, font_size=16)
            self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                "[color=ffffff]Please Enter The Forging Number.[/color]"), size_hint=(0.7, 1.0),
                                                       buttons=[close_button], auto_dismiss=False)
            self.home_screen_window_program.open()
            return

        # =========================================================================================|
        # [#] Try to find Forging Dimensions when user enter the Forging number and click on submit|
        # =========================================================================================|
        else:
            try:
                # region <<<<==============================[Forge Ref Length]==============================>>>>

                # =================================================================================================|
                # [#] Get the Value from the DataBase by using 'ForgeItemID' and Access the Data location by using:|
                #     Table Name : SpexForge.                                                                      |
                #     Column Name : ForgeRefLength.                                                                |
                # [#] Use Same Forging Database Table "SpexForge" even with JE Forging, but needs to make sure     |
                #     using JE Forging Number that used for Wiseco Side(they are saved in the Excel Sheet File).   |
                # =================================================================================================|
                engine_worx_database_cursor.execute(
                    'SELECT ForgeRefLength FROM SpexForge WHERE ForgeItemID = ?', forging_number)

                # ========================================================================================|
                # [#] Use for loop to iterate through the DateBase.                                       |
                # [#] Set the value as it is stored in the DataBase if no data found or stored as'String',|
                #     otherwise, Round the Numerical Value for 4-Digits.                                  |
                # [#] Expected Data output Type : 'Numeric'                                               |
                # [#] Expected Data output value : Numeric Value > [0.????]                               |
                # ========================================================================================|
                for data in engine_worx_database_cursor.fetchone():
                    if ((data is None) or (type(data) == str)):
                        forge_ref_length = data
                    else:
                        forge_ref_length = round(float(data), 4)
                print("[#]forge_ref_length FOR " + forging_number + ":")
                print("     ", forge_ref_length)

                # endregion <<<<============================[Forge Ref Length]============================>>>>

                # region <<<<==============================[Forging Diameter]==============================>>>>

                # =================================================================================================|
                # [#] Get the Value from the DataBase by using 'ForgeItemID' and Access the Data location by using:|
                #     Table Name : SpexForge.                                                                      |
                #     Column Name : ForgeOD.                                                                       |
                # [#] Use Same Forging Database Table "SpexForge" even with JE Forging, but needs to make sure     |
                #     using JE Forging Number that used for Wiseco Side(they are saved in the Excel Sheet File).   |
                # =================================================================================================|
                engine_worx_database_cursor.execute(
                    'SELECT ForgeOD FROM SpexForge WHERE ForgeItemID = ?', forging_number)

                # ========================================================================================|
                # [#] Use for loop to iterate through the DateBase.                                       |
                # [#] Set the value as it is stored in the DataBase if no data found or stored as'String',|
                #     otherwise, Round the Numerical Value for 4-Digits.                                  |
                # [#] Expected Data output Type : 'Numeric'                                               |
                # [#] Expected Data output value : Numeric Value > [0.????]                               |
                # ========================================================================================|
                for data in engine_worx_database_cursor.fetchone():
                    if ((data is None) or (type(data) == str)):
                        forging_diameter = data
                    else:
                        forging_diameter = round(float(data), 4)
                print("[#]forging_diameter FOR " + forging_number + ":")
                print("     ", forging_diameter)

                # endregion <<<<============================[Forging Diameter]============================>>>>

                # region <<<<========================[Forging Boss Outside Spacing]========================>>>>

                # =================================================================================================|
                # [#] Get the Value from the DataBase by using 'ForgeItemID' and Access the Data location by using:|
                #     Table Name : SpexForge.                                                                      |
                #     Column Name : BossOutsdSpace.                                                                |
                # [#] Use Same Forging Database Table "SpexForge" even with JE Forging, but needs to make sure     |
                #     using JE Forging Number that used for Wiseco Side(they are saved in the Excel Sheet File).   |
                # =================================================================================================|
                engine_worx_database_cursor.execute(
                    'SELECT BossOutsdSpace FROM SpexForge WHERE ForgeItemID = ?', forging_number)

                # ========================================================================================|
                # [#] Use for loop to iterate through the DateBase.                                       |
                # [#] Set the value as it is stored in the DataBase if no data found or stored as'String',|
                #     otherwise, Round the Numerical Value for 4-Digits.                                  |
                # [#] Expected Data output Type : 'Numeric'                                               |
                # [#] Expected Data output value : Numeric Value > [0.????]                               |
                # ========================================================================================|
                for data in engine_worx_database_cursor.fetchone():
                    if ((data is None) or (type(data) == str)):
                        forging_outside_boss_spacing = data
                    else:
                        forging_outside_boss_spacing = round(float(data), 4)
                print("[#]forging_outside_boss_spacing FOR " + forging_number + ":")
                print("     ", forging_outside_boss_spacing)

                # endregion <<<<==========================[Forging Boss Outside Spacing]=========================>>>>
            except Exception as error:
                close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                              font_size=16)
                self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                        "[color=ffffff]Failed to Use Forging Number " + '[b]' + forging_number + '[/b]' +
                        " to Create the Probe Program." + "\n" + "An Error has occurred : [/color]" + "\n" +
                        '[color=ff1a1a]' + str(error) + '[/color]' + "\n" +
                        "[color=ffffff]Make Sure the Forging Number you entered is correct and it match" + "\n" +
                        "with the DateBase." + "\n" + "Otherwise, Check Network, and Connection." + "\n"),
                                                           size_hint=(0.7, 1.0), buttons=[close_button],
                                                           auto_dismiss=False)
                self.home_screen_window_program.open()
                return

        # ==========================================================|
        # [#] Create list to add the new template lines to the list |
        # ==========================================================|
        global updated_probe_program_lines
        updated_probe_program_lines = []
        try:
            with open(probe_programs_template, 'rt') as current_program:
                for line in current_program:
                    updated_probe_program_lines.append(line.rstrip('\n'))
                print()
                print("Updated_Template_probe_program_lines:", '\n', updated_probe_program_lines)
                # =========================================================================|
                # To print the list line by line
                # =========================================================================|
                # print("Updated_probe_program_lines:" + '\n' + '\n'.join(updated_probe_program_lines))

        except IOError as error:
            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                          font_size=16)
            self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                    "[color=ffffff]Failed to Find, Load, or Access Probe Program Template" + "\n" +
                    "An Error has occurred : [/color]" + "\n" +
                    '[color=ff1a1a]' + str(error) + '[/color]' + "\n" +
                    "[color=ffffff]Double Check Network, and File Location" + "\n"),
                                                       size_hint=(0.7, 1.0), buttons=[close_button],
                                                       auto_dismiss=False)
            self.home_screen_window_program.open()
            return

        # ============================================================================================================|
        # [#] Forging Numbers in the DataBase are stored with the Rev extension like                                  |
        #    (F6566XA0,F6064MZA1,F4027TDXA2,FJE160-HEX...Etc),On other hand the ProbPrograms saved in variant ways,   |
        #    Sometimes it saved with the whole thing(with one of the REV) like 'F6228XA4', sometimes without the 'Rev'|
        #    like 'F6444X', because of that needs to 'Filter' the Forging Number to not have the Rev extension to make|
        #    ProbePrograms searching process more efficient.                                                          |
        # [#] Define Variable of 'Filtered' Forging Number that will use to Search the ProbePrograms and              |
        #     Set it to be "F" (because all forging numbers start with that).                                         |
        # [#] Define Variable of 'digit' and set it to be <0> to use it to iterate through the whole Forging Number.  |
        # [#] Use (while and for) loops with (if statement) to Set the 'Filtered' Forging Number by adding            |
        #     each digit of Forging number until find 'X' or 'Z' Letter to add it as well and End the loop.           |
        # ============================================================================================================|
        if forging_number != "" and forging_number is not None:
            global forging_number_for_probe_program
            forging_number_for_probe_program = "F"
            digit = 0
            # ==============================================================================================|
            # [#] Set the Condition of the (while) loop to End the loop when find 'X' or 'Z' Letter or reach|
            #     to the last digit of Forging Number (by putting 'forging_number[-1]').                    |
            # ==============================================================================================|
            while (digit != "X" and digit != "x" and digit != "Z" and digit != "z" and digit != forging_number[-1]):

                # ==============================================================================================|
                # [#] Start iterate through the Forging Number From index (position) <1> not <0> (by putting    |
                #     forging_number[1:]) because no need to add the 'F' letter again (it set on                |
                #     'forging_number_for_probe_program' above).                                                |
                # [#] Add each digit to the 'Filtered' Forging Number until find 'X' or 'Z' Letter to add       |
                #     it as well then End (break) the loop.                                                     |
                # [#] As a Result, 'Filtered' Forging Number will be forging number without Rev extension like: |
                #     F6566X, F6064MZ, F4027TDX, FJE160-HEX...Etc.                                              |
                # [#] Some ProbPrograms stored for "X" not "Z" or vice versa, for these forging the User needs  |
                #     to store the ProbProgram in both letters ('X' and 'Z') to be always able to find the      |
                #     program while it's created.                                                               |
                # ==============================================================================================|
                for digit in forging_number[1:]:
                    forging_number_for_probe_program = forging_number_for_probe_program + digit
                    if (digit == "X" or digit == "x" or digit == "Z" or digit == "z"):
                        break
            print()
            print("forging_number_for_probe_program: ", forging_number_for_probe_program)

        # ========================================================================================================|
        # [#] Define list to add all ProbPrograms that found from search of the 'Filtered' Forging Number.        |
        # [#] Use (for) loop with (glob.glob) method to search in (probe_programs_folder) path.                   |
        # [#] Use (*) after Forging Number to search the file even with part of name to find all possible results.|
        #     (Ex: name of F4035X it gives result of F4035XA0, F8835X it gives result of F8835XA1...Etc).         |
        # [#] Use (try/except) Blocks to Handle any Error may occur when Accessing or Finding Files and Folders.  |
        # ========================================================================================================|
        try:
            global result_of_probe_program_search
            result_of_probe_program_search = []
            for file in glob.glob(probe_programs_folder_path + '*\*' + forging_number_for_probe_program + '*'):
                result_of_probe_program_search.append(file)
            print("Total of results_of_probe_program_search: ", len(result_of_probe_program_search))
            print(result_of_probe_program_search)

            # =======================================================================================|
            # [#] Define list to add all ProbPrograms lines one by one After Finding the ProbProgram.|
            # =======================================================================================|
            existing_probe_programs_lines = []

            # =====================================================================================================|
            # [#] Use (if statement) to check ProbPrograms Search results.                                         |
            # [#] If number of ProbPrograms that founded is <1>, open the program and add all the lines to the list|
            # =====================================================================================================|
            if ((len(result_of_probe_program_search) == 1) and
                    (forging_number != "" and forging_number is not None)):
                print("RESULT_OF_PROBE_PROGRAM_SEARCH: ", result_of_probe_program_search)
                print("Existing_probe_program: ", result_of_probe_program_search[0])
                # =================================================================================================|
                # [#] Use <with open()> method to open the program (by use index[0] of the results list) as        |
                #     current file to iterate through its lines and add them to the ProbPrograms lines list.       |
                # [#] Use 'rt' to: read a file as text.                                                            |
                # [#] Use [line.rstrip('\n')] to strip newline and add it to list (ie:[Element],new line,[Element])|
                # =================================================================================================|
                with open(result_of_probe_program_search[0], 'rt') as current_program:
                    for line in current_program:
                        existing_probe_programs_lines.append(line.rstrip('\n'))

                    print("Existing_probe_program_lines:", '\n', existing_probe_programs_lines)
                # ===================================================================================|
                # [#] Use (for) loop to read the new Template lines and modify the lines that needed.|
                # ===================================================================================|
                for line in updated_probe_program_lines:
                    # ======================================================|
                    # Set up the 4-Digits same as the Existing Probe program|
                    # ======================================================|
                    updated_probe_program_lines[0] = existing_probe_programs_lines[0]

                    # ==========================================|
                    # Get the forge_ref_length from the DateBase|
                    # ==========================================|
                    substr = "VC150"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index == 0):
                        if ((forge_ref_length != 0 and forge_ref_length is not None and forge_ref_length != "")):
                            VC150_variable_index = updated_probe_program_lines.index(line)
                            print("VC150_variable_index:", VC150_variable_index)
                            print(updated_probe_program_lines[VC150_variable_index])

                            updated_probe_program_lines[VC150_variable_index] = (
                                    'VC150=' + format(forge_ref_length) + '  (ForgeRefLength)')

                    # ==========================================|
                    # Get the forging_diameter from the DateBase|
                    # ==========================================|
                    substr = "VC156"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index == 0):
                        if (forging_diameter != 0 and forging_diameter is not None):
                            VC156_variable_index = updated_probe_program_lines.index(line)
                            print("VC156_variable_index:", VC156_variable_index)
                            print(updated_probe_program_lines[VC156_variable_index])
                            updated_probe_program_lines[VC156_variable_index] = (
                                    'VC156=[' + format(forging_diameter) + '/2]' +
                                    '  (zPinBoreTop - ? IS Forging Diameter)')

                    # ======================================================|
                    # Get the forging_outside_boss_spacing from the DateBase|
                    # ======================================================|
                    substr = "VC159"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index == 0):
                        if (forging_outside_boss_spacing != 0 and forging_outside_boss_spacing is not None):
                            VC159_variable_index = updated_probe_program_lines.index(line)
                            print("VC159_variable_index:", VC159_variable_index)
                            print(updated_probe_program_lines[VC159_variable_index])
                            updated_probe_program_lines[VC159_variable_index] = (
                                    'VC159=' + format(forging_outside_boss_spacing) + '  (OutsideBossSpacing)')

                        elif (forging_outside_boss_spacing == 0 or forging_outside_boss_spacing is None):
                            VC159_variable_index = updated_probe_program_lines.index(line)
                            print("VC159_variable_index:", VC159_variable_index)
                            print(updated_probe_program_lines[VC159_variable_index])
                            updated_probe_program_lines[VC159_variable_index] = (
                                    'VC159=' + format(forging_diameter) + '  (OutsideBossSpacing)')

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # ===========================================================================|
                    substr = "VZOFZ[1]"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index == 0):
                        VZOFZ_1_variable_index = updated_probe_program_lines.index(line)
                        # print("VZOFZ[1]_index:", VZOFZ_1_variable_index)
                        # print(updated_probe_program_lines[VZOFZ_1_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "VZOFZ[1]"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index == 0):
                                VZOFZ_1_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("VZOFZ[1]_index for Existing Probe Program:",
                                #       VZOFZ_1_variable_index_in_existing_probe_program)
                                # print(existing_probe_programs_lines[VZOFZ_1_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[VZOFZ_1_variable_index] = \
                            existing_probe_programs_lines[VZOFZ_1_variable_index_in_existing_probe_program]

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # ===========================================================================|
                    substr = "VZOFZ[2]"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index == 0):
                        VZOFZ_2_variable_index = updated_probe_program_lines.index(line)
                        # print("VZOFZ[2]_index:", VZOFZ_2_variable_index)
                        # print(updated_probe_program_lines[VZOFZ_2_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "VZOFZ[2]"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index == 0):
                                VZOFZ_2_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("VZOFZ[2]_index for Existing Probe Program:",
                                #       VZOFZ_2_variable_index_in_existing_probe_program)
                                # print(existing_probe_programs_lines[VZOFZ_2_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[VZOFZ_2_variable_index] = \
                            existing_probe_programs_lines[VZOFZ_2_variable_index_in_existing_probe_program]

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # ===========================================================================|
                    substr = "VZOFZ[3]"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index == 0):
                        VZOFZ_3_variable_index = updated_probe_program_lines.index(line)
                        # print("VZOFZ[3]_index:", VZOFZ_3_variable_index)
                        # print(updated_probe_program_lines[VZOFZ_3_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "VZOFZ[3]"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index == 0):
                                VZOFZ_3_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("VZOFZ[3]_index for Existing Probe Program:",
                                #       VZOFZ_3_variable_index_in_existing_probe_program)
                                # print(existing_probe_programs_lines[VZOFZ_3_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[VZOFZ_3_variable_index] = \
                            existing_probe_programs_lines[VZOFZ_3_variable_index_in_existing_probe_program]

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # ===========================================================================|
                    substr = "VZOFZ[4]"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index == 0):
                        VZOFZ_4_variable_index = updated_probe_program_lines.index(line)
                        # print("VZOFZ[4]_index:", VZOFZ_4_variable_index)
                        # print(updated_probe_program_lines[VZOFZ_4_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "VZOFZ[4]"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index == 0):
                                VZOFZ_4_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("VZOFZ[4]_index for Existing Probe Program:",
                                #       VZOFZ_4_variable_index_in_existing_probe_program)
                                # print(existing_probe_programs_lines[VZOFZ_4_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[VZOFZ_4_variable_index] = \
                            existing_probe_programs_lines[VZOFZ_4_variable_index_in_existing_probe_program]

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # Use "WKO=1" as a text to search the line.                                  |
                    # Use " != -1 " in the 'if statement' because <find> method return (-1) if   |
                    # doesn't find the text in the line.                                         |
                    # ===========================================================================|
                    substr = "WKO=1"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index != -1):
                        OPSTN_WKO_1_variable_index = updated_probe_program_lines.index(line)
                        # print("OPSTN_WKO_1_variable_index:", OPSTN_WKO_1_variable_index)
                        # print(updated_probe_program_lines[OPSTN_WKO_1_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "WKO=1"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index != -1):
                                OPSTN_WKO_1_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("OPSTN_WKO_1_variable_index for Existing Probe Program:",
                                #       OPSTN_WKO_1_variable_index_in_existing_probe_program)
                                # print(
                                #     existing_probe_programs_lines[OPSTN_WKO_1_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[OPSTN_WKO_1_variable_index] = \
                            existing_probe_programs_lines[OPSTN_WKO_1_variable_index_in_existing_probe_program]

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # Use "WKO=2" as a text to search the line.                                  |
                    # Use " != -1 " in the 'if statement' because <find> method return (-1) if   |
                    # doesn't find the text in the line.                                         |
                    # ===========================================================================|
                    substr = "WKO=2"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index != -1):
                        OPSTN_WKO_2_variable_index = updated_probe_program_lines.index(line)
                        # print("OPSTN_WKO_2_variable_index:", OPSTN_WKO_2_variable_index)
                        # print(updated_probe_program_lines[OPSTN_WKO_2_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "WKO=2"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index != -1):
                                OPSTN_WKO_2_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("OPSTN_WKO_2_variable_index for Existing Probe Program:",
                                #       OPSTN_WKO_2_variable_index_in_existing_probe_program)
                                # print(existing_probe_programs_lines[
                                #           OPSTN_WKO_2_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[OPSTN_WKO_2_variable_index] = \
                            existing_probe_programs_lines[OPSTN_WKO_2_variable_index_in_existing_probe_program]

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # Use "WKO=3" as a text to search the line.                                  |
                    # Use " != -1 " in the 'if statement' because <find> method return (-1) if   |
                    # doesn't find the text in the line.                                         |
                    # ===========================================================================|
                    substr = "WKO=3"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index != -1):
                        OPSTN_WKO_3_variable_index = updated_probe_program_lines.index(line)
                        # print("OPSTN_WKO_3_variable_index:", OPSTN_WKO_3_variable_index)
                        # print(updated_probe_program_lines[OPSTN_WKO_3_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "WKO=3"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index != -1):
                                OPSTN_WKO_3_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("OPSTN_WKO_3_variable_index for Existing Probe Program:",
                                #       OPSTN_WKO_3_variable_index_in_existing_probe_program)
                                # print(existing_probe_programs_lines[
                                #           OPSTN_WKO_3_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[OPSTN_WKO_3_variable_index] = \
                            existing_probe_programs_lines[OPSTN_WKO_3_variable_index_in_existing_probe_program]

                    # ===========================================================================|
                    # Get the line from the Existing ProbeProgram and copy it in the new template|
                    # Use "WKO=4" as a text to search the line.                                  |
                    # Use " != -1 " in the 'if statement' because <find> method return (-1) if   |
                    # doesn't find the text in the line.                                         |
                    # ===========================================================================|
                    substr = "WKO=4"
                    updated_probe_program_lines_index = line.find(substr)
                    if (updated_probe_program_lines_index != -1):
                        OPSTN_WKO_4_variable_index = updated_probe_program_lines.index(line)
                        # print("OPSTN_WKO_4_variable_index:", OPSTN_WKO_4_variable_index)
                        # print(updated_probe_program_lines[OPSTN_WKO_4_variable_index])
                        for line in existing_probe_programs_lines:
                            substr = "WKO=4"  # MAYBE CAN DELETE IT LATER
                            existing_probe_programs_lines_index = line.find(substr)
                            if (existing_probe_programs_lines_index != -1):
                                OPSTN_WKO_4_variable_index_in_existing_probe_program = \
                                    existing_probe_programs_lines.index(line)
                                # print("OPSTN_WKO_4_variable_index for Existing Probe Program:",
                                #       OPSTN_WKO_4_variable_index_in_existing_probe_program)
                                # print(existing_probe_programs_lines[
                                #           OPSTN_WKO_4_variable_index_in_existing_probe_program])
                                # print()
                        updated_probe_program_lines[OPSTN_WKO_4_variable_index] = \
                            existing_probe_programs_lines[OPSTN_WKO_4_variable_index_in_existing_probe_program]

                print("----------------------------------------------------------------------------")
                print("Updated_probe_program_lines AFTER MODIFICATION:", '\n', updated_probe_program_lines)
                print("----------------------------------------------------------------------------")

                # =====================================================================|
                # [#] Call the function to create Probe Program in the Original Folder.|
                # =====================================================================|
                create_probe_program_in_original_folder(self)

            # ===========================================================================================|
            # [#] If NO ProbPrograms founded, warn the User to double check and create New ProbePrograms.|
            # ===========================================================================================|
            elif ((len(result_of_probe_program_search) == 0) and
                  (forging_number != "" and forging_number is not None)):
                close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                              font_size=16)
                self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                        "[color=ffffff]Probe Program does NOT found for Forging number of " '[b]' + forging_number + '.[/b]'
                        + '\n' + "Double Check Probe Programs Folder (maybe it saved for 'X' not 'Z' or vice versa)." +
                        '\n' + "If it is NOT there, Create new Probe Program using the New Template." + '\n' + "[/color]"),
                                                           size_hint=(0.7, 1.0), buttons=[close_button],
                                                           auto_dismiss=False)
                self.home_screen_window_program.open()
                return

            # =====================================================================================================|
            # [#] If number of ProbPrograms that founded is More than <1>, that's indicate many ProbPrograms found |
            #   for the Forging Number, therefor User needs to Double Check Probe Programs Folder and delete the   |
            #   Unnecessary programs (sometimes that happens if program saved as test or specific edition Versions)|
            # [#] Use (return) to stop the function (APP as a result) from executing the rest of the code.         |
            # =====================================================================================================|
            elif ((len(result_of_probe_program_search) > 1) and
                  (forging_number != "" and forging_number is not None)):

                # ===============================================================================================|
                # [#] Inform the User of the result of ProbPrograms that found to help to Fix the Confusion.     |
                # [#] If number of ProbPrograms that founded is less than <20>, show them to the User.           |
                # [#] If number of ProbPrograms that founded is more than <20> (it's rear), show the User general|
                #     message without the ProbPrograms because there is no enough room for more than 20 programs.|
                # ===============================================================================================|
                if (len(result_of_probe_program_search) <= 20):
                    close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                                  font_size=16)
                    self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                            "[color=ffffff]Many Probe Programs found for this Forging " '[b]' + forging_number + '.[/b]'
                            + '\n' + '\n' + ('\n'.join(result_of_probe_program_search)) + '\n' + '\n' +
                            "Fix the Confusion and Try Again." + "\n" + '\n' + "[/color]"), size_hint=(0.7, 1.0),
                                                               buttons=[close_button], auto_dismiss=False)
                    self.home_screen_window_program.open()
                    return
                else:
                    close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                                  font_size=16)
                    self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                            "[color=ffffff]Many Probe Programs found for this Forging " '[b]' + forging_number + '.[/b]'
                            + '\n' + "Fix the Confusion and Try Again." + "\n" + '\n' + "[/color]"),
                                                               size_hint=(0.7, 1.0), buttons=[close_button],
                                                               auto_dismiss=False)
                    self.home_screen_window_program.open()
                    return

        except Exception as error:
            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                          font_size=16)
            self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                    "[color=ffffff]Failed to Find, Load, or Access Probe Programs Folder" + "\n" +
                    "An Error has occurred : [/color]" + "\n" + '[color=ff1a1a]' + str(error) + '[/color]' + "\n" +
                    "[color=ffffff]Double Check Network, and File Location" + "\n"), size_hint=(0.7, 1.0),
                                                       buttons=[close_button], auto_dismiss=False)
            self.home_screen_window_program.open()
            return

    # =============================================================================|
    # [#] Create Function to Reset the Forging Number TextInput Field to start over|
    # =============================================================================|
    def reset_fields(self):
        print("(reset_fields) Function >> called")
        self.manager.get_screen('HomeScreen').ids["ForgingNumber"].text = ""

    # ====================================================================================================|
    #  Create Function to close screen message window(related to Database) when User click on Close Button|
    # ====================================================================================================|
    def close_home_screen_window_database(self, obj):
        print("(close_home_screen_window_database) Function >> called")
        self.home_screen_window_database.dismiss()

    # ===================================================================================================|
    #  Create Function to close screen message window(related to Program) when User click on Close Button|
    # ===================================================================================================|
    def close_home_screen_window_program(self, obj):
        print("(close_home_screen_window_program) Function >> called")
        self.home_screen_window_program.dismiss()


# endregion <<<<===========================================[Home Screen]============================================>>>>


# region <<<<===========================[Probe Programs Functions]============================>>>>

def create_probe_program_in_original_folder(self):
    print("(create_probe_program_in_original_folder) Function >> called")

    # ====================================================================================================|
    # [#] Define Variable to set the Program that will saved in the Original Folder.                      |
    # [#] Variable contains: Original Folder Path + "\\" + Forging Number + ".SSB" (which is the extension|
    #     that make machine able to read the File).                                                       |
    # ====================================================================================================|
    global new_probe_program_in_original_folder

    try:
        # ===============================================================|
        # [#] Set the Program to contains:                               |
        #     Original Folder Path + "\\" + Forging Number +".SSB".|
        # ===============================================================|
        new_probe_program_in_original_folder = (
                original_folder_path_of_probe_programs + "\\" +
                forging_number_for_probe_program + ".SSB")

        # ======================================================================================================|
        # [#] Set Variable to create the Program in the Original Folder.                                        |
        # [#] Steps to Create File:                                                                             |
        #    [#] Use <open()> Method To create empty File inside Folder with Parameter "x" to create the file   |
        #        if it's NOT exist on the Folder, if it is Exist, it will returns an error of (FileExistsError) |
        #    [#] Use [.write()] to Add Content of the List of Program (Main Program lines) to the File that     |
        #        Created with Use ['\n'.join()] to Add List Elements of (Main Program lines) Line by Line...    |
        #        ...(ie: [Element],new line,[Element]).                                                         |
        #    [#] Use [.close()] Method to close the File (with contents) has been created in Original Folder.   |
        # [#] Use (try/except) Blocks to Handle any Error may occur when Accessing or Finding Files and Folders.|
        # ======================================================================================================|
        try:
            create_new_probe_program_in_original_folder = open(
                new_probe_program_in_original_folder, "x")
            create_new_probe_program_in_original_folder.write(
                '\n'.join(updated_probe_program_lines))
            create_new_probe_program_in_original_folder.close()

            print("Probe Program Has been Created Successfully in ORIGINAL Folder.")
            # =======================================================================================|
            # [#] Call the function to create Probe Program in the Running Folder.|
            # =======================================================================================|
            create_probe_program_in_running_folder(self)

        except PermissionError or FileNotFoundError as error:
            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program, font_size=16)
            self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                    "[color=ffffff]Failed to Find ORIGINAL Folder location to Save the Program." + "\n" +
                    "An Error has occurred : [/color]" + "\n" +
                    '[color=ff1a1a]' + str(error) + '[/color]' + "\n" +
                    "[color=ffffff]Double Check Network, and File Location" + "\n"), size_hint=(0.7, 1.0),
                                                       buttons=[close_button], auto_dismiss=False)
            self.home_screen_window_program.open()
            return

    except(FileExistsError):
        close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program, font_size=16)
        self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                "[color=ffffff]Probe Program for " + '[b]' + forging_number + '[/b]' + " is already DONE," + "\n" +
                "Try to do another One.[/color]"), size_hint=(0.7, 1.0),
                                                   buttons=[close_button], auto_dismiss=False)
        self.home_screen_window_program.open()
        return


def create_probe_program_in_running_folder(self):
    print("(create_probe_program_in_running_folder) Function >> called")

    # ===================================================================================================|
    # [#] Define Variable to set the Program that will saved in the Running Folder.                      |
    # [#] Variable contains: Running Folder Path + "\\" + Forging Number + ".SSB" (which is the extension|
    #     that make machine able to read the File).                                                      |
    # ===================================================================================================|
    global new_probe_program_in_running_folder

    try:
        # ===============================================================|
        # [#] Set the Program to contains:                               |
        #     Running Folder Path + "\\" + Forging Number +".SSB".       |
        # ===============================================================|
        new_probe_program_in_running_folder = (
                running_folder_path_of_probe_programs + "\\" +
                forging_number_for_probe_program + ".SSB")

        # ======================================================================================================|
        # [#] Set Variable to create the Program in the Running Folder.                                         |
        # [#] Steps to Create File:                                                                             |
        #    [#] Use <open()> Method To create empty File inside Folder with Parameter "x" to create the file   |
        #        if it's NOT exist on the Folder, if it is Exist, it will returns an error of (FileExistsError) |
        #    [#] Use [.write()] to Add Content of the List of Program (Main Program lines) to the File that     |
        #        Created with Use ['\n'.join()] to Add List Elements of (Main Program lines) Line by Line...    |
        #        ...(ie: [Element],new line,[Element]).                                                         |
        #    [#] Use [.close()] Method to close the File (with contents) has been created in Original Folder.   |
        # [#] Use (try/except) Blocks to Handle any Error may occur when Accessing or Finding Files and Folders.|
        # ======================================================================================================|
        try:
            create_new_probe_program_in_running_folder = open(
                new_probe_program_in_running_folder, "x")
            create_new_probe_program_in_running_folder.write(
                '\n'.join(updated_probe_program_lines))
            create_new_probe_program_in_running_folder.close()

            print("Probe Program Has been Created Successfully in RUNNING Folder.")
            # =================================================================================================|
            # [#] Try to open both old Probe program and the updated one by Cimco Editor in the Running Folder.|
            # =================================================================================================|
            try:
                subprocess.Popen([cimco_editor_path, (new_probe_program_in_running_folder),
                                  (result_of_probe_program_search[0])])

                close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                              font_size=16)
                self.home_screen_window_program = MDDialog(title='[color=248f24]Success Message[/color]', text=(
                        "[color=ffffff]Probe Program has been created successfully."
                        + "\n" + "The Old Probe Program and the Updated One should Open By Cimco Editor shortly," + "\n" +
                        "Please Double check by using the Comparison Feature inside Cimco Editor.[/color]" + "\n"),
                                                           size_hint=(0.7, 1.0),
                                                           buttons=[close_button], auto_dismiss=False)
                self.home_screen_window_program.open()
            except Exception as error:
                close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program,
                                              font_size=16)
                self.home_screen_window_program = MDDialog(title='[color=cccc00]Warning Message[/color]', text=(
                        "[color=ffffff]Probe Program has been created successfully, but Failed to Open it by CIMCO Editor."
                        + "\n" + "An Error has occurred : [/color]" + "\n" +
                        '[color=ff1a1a]' + str(error) + '[/color]' + "\n" +
                        "[color=ffffff]Double Check Network, and CIMCO Editor Location." + "\n"), size_hint=(0.7, 1.0),
                                                           buttons=[close_button], auto_dismiss=False)
                self.home_screen_window_program.open()
                return

        except PermissionError or FileNotFoundError as error:
            close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program, font_size=16)
            self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                    "[color=ffffff]Failed to Find RUNNING Folder location to Save the Program." + "\n" +
                    "An Error has occurred : [/color]" + "\n" +
                    '[color=ff1a1a]' + str(error) + '[/color]' + "\n" +
                    "[color=ffffff]Double Check Network, and File Location" + "\n"), size_hint=(0.7, 1.0),
                                                       buttons=[close_button], auto_dismiss=False)
            self.home_screen_window_program.open()
            return

    except(FileExistsError):
        close_button = MDRaisedButton(text='Close', on_release=self.close_home_screen_window_program, font_size=16)
        self.home_screen_window_program = MDDialog(title='[color=990000]Warning Message[/color]', text=(
                "[color=ffffff]Probe Program for " + '[b]' + forging_number + '[/b]' + " is already DONE," + "\n" +
                "Try to do another One.[/color]"), size_hint=(0.7, 1.0),
                                                   buttons=[close_button], auto_dismiss=False)
        self.home_screen_window_program.open()
        return


# endregion <<<<===========================[Probe Programs Functions]============================>>>>


# region <<<<==========================================[Setting Screen]==========================================>>>>

class SettingScreen(Screen):
    pass


# endregion <<<<========================================[Setting Screen]=========================================>>>>


# region <<<<==========================================[Screen Manager]==========================================>>>>

# ==============================|
# [#] Create the screen manager.|
# ==============================|
sm = ScreenManager()
sm.add_widget(HomeScreen(name='HomeScreen'))
sm.add_widget(SettingScreen(name='SettingScreen'))


# endregion <<<<=========================================[Screen Manager]========================================>>>>


# region <<<<=======================================[Application Builder]========================================>>>>


# ================================================|
# [#] Create Class with App name to Build the App.|
# ================================================|
class ProbeProgramsMakerDB(MDApp):

    def build(self):
        # TO CONTROL SIZE OF THE SCREEN (Window.size = (WIDTH, HEIGHT))
        Window.size = (900, 650)
        # TO CHOOSE BACKGROUND MODE OF APP WHETHER DARK OR LIGHT
        self.theme_cls.theme_style = "Dark"
        # TO SET DEFAULT COLOR OF APP ELEMENTS(LABELS,BUTTONS...ETC)
        self.theme_cls.primary_palette = "Red"
        # TO SET DEFAULT COLOR CONCENTRATION(DARKNESS AND BRIGHTNESS) OF APP ELEMENTS(LABELS,BUTTONS...ETC)
        self.theme_cls.primary_hue = "900"
        # LOAD (builder_screen) TO USE IT IN THE APP
        builder_screen = Builder.load_string(Screens_Builder)
        # TO DEFINE (Screen() THAT USED TO DISPLAY THE APP) AS (app_screen) TO USE IT LATER
        app_screen = Screen()

        # BoxLayout FOR ENTIRE APP INCLUDE ALL WIDGETS AND ELEMENTS, SHOULD ADD ALL APP COMPONENTS FOR THIS BOX LAYOUT.
        # (orientation='vertical') TO ORGANIZE APP ELEMENTS VERTICALLY,
        # (spacing=20) TO MAKE SPACE BETWEEN APP ELEMENTS,
        # (padding=15) TO MAKE SPACE BETWEEN WALL BORDERS AND APP ELEMENTS,
        # (md_bg_color= [32/255.0, 32/255.0, 32/255.0, 1]) TO CHANGE THE COLOR BY ADJUSTING RGB VALUE
        # (CHECK: https://www.w3schools.com/colors/colors_picker.asp?colorhex=edfeff)
        app_box_layout = MDBoxLayout(orientation='vertical', spacing=20, padding=15,
                                     md_bg_color=[32 / 255.0, 32 / 255.0, 32 / 255.0, 1])

        # TO ADD PICTURE FOR THE APP FROM LOCAL DIRECTORY
        app_image = Image(source=r'H:\CNC_Programming\WisecoApplications\WisecoApplicationsLogo/Wiseco.gif',
                          size_hint_y=None, height=70, allow_stretch=True, pos_hint={'center_x': 0.5, 'center_y': 0.10},
                          color=[150 / 255.0, 0 / 255.0, 0 / 255.0, 1])
        # TO ADD app_image TO app_box_layout TO DISPLAY IT IN THE APP SCREEN
        app_box_layout.add_widget(app_image)

        # TO ADD Screens_Builder THAT'S CREATE ABOVE
        app_box_layout.add_widget(builder_screen)

        # ADD app_box_layout THAT CONTAIN ALL ELEMENTS AND WIDGETS OF THE APP TO app_screen
        # TO DISPLAY IT IN THE APP SCREEN.
        app_screen.add_widget(app_box_layout)
        return app_screen


ProbeProgramsMakerDB().run()

# endregion <<<<=====================================[Application Builder]=======================================>>>>
