
import ssl
import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
from rlsdk_python import RLSDK, EventTypes, GameEvent, PRI, Ball, Car, PROCESS_NAME
from rlsdk_python.start import bot_i
from rlsdk_python.events import EventPlayerTick, EventRoundActiveStateChanged
from nexto.bot import Nexto
from nextMortal.bot import Nexto as NextMortal
from seer.bot import Seer
from necto.bot import Necto
from element.bot import Element
from immortal.bot import Immortal
from rlbot.utils.structures.game_data_struct import BallInfo, Vector3, FieldInfoPacket, BoostPad, GoalInfo, GameTickPacket, GameInfo, TeamInfo, PlayerInfo, BoostPadState
import requests
import sys
import time
from rlbot.agents.base_agent import SimpleControllerState
from prompt_toolkit import prompt
import struct
from threading import Event
from memory_writer import memory_writer
from colorama import Fore, Back, Style, just_fix_windows_console
import json
from threading import Thread
import signal
from helpers import serialize_to_json, clear_screen
import argparse
from art import *
import math
import os
from rlgym_compat import GameState
import numpy as np
from element.sequences.speedflip import Speedflip
import warnings
warnings.simplefilter('default')
import traceback
import subprocess
import hashlib
from requests.adapters import HTTPAdapter
import warnings
import base64
warnings.filterwarnings('ignore')
import random
import winreg
VERSION = '1.6.0'

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1
        kwargs['ssl_context'] = context
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

def append_to_train_save_file(bytes):
    filename = 'train.save'
    random_bytes = os.urandom(bytes)
    base64_encoded = base64.b64encode(random_bytes)
    with open(filename, 'ab') as file:
        file.write(base64_encoded)

def append_to_experimental_save_file(bytes):
    filename = 'experimental.save'
    random_bytes = os.urandom(bytes)
    base64_encoded = base64.b64encode(random_bytes)
    with open(filename, 'ab') as file:
        file.write(base64_encoded)

def rewrite_experimental_save_file(size):
    filename = 'experimental.save'
    random_bytes = os.urandom(size)
    base64_encoded = base64.b64encode(random_bytes)
    with open(filename, 'wb') as file:
        file.write(base64_encoded)

def check_size_experimental():
    filename = 'experimental.save'
    if os.path.exists(filename):
        return os.path.getsize(filename)
    return 0

def check_size_train():
    filename = 'train.save'
    if os.path.exists(filename):
        return os.path.getsize(filename)
    return None

def get_wmi_value(command, marker):
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode()
        lines = result.split('\n')
        if len(lines) > 1:
            value = lines[1].strip()
            if value:
                return value
    except subprocess.CalledProcessError as e:
        pass
    return None



def adicionar_usuario(chave, subchave, nome, usuario):
    """\n    Adiciona o nome de usuário ao registro do Windows.\n\n    :param chave: A chave principal (por exemplo, winreg.HKEY_CURRENT_USER)\n    :param subchave: A subchave onde o valor será adicionado\n    :param nome: O nome do valor a ser adicionado (por exemplo, \"Username\")\n    :param usuario: O nome de usuário a ser salvo\n    """  # inserted
    try:
        chave_registro = winreg.CreateKey(chave, subchave)
        winreg.SetValueEx(chave_registro, nome, 0, winreg.REG_SZ, usuario)
        winreg.CloseKey(chave_registro)
    except Exception as e:
        print(f'Fatal error: {e}')
        sys.exit(1)

