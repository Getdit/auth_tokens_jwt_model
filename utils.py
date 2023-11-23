import curses


def menu(title, classes):
    def character(stdscr, ):
        attributes = {}

        bc = curses.COLOR_BLACK

        # make the 'normal' format
        curses.init_pair(1, 7, bc)
        attributes['normal'] = curses.color_pair(7)

        # make the 'highlighted' format
        curses.init_pair(2, 1, bc)
        attributes['highlighted'] = curses.color_pair(2)

        # handle the menu
        c = 0
        option = 0
        while c != 10:
            stdscr.erase()

            # add the title
            stdscr.addstr(f"{title}\n", curses.color_pair(1))

            # add the options
            for i in range(len(classes)):
                if i == option:
                    attr = attributes['highlighted']
                else:
                    attr = attributes['normal']

                stdscr.addstr(f'> ', attr)
                stdscr.addstr(f'{classes[i]}' + '\n', attr)
            c = stdscr.getch()

            if c == curses.KEY_UP and option > 0:
                option -= 1
            elif c == curses.KEY_DOWN and option < len(classes) - 1:
                option += 1
        return option

    return curses.wrapper(character)



from jwt import PyJWS
import base64

import json
from typing import Dict, Optional, Type

from jwt.algorithms import (
    has_crypto,
    requires_cryptography,
)
from jwt.exceptions import (
    DecodeError,
    InvalidAlgorithmError,
    InvalidSignatureError,
    InvalidTokenError,
)


def base64_encode(data):
    return bytes(base64.b64encode(data))

def base64_decode(data):
    return base64.b64decode(data)

class PersonalPyJWS(PyJWS):
    def encode(
        self,
        payload: bytes,
        key: str,
        algorithm: str = "HS256",
        headers: Optional[Dict] = None,
        json_encoder: Optional[Type[json.JSONEncoder]] = None,
    ) -> str:
        segments = []

        if algorithm is None:
            algorithm = "none"

        if algorithm not in self._valid_algs:
            pass

        # Header
        header = {"typ": self.header_typ, "alg": algorithm}

        if headers:
            self._validate_headers(headers)
            header.update(headers)

        json_header = json.dumps(
            header, separators=(",", ":"), cls=json_encoder
        ).encode()

        segments.append(base64_encode(json_header))
        segments.append(base64_encode(payload))

        # Segments
        signing_input = b".".join(segments)
        try:
            alg_obj = self._algorithms[algorithm]
            key = alg_obj.prepare_key(key)
            signature = alg_obj.sign(signing_input, key)

        except KeyError:
            if not has_crypto and algorithm in requires_cryptography:
                raise NotImplementedError(
                    "Algorithm '%s' could not be found. Do you have cryptography "
                    "installed?" % algorithm
                )
            else:
                raise NotImplementedError("Algorithm not supported")

        segments.append(base64_encode(signature))

        encoded_string = b".".join(segments)

        return encoded_string.decode("utf-8")