#!/usr/bin/python3
#coding:utf-8

from sshkey_tools.keys import RsaPrivateKey, EcdsaPrivateKey, EcdsaCurves

from settings import DEFAULT_KEYPAIR_FILENAME, DEFAULT_KEYPAIR_LOCATION


def get_keys():
    has_key = input("Você já possui uma chave SSH? (S/n) ") == "S"

    if has_key:
        key_path = input(f"Digite o caminho para a chave (Deixem em branco para {DEFAULT_KEYPAIR_LOCATION+DEFAULT_KEYPAIR_FILENAME}):\n    ") or (DEFAULT_KEYPAIR_LOCATION+DEFAULT_KEYPAIR_FILENAME)
        key_pass = input("Digite a senha da chave (Deixe em branco caso não possua senha):\n    ") or None

        priv = EcdsaPrivateKey.from_file(key_path, key_pass)

    else:
        key_path = input(f"Digite o caminho para a chave (Deixem em branco para salvar em {DEFAULT_KEYPAIR_LOCATION+DEFAULT_KEYPAIR_FILENAME}):\n    ") or (DEFAULT_KEYPAIR_LOCATION+DEFAULT_KEYPAIR_FILENAME)
        key_pass = input("Digite a senha da chave (Deixe em branco caso não possua senha):\n    ") or None

        priv = EcdsaPrivateKey.generate(EcdsaCurves.P256)
        priv.to_file(key_path, key_pass, "utf-8")
        priv.public_key.to_file(key_path + ".pub", "utf-8")


    return priv.to_string("utf-8").split("\n"), priv.public_key.to_string("utf-8"), key_path, key_path+".pub"