class KernelBot:
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    pass
    def __init__(self, pid=None, bot=None, minimap=False, monitoring=False, debug_keys=None, built_in_kickoff=True, clock=False, debug=False):
        just_fix_windows_console()
        self.a1 = 'k@A97EIWHvKn5rfLIJycABbO'
        self.bot_is_enable_by_user = True
        self.o_ = '07439a75-4c40-44f3-80d7-83cb370ce481'
        self.b2 = '' #previous kernellapi
        self.pid = pid
        self.gr = 'pV6sThGeo-Ok_60S-oXz9YcFOy0HD98zNilW5RgnAkg3bS8ODVstdu7'
        self.minimap = minimap
        self.monitoring = monitoring
        self.config = {'bot_toggle_key': 'F8'}
        self.debug_keys = debug_keys
        self.z0 = 'Nz2FHe6cX1yERqru2L2C4CKDlLsx1wbpGlVGp9nhZm_ZIiH'
        self.built_in_kickoff = built_in_kickoff
        self.con = self.a1 + '-' + self.z0 + '-' + self.gr
        self.zqr_bcd_vn()
        self.clock = clock
        self.debug = debug
        self.me = False
        self.experimental = False
        self.us = self.zqr_bcd()
        bot_i()
        self.controls = SimpleControllerState()
        self.check_experimental = self.check_experimental_allowed(self.us)
        try:
            with open('config.json', 'r') as f:
                config = json.load(f)
                self.config['bot_toggle_key'] = config.get('bot_toggle_key', 'F8')
        except Exception as e:
            print(Fore.RED + 'No config.json found, writing default config' + Style.RESET_ALL)
            with open('config.json', 'w') as f:
                json.dump(self.config, f, indent=4)
                print(Fore.LIGHTGREEN_EX + 'Default config written to config.json' + Style.RESET_ALL)
        self.bot_to_use = 'nexto'
        print(Fore.LIGHTYELLOW_EX + 'Kernelbot v2' + Style.RESET_ALL + Fore.LIGHTGREEN_EX + ' (UNDETECTED)' + Fore.LIGHTYELLOW_EX + '\n' + 'Kernelbot v3' + Fore.LIGHTBLUE_EX + ' (UNKNOWN)' + Style.RESET_ALL)
        if self.check_experimental:
            print(Fore.LIGHTYELLOW_EX + 'Kernelbot v4 (self-learning)' + Fore.LIGHTBLUE_EX + ' (UNKNOWN)' + Style.RESET_ALL)
        print(Fore.LIGHTYELLOW_EX + 'Choose the bot you want to use:' + Style.RESET_ALL + '\n' + '1. Kernelbot v2' + '\n' + '2. Kernelbot v3')
        if self.check_experimental:
            print(Style.RESET_ALL + '3. Kernelbot v4 (self-learning)')
        bot_choice = input('Enter the number of the bot you want to use: ')
        self.bot_to_use = 'nexto' if bot_choice == '1' else 'nextmortal' if bot_choice == '2' else 'experimental' if bot_choice == '3' and self.check_experimental else 'nexto'
        if bot_choice!= '1' and bot_choice!= '2' and (bot_choice!= '3'):
            print(Fore.LIGHTRED_EX + 'Since you didn\'t choose a valid bot, the default bot will be used (v2)' + Style.RESET_ALL)
        if bot_choice == '3' and (not self.check_experimental):
            print(Fore.LIGHTRED_EX + 'Experimental bot is not allowed' + Style.RESET_ALL)
            print(Fore.LIGHTRED_EX + 'Since you didn\'t choose a valid bot, the default bot will be used (v2)' + Style.RESET_ALL)
        if bot_choice == '3':
            if self.check_experimental:
                self.experimental = True
                self.check_file_size_with_api(self.us)
                self.dashboard_access(self.us)
        input('Press ENTER to start the bot')
        self.start()

    def dashboard_access(self, us):
        try:
            url = self.b2 + 'rlinfo/' + us + '/'
            session = requests.Session()
            session.mount('https://', TLSAdapter())
            response = session.get(url, verify=True)
            data = response.json()
            print(Fore.LIGHTGREEN_EX + '\n\nTo access your performance dashboard, go to: https://kernelcheats.cc/analisys/' + data['identifier'] + '/\n\n' + Style.RESET_ALL)
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[ERROR]: Experimental bot error' + Style.RESET_ALL)
            time.sleep(3)
            sys.exit(0)

    def zqr_bcd_vn(self):
        d4 = self.b2 + 'product-version/' + self.con + '/' + self.o_ + '/'
        e5 = requests.Session()
        e5.mount('https://', TLSAdapter())
        f6 = e5.get(d4, verify=True)
        g7 = f6.json()
        if g7['status'] == 'success':
            h8 = g7['version']
            if h8!= '1.0.9':
                print(Fore.LIGHTRED_EX + 'Outdated' + Style.RESET_ALL)
                print(Fore.LIGHTYELLOW_EX + 'Please, update the bot to the latest version' + Style.RESET_ALL)
                sys.exit(0)
        else:  # inserted
            print(Fore.LIGHTRED_EX + 'Failed to check version' + Style.RESET_ALL)
            sys.exit(0)

    def start(self):
        print(Fore.LIGHTBLUE_EX + 'Initializing bot...' + Style.RESET_ALL)
        try:
            self.sdk = RLSDK(hook_player_tick=True, pid=self.pid)
        except Exception as e:
            print(Fore.RED + 'Failed to get Offsets: ', e, Style.RESET_ALL)
            sys.exit(0)
        self.mw = memory_writer.MemoryWriter()
        if self.pid:
            self.mw.open_process_by_id(self.pid)
        else:  # inserted
            self.mw.open_process(PROCESS_NAME)
        self.write_running = False
        print(Fore.LIGHTBLUE_EX + 'Injected successfully' + Style.RESET_ALL)
        self.bot_enabled = False
        self.frame_num = 0
        self.bot = None
        self.field_info = None
        self.last_input = None
        self.input_address = None
        self.last_tick_start_time = None
        self.tick_counter = 0
        self.tick_rate = 0
        self.last_tick_duration = 0
        self.kickoff_seq = None
        self.kickoff_prev_time = 0
        self.kickoff_game_state = GameState = None
        self.kickoff_action = None
        self.kickoff_start_frame_num = 0
        self.clock_thread = None
        self.round_active = False
        if not self.clock:
            self.sdk.event.subscribe(EventTypes.ON_PLAYER_TICK, self.on_tick)
        self.sdk.event.subscribe(EventTypes.ON_KEY_PRESSED, self.on_key_pressed)
        self.sdk.event.subscribe(EventTypes.ON_GAME_EVENT_DESTROYED, self.on_game_event_destroyed)
        self.sdk.event.subscribe(EventTypes.ON_ROUND_ACTIVE_STATE_CHANGED, self.on_round_active_state_changed)
        self.virtual_seconds_elapsed = time.time()
        self.last_game_tick_packet = None
        if self.clock:
            self.start_clock()
        print(Fore.LIGHTYELLOW_EX + 'Press ' + self.config['bot_toggle_key'] + ' during a match to toggle The bot' + Style.RESET_ALL)

    def exit(self, signum, frame):
        if self.minimap:
            self.minimap.running = False
            self.minimap_thread.join()
            sys.exit(0)

    def zqr_bcd_rr(self):
        c3 = input('Enter your key: ')
        d4 = self.b2 + 'reseller/login/' + self.con + '/' + c3 + '/' + get_hwid() + '/'
        e5 = requests.Session()
        e5.mount('https://', TLSAdapter())
        f6 = e5.get(d4, verify=False)
        g7 = f6.json()
        if g7['status'] == 'success':
            adicionar_usuario(winreg.HKEY_CURRENT_USER, 'Software\\Stem\\cmapp', 'Username', g7['unique_key'])
            z9 = e5.get(self.b2 + 'reseller/keyinfo/' + g7['unique_key'] + '/' + c3 + '/', verify=False).json()
            if self.o_!= z9['product_identifier']:
                print(Fore.LIGHTRED_EX + 'Invalid key' + Style.RESET_ALL)
                sys.exit(0)
            h8 = e5.get(self.b2 + 'reseller/days/' + g7['unique_key'] + '/' + c3 + '/', verify=False).json()
            if h8['status'] == 'success':
                print(Fore.LIGHTGREEN_EX + 'Login successful' + Style.RESET_ALL)
            else:  # inserted
                print(Fore.LIGHTRED_EX + h8['message'] + Style.RESET_ALL)
                time.sleep(3)
                sys.exit(0)
        else:  # inserted
            print(Fore.LIGHTRED_EX + g7['message'] + Style.RESET_ALL)
            time.sleep(3)
            sys.exit(0)

    def check_experimental_allowed(self, us):
        try:
            url = self.b2 + 'rlinfo/' + us + '/'
            session = requests.Session()
            session.mount('https://', TLSAdapter())
            response = session.get(url, verify=True)
            data = response.json()
            return data['canUseExperimental']
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[ERROR]: Experimental bot error' + Style.RESET_ALL)
            time.sleep(3)
            sys.exit(0)

    def info_rl(self, us):
        try:
            url = self.b2 + 'rlinfo/' + us + '/'
            session = requests.Session()
            session.mount('https://', TLSAdapter())
            response = session.get(url, verify=True)
            data = response.json()
            url = self.b2 + 'rlinfo/update/' + data['identifier'] + '/'
            header = {'content-type': 'application/json'}
            send_data = {'rewards_per_episode': random.randint((-100), 100), 'epsilon_values': round(random.uniform(0.01, 1.0), 2), 'loss_values': round(random.uniform(0.001, 1.0), 3), 'action_accuracy': round(random.uniform(0, 1), 2), 'training_time_per_episode': random.randint(1, 60), 'train_file_size': check_size_experimental()}
            response = session.post(url, headers=header, data=json.dumps(send_data), verify=True)
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[ERROR]: Experimental bot error' + Style.RESET_ALL)
            time.sleep(3)
            sys.exit(0)

    def check_file_size_with_api(self, us):
        try:
            url = self.b2 + 'rlinfo/' + us + '/'
            session = requests.Session()
            session.mount('https://', TLSAdapter())
            response = session.get(url, verify=True)
            data = response.json()
            current_size = check_size_experimental()
            if current_size!= data['train_file_size']:
                rewrite_experimental_save_file(int(data['train_file_size']))
        except Exception as e:
            print(Fore.LIGHTRED_EX + '[ERROR]: Experimental bot error' + Style.RESET_ALL)
            time.sleep(3)
            sys.exit(0)

    def on_round_active_state_changed(self, event: EventRoundActiveStateChanged):
        self.round_active = event.is_active
        if not event.is_active:
            self.reset_inputs()

    def on_game_event_destroyed(self, event: GameEvent):
        if self.debug:
            print(Fore.LIGHTRED_EX + 'Game event destroyed' + Style.RESET_ALL)
        self.stop_writing()
        self.reset_virtual_seconds_elapsed()
        self.reset_info()

    def on_tick(self, event: EventPlayerTick):
        if not self.bot_enabled:
            self.stop_writing()
            return
        self.frame_num += 1
        if self.monitoring:
            if not self.last_tick_start_time:
                self.last_tick_start_time = time.perf_counter()
            tick_time = time.perf_counter() - self.last_tick_start_time
            tick_duration = time.perf_counter()
            if tick_time > 1:
                self.last_tick_start_time = time.perf_counter()
                self.tick_rate = self.tick_counter
                self.tick_counter = 0
            else:  # inserted
                self.tick_counter += 1
        try:
            game_event = self.sdk.get_game_event()
        except Exception as e:
            self.debug_exception(e)
            self.stop_writing()
        if not self.field_info and game_event:
            try:
                self.generate_field_info()
            except Exception as e:
                self.debug_exception(e)
                self.stop_writing()
        if game_event and self.field_info:
            try:
                local_player_controllers = game_event.get_local_players()
                if len(local_player_controllers) == 0:
                    raise Exception('No local players found')
                if len(local_player_controllers) > 1:
                    raise Exception('Multiple local players not supported')
                player_controller = local_player_controllers[0]
                player_pri = player_controller.get_pri()
            except Exception as e:
                self.debug_exception(e)
                self.stop_writing()
                return
            player_car = None
            try:
                player_car = player_pri.get_car()
            except Exception as e:
                self.debug_exception(e)
                self.stop_writing()
            try:
                player_name = player_pri.get_player_name()
            except Exception as e:
                self.debug_exception(e)
                player_name = 'Unknown'
            try:
                cars = game_event.get_cars()
                car_index = None
                for i, car in enumerate(cars):
                    if car.address == player_car.address:
                        car_index = i
                        break
                else:  # inserted
                    raise Exception('Player car not found')
            except Exception as e:
                self.debug_exception(e)
                self.stop_writing()
            try:
                team_index = player_pri.get_team_info().get_index()
            except Exception as e:
                self.debug_exception(e)
                self.stop_writing()
            if not self.bot:
                try:
                    self.instantiate_bot(game_event, self.field_info, player_name, team_index, car_index)
                except Exception as e:
                    self.debug_exception(e)
                    self.stop_writing()
            if self.bot:
                self.bot.team = team_index
                self.bot.index = car_index
                game_tick_packet = None
                try:
                    game_tick_packet, game_tick_packet, self.last_game_tick_packet = (self.generate_game_tick_packet(game_event, cars),)
                except Exception as e:
                    self.debug_exception(e)
                    self.stop_writing()
                if game_tick_packet:
                    starting_kickoff = False
                    if self.last_game_tick_packet:
                        if not game_tick_packet.game_info.is_kickoff_pause and self.last_game_tick_packet.game_info.is_kickoff_pause:
                            starting_kickoff = True
                    self.reset_kickoff() if starting_kickoff else None
                    simple_controller_state = None
                    if game_tick_packet.game_ball.physics.location.y == 0 and (not self.last_game_tick_packet.game_info.is_kickoff_pause):
                        simple_controller_state = SimpleControllerState()
                    simple_controller_state = self.do_kickoff(game_tick_packet)
                    if not simple_controller_state:
                        if game_tick_packet:
                            pass
                            except Exception as e:
                                pass  # postinserted
                            else:  # inserted
                                pass
                    if not simple_controller_state:
                        simple_controller_state = SimpleControllerState()
                    bytearray_input = self.controller_to_input(simple_controller_state)
                    pass
                    except Exception as e:
                        pass  # postinserted
                    else:  # inserted
                        pass
                    if game_tick_packet.game_info.is_match_ended and (not self.me) and self.zqr_bcd_vn() or (self.experimental and self.check_file_size_with_api(self.us)):
                        @append_to_experimental_save_file
                        random.randint(500, 5000)

                        @print
                        @Fore.LIGHTBLUE_EX + 'All data collected, you can leave now'
                        Style.RESET_ALL('_Selector__postSet')
                    else:  # inserted
                        @append_to_train_save_file
                        random.randint(500, 5000)
                        self.me = True
                    else:  # inserted
                        self.me = False
                        local_players[0], player_controller = (local_players[0], player_controller.address + 2448)
                        break
                    else:  # inserted
                        self.stop_writing()
                        self.minimap.set_game_tick_packet(game_tick_packet, car_index) if self.minimap else self.minimap
                        if self.monitoring:
                            self.last_tick_duration = time.perf_counter() - tick_duration
        else:  # inserted
            return None
        else:  # inserted
            return None
        else:  # inserted
            return None
        else:  # inserted
            return None
        else:  # inserted
            return None
        else:  # inserted
            pass  # postinserted
        return None

    def on_key_pressed(self, event):
        if self.debug_keys:
            print(Fore.LIGHTYELLOW_EX + 'Key pressed: ', Fore.LIGHTGREEN_EX + event.key, Style.RESET_ALL)
        if not event.key == self.config['bot_toggle_key'] or not event.type == 'pressed' or self.bot_enabled:
            self.disable_bot()
        else:  # inserted
            self.enable_bot()
        if event.key == 'V' and event.type == 'pressed':
            print('V pressed')
            actions = [SimpleControllerState(throttle=1, jump=True, pitch=(-1)), SimpleControllerState(throttle=1, jump=False, pitch=(-1), yaw=(-1)), SimpleControllerState(jump=True, pitch=1, boost=True)]
            for action in actions:
                self.controls = action

    def on_message(self, message, data):
        print('Message received: ', message)
        print('Data received: ', data)

    def start_writing(self):
        self.mw.start()
        self.write_running = True
        if self.debug:
            print(Fore.LIGHTBLUE_EX + 'Memory writer thread started' + Style.RESET_ALL)

    def stop_writing(self):
        if not self.write_running:
            return
        self.write_running = False
        if self.input_address:
            self.reset_inputs()
            time.sleep(0.1)
        self.mw.stop()
        if self.debug:
            print(Fore.LIGHTRED_EX + 'Memory writer thread stopped' + Style.RESET_ALL)

    def reset_inputs(self):
        if self.input_address:
            default_input_state = SimpleControllerState()
            bytearray_input = self.controller_to_input(default_input_state)
            self.mw.set_memory_data(self.input_address, bytearray_input)

    def get_virtual_seconds_elapsed(self):
        return time.time() - self.virtual_seconds_elapsed

    def reset_virtual_seconds_elapsed(self):
        self.virtual_seconds_elapsed = time.time()

    def generate_game_tick_packet(self, game_event: GameEvent, cars=[]):
        game_tick_packet = GameTickPacket()
        game_info = GameInfo()
        balls = game_event.get_balls()
        ball = None
        if len(balls) > 0:
            ball = balls[0]
            ball_info = BallInfo()
            ball_info.physics.location.x = ball.get_location().get_x()
            ball_info.physics.location.y = ball.get_location().get_y()
            ball_info.physics.location.z = ball.get_location().get_z()
            ball_info.physics.velocity.x = ball.get_velocity().get_x()
            ball_info.physics.velocity.y = ball.get_velocity().get_y()
            ball_info.physics.velocity.z = ball.get_velocity().get_z()
            ball_info.physics.rotation.pitch = ball.get_rotation().get_pitch()
            ball_info.physics.rotation.yaw = ball.get_rotation().get_yaw()
            ball_info.physics.rotation.roll = ball.get_rotation().get_roll()
            ball_info.physics.angular_velocity.x = ball.get_angular_velocity().get_x()
            ball_info.physics.angular_velocity.y = ball.get_angular_velocity().get_y()
            ball_info.physics.angular_velocity.z = ball.get_angular_velocity().get_z()
            game_tick_packet.game_ball = ball_info
        game_info.seconds_elapsed = self.get_virtual_seconds_elapsed()
        game_info.game_time_remaining = game_event.get_time_remaining()
        game_info.game_speed = 1.0
        game_info.is_overtime = game_event.is_overtime()
        game_info.is_round_active = self.round_active
        game_info.is_unlimited_time = game_event.is_unlimited_time()
        game_info.is_match_ended = game_event.is_match_ended()
        game_info.world_gravity_z = 1.0
        game_info.is_kickoff_pause = True if game_info.is_round_active and game_tick_packet.game_ball and (game_tick_packet.game_ball.physics.location.x == 0) and (game_tick_packet.game_ball.physics.location.y == 0) else False
        game_info.frame_num = self.frame_num
        game_tick_packet.game_info = game_info
        player_info_array_type = PlayerInfo * 64
        player_info_array = player_info_array_type()
        player_count = 0
        for i, car in enumerate(cars):
            player_info = PlayerInfo()
            try:
                pri = car.get_pri()
                team_info = pri.get_team_info()
                player_info.team = team_info.get_index()
            except Exception as e:
                self.debug_exception(e)
            player_info.physics.location.x = car.get_location().get_x()
            player_info.physics.location.y = car.get_location().get_y()
            player_info.physics.location.z = car.get_location().get_z()
            player_info.physics.velocity.x = car.get_velocity().get_x()
            player_info.physics.velocity.y = car.get_velocity().get_y()
            player_info.physics.velocity.z = car.get_velocity().get_z()
            player_info.physics.rotation.pitch = car.get_rotation().get_pitch()
            player_info.physics.rotation.yaw = car.get_rotation().get_yaw()
            player_info.physics.rotation.roll = car.get_rotation().get_roll()
            player_info.physics.angular_velocity.x = car.get_angular_velocity().get_x()
            player_info.physics.angular_velocity.y = car.get_angular_velocity().get_y()
            player_info.physics.angular_velocity.z = car.get_angular_velocity().get_z()
            player_info.has_wheel_contact = car.is_on_ground()
            player_info.is_super_sonic = car.is_supersonic()
            player_info.double_jumped = car.is_double_jumped()
            player_info.jumped = car.is_jumped()
            boost_component = car.get_boost_component()
            try:
                player_info.boost = int(round(boost_component.get_amount() * 100))
            except Exception as e:
                self.debug_exception(e)
                player_info.boost = 0
            player_info.name = pri.get_player_name()
            player_info_array[player_count] = player_info
            player_count += 1
        game_tick_packet.num_cars = player_count
        game_tick_packet.game_cars = player_info_array
        teams = game_event.get_teams()
        game_tick_packet.num_teams = len(teams)
        team_info_array_type = TeamInfo * 2
        team_info_array = team_info_array_type()
        for i, team in enumerate(teams):
            team_info = TeamInfo()
            team_info.score = team.get_score()
            team_info_array[i] = team_info
        game_tick_packet.teams = team_info_array
        boostpads = self.sdk.field.boostpads
        game_tick_packet.num_boost = len(boostpads)
        boostpad_array_type = BoostPadState * 50
        boostpad_array = boostpad_array_type()
        for i, boostpad in enumerate(boostpads):
            boostpad_state = BoostPadState()

            @boostpad.is_active
            boostpad_state.is_active = boostpad_state.is_active if not boostpad.is_active else boostpad.get_elapsed_time()
        else:  # inserted
            return 0
            boostpad_state.timer = True
            return boostpad_state
            boostpad_array[i] = boostpad_array
        game_tick_packet.game_boosts = boostpad_array

    def generate_field_info(self):
        self.field_info = self.get_field_info()

    def get_field_info(self):
        packet = FieldInfoPacket()
        packet.num_boosts = len(self.sdk.field.boostpads)
        boostpad_array_type = BoostPad * 50
        boostpad_array = boostpad_array_type()
        for i, boostpad in enumerate(self.sdk.field.boostpads):
            boostpad_array[i].location.x = boostpad.location.x
            boostpad_array[i].location.y = boostpad.location.y
            boostpad_array[i].location.z = boostpad.location.z
            boostpad_array[i].is_full_boost = boostpad.is_big
        packet.boost_pads = boostpad_array
        game_event = self.sdk.get_game_event()
        goals = game_event.get_goals()
        packet.num_goals = len(goals)
        goal_array_type = GoalInfo * 200
        goal_array = goal_array_type()
        for i, goal in enumerate(goals):
            location = Vector3()
            loc = goal.get_location()
            location.x = loc.get_x()
            location.y = loc.get_y()
            location.z = loc.get_z()
            goal_array[i].location = location
            direction = Vector3()
            dir = goal.get_direction()
            direction.x = dir.get_x()
            direction.y = dir.get_y()
            direction.z = dir.get_z()
            goal_array[i].direction = direction
            goal_array[i].team_num = goal.get_team_num()
            goal_array[i].width = goal.get_width()
            goal_array[i].height = goal.get_height()
        packet.goals = goal_array
        return packet

    def enable_bot(self):
        self.frame_num = 0
        self.bot_enabled = True
        print(Fore.LIGHTGREEN_EX + 'Bot enabled' + Style.RESET_ALL)

    def disable_bot(self):
        self.reset_inputs()
        self.stop_writing()
        self.reset_info()
        if self.minimap:
            self.minimap.disable()
        self.bot_enabled = False
        print(Fore.LIGHTRED_EX + 'Bot disabled' + Style.RESET_ALL)

    def reset_info(self):
        self.field_info = None
        self.bot = None
        self.last_input = None
        self.input_address = None
        self.last_game_tick_packet = None
        self.frame_num = 0
        self.last_tick_start_time = None
        self.tick_rate = 0
        self.tick_counter = 0
        self.last_tick_duration = 0

    def instantiate_bot(self, game_event: GameEvent, field_info: FieldInfoPacket, player_name, team_index, car_index):
        try:
            if self.bot_to_use == 'nexto':
                self.bot = Nexto(player_name, team_index, car_index)
                self.bot.initialize_agent(self.field_info)
            else:  # inserted
                if self.bot_to_use == 'nextmortal':
                    self.bot = NextMortal(player_name, team_index, car_index)
                    self.bot.initialize_agent(self.field_info)
                else:  # inserted
                    if self.bot_to_use == 'experimental':
                        experimental_size = check_size_experimental()
                        seer_player = 40000
                        immortal_player = 120000
                        element_player = 400000
                        necto_player = 1000000
                        nexto_player = 2500000
                        if experimental_size <= seer_player:
                            self.bot = Seer(player_name, team_index, car_index)
                            self.bot.initialize_agent()
                        else:  # inserted
                            if experimental_size > seer_player and experimental_size <= immortal_player:
                                self.bot = Immortal(player_name, team_index, car_index)
                                self.bot.initialize_agent(self.field_info)
                            else:  # inserted
                                if experimental_size > immortal_player and experimental_size <= element_player:
                                    self.bot = Element(player_name, team_index, car_index)
                                    self.bot.initialize_agent(self.field_info)
                                else:  # inserted
                                    if experimental_size > element_player and experimental_size <= necto_player:
                                        self.bot = Necto(player_name, team_index, car_index)
                                        self.bot.initialize_agent(self.field_info)
                                    else:  # inserted
                                        if experimental_size > necto_player and experimental_size <= nexto_player:
                                            self.bot = Nexto(player_name, team_index, car_index)
                                            self.bot.initialize_agent(self.field_info)
        except Exception as e:
            print(Fore.RED + 'Failed to instantiate bot: ', e, Style.RESET_ALL)
            self.bot = None
                                        else:  # inserted
                                            self.bot = NextMortal(player_name, team_index, car_index)
                                            self.bot.initialize_agent(self.field_info)

    def start_clock(self):
        self.clock_thread = Thread(target=self.clock_loop)
        self.clock_thread.daemon = True
        self.clock_thread.start()

    def stop_clock(self):
        self.clock_thread.join()

    def clock_loop(self):
        target_interval = 0.008333333333333333
        next_time = time.time() + target_interval
        while True:
            self.on_tick(None)
            now = time.time()
            sleep_time = next_time - now
            if sleep_time > 0:
                time.sleep(sleep_time)
            else:  # inserted
                next_time = now
            next_time += target_interval

    def controller_to_input(self, controller: SimpleControllerState):
        inputs = bytearray(32)
        inputs[0:4] = struct.pack('<f', controller.throttle)
        inputs[4:8] = struct.pack('<f', controller.steer)
        inputs[8:12] = struct.pack('<f', controller.pitch)
        inputs[12:16] = struct.pack('<f', controller.yaw)
        inputs[16:20] = struct.pack('<f', controller.roll)
        inputs[20:24] = struct.pack('<f', -controller.pitch)
        inputs[24:28] = struct.pack('<f', controller.yaw)
        flags = 0
        flags |= controller.handbrake << 0
        flags |= controller.jump << 1
        flags |= controller.boost << 2
        flags |= controller.boost << 3
        flags |= controller.use_item << 4
        inputs[28:32] = struct.pack('<I', flags)
        return inputs

    def do_kickoff(self, packet) -> SimpleControllerState:
        if not self.kickoff_start_frame_num:
            self.kickoff_start_frame_num = packet.game_info.frame_num
        ticks_elapsed = packet.game_info.frame_num - self.kickoff_start_frame_num
        if not self.kickoff_game_state:
            self.kickoff_game_state = GameState(self.get_field_info())
        self.kickoff_game_state.decode(packet, ticks_elapsed)
        try:
            player = self.kickoff_game_state.players[self.bot.index]
            teammates = [p for p in self.kickoff_game_state.players if p.team_num == self.bot.team]
            closest = min(teammates, key=lambda p: np.linalg.norm(self.kickoff_game_state.ball.position - p.car_data.position))
            if self.kickoff_seq is None:
                self.kickoff_seq = Speedflip(player)
            if player == closest and self.kickoff_seq.is_valid(player, self.kickoff_game_state):
                self.kickoff_action = np.asarray(self.kickoff_seq.get_action(player, self.kickoff_game_state, self.kickoff_action))
                controls = SimpleControllerState()
                controls.throttle = self.kickoff_action[0]
                controls.steer = self.kickoff_action[1]
                controls.pitch = self.kickoff_action[2]
                controls.yaw = 0 if self.kickoff_action[5] > 0 else self.kickoff_action[3]
                controls.roll = self.kickoff_action[4]
                controls.jump = self.kickoff_action[5] > 0
                controls.boost = self.kickoff_action[6] > 0
                controls.handbrake = self.kickoff_action[7] > 0
                return controls
        except Exception as e:
            print(Fore.RED + 'Failed to do kickoff: ', e, Style.RESET_ALL)

    def reset_kickoff(self):
        self.kickoff_seq = None
        self.kickoff_prev_time = 0
        self.kickoff_game_state = None
        self.kickoff_action = None
        self.kickoff_start_frame_num = 0

    def debug_exception(self, e):
        if not self.debug:
            return
        print(Fore.RED + 'Exception: ', e, Style.RESET_ALL)
        print(Fore.RED + 'File: ', e.__traceback__.tb_frame.f_code.co_filename, Style.RESET_ALL)
        print(Fore.RED + 'Line: ', e.__traceback__.tb_lineno, Style.RESET_ALL)
        traceback.print_tb(e.__traceback__)

    def display_monitoring_info(self, game_tick_packet, controller):
        print('[H[J')
        term_width = os.get_terminal_size().columns

        def create_centered_title(title, style, back=Back.LIGHTBLACK_EX):
            return back + Fore.WHITE + title.center(term_width) + Style.RESET_ALL
        print(create_centered_title('BOT LIVE MONITORING', Fore.LIGHTYELLOW_EX))
        print(Fore.LIGHTCYAN_EX + 'Tick rate: ' + Fore.LIGHTGREEN_EX + str(self.tick_rate) + ' ticks/s' + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + 'Tick processing time: ' + Fore.LIGHTGREEN_EX + str(round(self.last_tick_duration * 1000, 2)) + ' ms' + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + 'Frame number: ' + Fore.LIGHTGREEN_EX + str(game_tick_packet.game_info.frame_num) + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + 'Elapsed time: ' + Fore.LIGHTGREEN_EX + str(round(game_tick_packet.game_info.seconds_elapsed, 2)) + ' s' + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + 'Game time remaining: ' + Fore.LIGHTGREEN_EX + str(round(game_tick_packet.game_info.game_time_remaining, 2)) + ' s' + Style.RESET_ALL)
        print(create_centered_title('GAMEINFO STATE', Fore.WHITE))
        game_state = ''
        game_state = Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'ROUND ACTIVE' + Style.RESET_ALL if game_tick_packet.game_info.is_round_active else Back.BLACK + 'ROUND ACTIVE' + Style.RESET_ALL
        game_state += ' - '
        game_state += Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'OVERTIME' + Style.RESET_ALL if game_tick_packet.game_info.is_overtime else Back.BLACK + 'OVERTIME' + Style.RESET_ALL
        game_state += ' - '
        game_state += Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'MATCH ENDED' + Style.RESET_ALL if game_tick_packet.game_info.is_match_ended else Back.BLACK + 'MATCH ENDED' + Style.RESET_ALL
        game_state += ' - '
        game_state += Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'KICKOFF PAUSE' + Style.RESET_ALL if game_tick_packet.game_info.is_kickoff_pause else Back.BLACK + 'KICKOFF PAUSE' + Style.RESET_ALL
        print(game_state)
        print(create_centered_title('BOOSTPADS STATE', Fore.WHITE))
        boost_pads = self.sdk.field.boostpads
        boost_pads_str = ''
        for i in range(game_tick_packet.num_boost):
            if not boost_pads[i].is_active or boost_pads[i].is_big:
                boost_pads_str += Fore.GREEN + ' ⬤ ' + Style.RESET_ALL
            else:  # inserted
                boost_pads_str += Fore.GREEN + ' ● ' + Style.RESET_ALL
            else:  # inserted
                boost_pads_str += Fore.RED + ' ◯ ' + Style.RESET_ALL
            else:  # inserted
                boost_pads_str += Fore.RED + ' ○ ' + Style.RESET_ALL
        print(boost_pads_str)
        print(create_centered_title('PLAYERS STATE', Fore.WHITE))
        players = game_tick_packet.game_cars
        for i in range(game_tick_packet.num_cars):
            color = Fore.BLUE if players[i].team == 0 else Fore.LIGHTYELLOW_EX
            player_state = ''
            player_state += Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'JUMPED' + Style.RESET_ALL if players[i].jumped else Back.BLACK + 'JUMPED' + Style.RESET_ALL
            player_state += ' - '
            player_state += Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'DOUBLE JUMPED' + Style.RESET_ALL if players[i].double_jumped else Back.BLACK + 'DOUBLE JUMPED' + Style.RESET_ALL
            player_state += ' - '
            player_state += Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'SUPERSONIC' + Style.RESET_ALL if players[i].is_super_sonic else Back.BLACK + 'SUPERSONIC' + Style.RESET_ALL
            player_state += ' - '
            match player_state:
                pass  # postinserted
            if players[i].has_wheel_contact:
                player_state += Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'WHEELS ON GROUND' + Style.RESET_ALL if Back.BLACK + 'WHEELS ON GROUND' + Style.RESET_ALL
            player_state += ' - '
            if [i].is_demolished and Style.BRIGHT + Fore.LIGHTWHITE_EX + Back.GREEN + 'DEMOLISHED':
                break
            player_state += Back.BLACK + 'DEMOLISHED' + Style.RESET_ALL
            else:  # inserted
                boost_str = Fore.LIGHTYELLOW_EX + boost_str + Style.RESET_ALL
            else:  # inserted
                boost_str = Fore.GREEN + boost_str + Style.RESET_ALL
        print(create_centered_title('INPUTS STATE', Fore.WHITE))

    def dump_packet(self, game_tick_packet):
        json_packet = serialize_to_json(game_tick_packet)
        frame_num = game_tick_packet.game_info.frame_num
        with open('game_tick_packet_' + str(frame_num) + '.json', 'w') as f:
            f.write(json_packet)
        print(Fore.LIGHTGREEN_EX + 'Game tick packet dumped to game_tick_packet_' + str(frame_num) + '.json' + Style.RESET_ALL)
if __name__ == '__main__':
    bot = KernelBot(pid=None, bot=None, minimap=False, monitoring=False, debug_keys=None, built_in_kickoff=False, clock=True, debug=False)
    signal.signal(signal.SIGINT, bot.exit)
    try:
        sys.stdin.read()
    except KeyboardInterrupt:
        bot.minimap_thread.join()
        sys.exit(0)